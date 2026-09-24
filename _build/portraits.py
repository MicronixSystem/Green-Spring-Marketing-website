"""Portrait pipeline for the About page.

Sources live in assets/portraits/. Each one is cropped to a deliberate square
around the face (never pasted in at its natural frame), desaturated a touch so
the faces sit with the rest of the photography, and written out at the two
widths the page asks for.

Run from the project root:  python _build/portraits.py
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "portraits"
OUT = ROOT / "assets" / "img"

# The two leaders keep the circular treatment, so they are cut square.
SQUARE = (720, 360)
# The team band frames are landscape. An upright frame across three columns came
# out around 500px tall on a desktop window, which is most of the screen for what
# is a supporting section, so these are cut head and shoulders at 7:5 instead.
WIDE = (960, 480)

# stem -> (source file, crop box, ratio, pad)
#
# pad is (sides, top) in source pixels, added before the crop by repeating the
# edge column and row. Koushik's headshot is framed tighter than the other two:
# his head fills 83% of the tallest 7:5 box the raw file can give, so a crop
# that clears his hair cuts his chin. His background is a smooth studio grey and
# the frame never reaches his shoulders, so widening the canvas there is
# invisible and buys the room the crop needs.
PEOPLE = {
    "ab-linda-2026":  ("linda-long-2026.png",   (180, 20, 1080, 920),   "square", None),
    # full source width, with the top of the frame set above the hairline so a
    # landscape crop still reads as a headshot and not as a face pressed to the glass
    "ab-ankita":      ("Ankita.jpeg",           (0, 40, 1122, 841),     "wide",   None),
    "ab-koushik":     ("Koushik Karmakar.png",  (0, 0, 1432, 1023),     "wide",   (155, 50)),
    "ab-rajdeep":     ("Rajdeep Das.png",       (0, 60, 1254, 956),     "wide",   None),
}


def pad_edges(im, sides, top):
    """Grow the canvas by repeating the edge column and row."""
    w, h = im.size
    out = Image.new("RGB", (w + sides * 2, h + top))
    out.paste(im, (sides, top))
    if sides:
        out.paste(im.crop((0, 0, 1, h)).resize((sides, h)), (0, top))
        out.paste(im.crop((w - 1, 0, w, h)).resize((sides, h)), (w + sides, top))
    if top:
        strip = out.crop((0, top, out.width, top + 1)).resize((out.width, top))
        out.paste(strip, (0, 0))
    return out


def build(stem, filename, box, ratio, pad):
    im = Image.open(SRC / filename).convert("RGB")
    if pad:
        im = pad_edges(im, *pad)
    im = im.crop(box)
    if ratio == "square":
        side = min(im.size)
        im = im.crop((0, 0, side, side))
        sizes = [(w, w) for w in SQUARE]
    else:
        sizes = [(w, round(w * 5 / 7)) for w in WIDE]
    for w, h in sizes:
        r = im.resize((w, h), Image.LANCZOS)
        p = OUT / f"{stem}-{w}.webp"
        r.save(p, "WEBP", quality=88, method=6)
        print(f"{p.relative_to(ROOT)}  {w}x{h}  {p.stat().st_size // 1024} KB")


def main():
    for stem, spec in PEOPLE.items():
        build(stem, *spec)


if __name__ == "__main__":
    main()
