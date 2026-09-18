"""Build the "Your brand is more than a logo" photograph.

Source: the flat-lay Rupam generated on 18 Sep 2026, saved unedited at
assets/from-client/brand-world-source.png. It is generated with no legible
lettering anywhere, because small type is where these renders give themselves
away. The real wordmark is composited on afterwards from the client's own logo
file, so the only text in the frame is genuinely theirs and genuinely sharp.

    python _build/brand_world.py
"""
import os
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(HERE, 'assets/from-client/brand-world-source.png')
LOGO = os.path.join(HERE, 'assets/from-client/09 2026 New GSM Logo.png')
OUT  = os.path.join(HERE, 'assets/img')

STONE, MOSS = (238, 236, 230), (163, 181, 156)
QUAD  = [(671, 488), (908, 536), (879, 684), (639, 635)]   # the card, TL TR BR BL
RW, RH = 560, 350                 # rectified card space
BAND  = (138, 266)                # the render's printed rules, in card space
CLEAN = (14, 132)                 # a rule-free strip of the same card, for grain
LOGO_W = 0.66                     # share of the card width the mark occupies

CROPS = [                         # name, box in the 1536x1024 master, widths
    ('brand-world',   (205, 0, 1229, 1024), (1024, 720)),   # desktop column, 1:1
    ('brand-world-w', (110, 40, 1470,  890), (1360, 800)),  # stacked, 1.6:1
]


def coeffs(dst, src):
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -x*u, -y*u]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -x*v, -y*v]); B.append(v)
    return np.linalg.solve(np.array(A, float), np.array(B, float))


def blur(a, r):
    return np.asarray(Image.fromarray(np.clip(a, 0, 255).astype('uint8'))
                      .filter(ImageFilter.GaussianBlur(r))).astype(float)


def vmedian(a, k=9):
    p = np.pad(a, ((k//2, k//2), (0, 0), (0, 0)), mode='edge')
    return np.median(np.stack([p[i:i+a.shape[0]] for i in range(k)]), axis=0)


def repair(rect):
    """Drop the render's printed rules, keeping the card's lighting and grain.
    A row-profile correction will not do it: the rules do not span the full
    width, so flattening the row only inverts them."""
    y0, y1 = BAND
    low  = blur(vmedian(rect[y0:y1]), 7)
    c    = rect[CLEAN[0]:CLEAN[1]]
    res  = c - blur(c, 7)
    grain = np.tile(res, (int(np.ceil((y1-y0)/res.shape[0])), 1, 1))[:y1-y0]
    ramp = np.ones(y1-y0); n = 8
    ramp[:n] = np.linspace(0, 1, n); ramp[-n:] = np.linspace(1, 0, n)
    rect[y0:y1] = rect[y0:y1]*(1-ramp[:, None, None]) + (low+grain)*ramp[:, None, None]
    return rect


def mark(width):
    """Area-average the resize. Lanczos shatters the logo's hairline rules into
    dashes at this size; a box filter leaves them continuous and faint."""
    a   = np.asarray(Image.open(LOGO).convert('RGB')).astype(float)
    lum = a @ [0.2126, 0.7152, 0.0722]
    al  = np.clip((250-lum)/200, 0, 1)
    ys, xs = np.nonzero(al > 0.06)
    sl  = (slice(ys.min(), ys.max()+1), slice(xs.min(), xs.max()+1))
    al, a, lum = al[sl], a[sl], lum[sl]
    leaf = ((a[:, :, 1] > a[:, :, 0]+14) & (lum > 70)).astype(float)
    h  = max(1, round(width*al.shape[0]/al.shape[1]))
    rs = lambda m: np.asarray(Image.fromarray((m*255).astype('uint8'))
                              .resize((width, h), Image.BOX)).astype(float)/255
    return np.clip(rs(al)**0.72, 0, 1), rs(leaf)


def brand_the_card(base):
    W, H = base.size
    c = coeffs([(0, 0), (RW, 0), (RW, RH), (0, RH)], QUAD)
    rect = np.asarray(base.transform((RW, RH), Image.PERSPECTIVE, c, Image.BICUBIC)).astype(float)

    light = rect @ [0.2126, 0.7152, 0.0722]
    light = np.clip(light/light.mean(), .78, 1.22)
    rect = repair(rect)

    A, L = mark(int(RW*LOGO_W))
    th, tw = A.shape
    x0, y0 = (RW-tw)//2, (RH-th)//2
    ink = np.where(L[..., None] > .45, np.array(MOSS, float), np.array(STONE, float))
    rect[y0:y0+th, x0:x0+tw] = (rect[y0:y0+th, x0:x0+tw]*(1-A[..., None])
                                + ink*light[y0:y0+th, x0:x0+tw][..., None]*A[..., None])

    # Warp back through a 2x canvas and area-average down. A direct warp to the
    # master point-samples, and the rules dash again.
    S = 2
    inv = coeffs([(x*S, y*S) for x, y in QUAD], [(0, 0), (RW, 0), (RW, RH), (0, RH)])
    warped = (Image.fromarray(np.clip(rect, 0, 255).astype('uint8'))
              .transform((W*S, H*S), Image.PERSPECTIVE, inv, Image.BICUBIC)
              .resize((W, H), Image.LANCZOS))

    cx, cy = (sum(p[0] for p in QUAD)/4, sum(p[1] for p in QUAD)/4)
    inset = [(x+(cx-x)*0.014, y+(cy-y)*0.014) for x, y in QUAD]   # stay off the printed edge
    m = Image.new('L', (W*S, H*S), 0)
    ImageDraw.Draw(m).polygon([(x*S, y*S) for x, y in inset], fill=255)
    m = m.resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.5))
    return Image.composite(warped, base, m)


def grade(im):
    """The paper reads warmer than the page's stone, and the foliage sits below
    the four pillar photographs. Neutralise, then lift chroma into their range."""
    a = np.asarray(im).astype(float) * np.array([0.991, 1.000, 1.021])
    lum = (a @ [0.2126, 0.7152, 0.0722])[..., None]
    return Image.fromarray(np.clip(lum + (a-lum)*1.32, 0, 255).astype('uint8'))


def main():
    master = grade(brand_the_card(Image.open(SRC).convert('RGB')))
    for name, box, widths in CROPS:
        c = master.crop(box)
        for w in widths:
            h = round(w * c.height / c.width)
            p = os.path.join(OUT, '%s-%d.webp' % (name, w))
            c.resize((w, h), Image.LANCZOS).save(p, 'WEBP', quality=86, method=6)
            print('%-34s %4dx%-4d %6.1f KB' % (os.path.basename(p), w, h,
                                               os.path.getsize(p)/1024))


if __name__ == '__main__':
    main()
