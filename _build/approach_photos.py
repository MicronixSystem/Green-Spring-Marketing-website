"""Photo pipeline for the Approach page.

Sources live in assets/photos/ (Pexels, free commercial licence, downloaded at
2400px wide). Each is cropped to a deliberate box around a chosen focal point,
given a light grade (saturation pull plus a warm ivory tint) so the six sit with
the existing photography, then resized with LANCZOS and written as WebP.

Run from the project root:  python _build/approach_photos.py
"""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "photos"
OUT = ROOT / "assets" / "img"

WARM = (255, 244, 224)  # warm ivory tint colour

# Default WebP quality is 88. These two were over 400 KB and are saved lower;
# checked by eye for banding in the sky and mud in the shadows.
QUALITY = {"ap-rel-wide-2400": 72, "ap-step3-1600": 72}

# stem -> (source file, [(crop box in source px, [(w, h, suffix), ...]), ...], saturation, tint strength)
#
# A box is (left, top, right, bottom) in source pixels. Every box has the same
# aspect ratio as the outputs listed with it, so the resize never squashes.
PHOTOS = {
    # Two bare trees in fog, finely branched, against a flat warm ivory sky. The
    # left two fifths of the wide box is clean sky for the headline. A leafy
    # replacement was tried and dropped: the best in-leaf candidates were either
    # trunk-dominant or had a cold blue sky that fights the warm palette, and
    # this frame sits with the misty heroes already on the home and about pages.
    # The tall box stops short of the second trunk so one tree carries the phone.
    "ap-hero": ("approach-hero-winter-trees-fog.jpg", [
        ((0, 0, 2400, 1500),    [(2400, 1500, "wide-2400"), (1600, 1000, "wide-1600")]),
        ((520, 0, 1720, 1500),  [(1200, 1500, "tall-1200"), (800, 1000, "tall-800")]),
    ], 1.0, 0.0),
    # Twisting grey branches and tendrils over soft green. Focus on the knot of
    # crossings around x 1100-1300.
    "ap-step1": ("approach-step1-intertwined-branches.jpg", [
        ((200, 100, 2236, 1500), [(1600, 1100, "1600"), (800, 550, "800")]),
    ], 0.75, 0.10),
    # The amber tree on the misty hillside, centred, with dark conifers around it.
    "ap-step2": ("approach-step2-amber-tree-in-grove.jpg", [
        ((300, 900, 2100, 2137), [(1600, 1100, "1600"), (800, 550, "800")]),
    ], 0.90, 0.05),
    # Backlit canopy, bright gap right of centre.
    "ap-step3": ("approach-step3-light-through-canopy.jpg", [
        ((74, 0, 2400, 1600),    [(1600, 1100, "1600"), (800, 550, "800")]),
    ], 0.70, 0.12),
    # Fresh leaves on grey old wood, branch running lower left to upper right.
    "ap-step4": ("approach-step4-new-buds-on-branch.jpg", [
        ((0, 0, 2326, 1600),     [(1600, 1100, "1600"), (800, 550, "800")]),
    ], 0.85, 0.08),
    # Live-oak limbs meeting overhead. The band stops above the red path so only
    # canopy and a little shaded grass remain.
    "ap-rel": ("approach-rel-oak-canopy-overhead.jpg", [
        ((0, 40, 2400, 1240),    [(2400, 1200, "wide-2400"), (1600, 800, "wide-1600")]),
    ], 0.60, 0.10),
}


def grade(im, sat, tint):
    if sat != 1.0:
        im = ImageEnhance.Color(im).enhance(sat)
    if tint:
        im = Image.blend(im, Image.new("RGB", im.size, WARM), tint * 0.5)
    return im


def build(stem, filename, crops, sat, tint):
    im = grade(Image.open(SRC / filename).convert("RGB"), sat, tint)
    for box, sizes in crops:
        c = im.crop(box)
        for w, h, suffix in sizes:
            assert abs(c.width / c.height - w / h) < 0.01, (stem, suffix)
            r = c.resize((w, h), Image.LANCZOS)
            p = OUT / f"{stem}-{suffix}.webp"
            r.save(p, "WEBP", quality=QUALITY.get(p.stem, 88), method=6)
            print(f"{p.relative_to(ROOT)}  {w}x{h}  {p.stat().st_size // 1024} KB")


def main():
    for stem, spec in PHOTOS.items():
        build(stem, *spec)


if __name__ == "__main__":
    main()
