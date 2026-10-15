"""Photo pipeline for the Capabilities page.

Sources live in assets/photos/ (Pexels, free commercial licence, downloaded at
2400px wide). Each is cropped to a deliberate box around a chosen focal point,
given a light grade (saturation pull plus a warm ivory tint), resized with
LANCZOS and written as WebP.

Run from the project root:  python _build/capabilities_photos.py
"""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "photos"
OUT = ROOT / "assets" / "img"

WARM = (255, 244, 224)  # warm ivory tint colour

# Default WebP quality is 88, but the weight budget here is 350 KB a file (500 KB
# for the 2400 hero), so dense-foliage frames are saved lower. Each was checked
# by eye for banding and muddy shadows.
QUALITY = {"cp-03-900": 78, "cp-int-wide-2400": 74, "cp-int-wide-1600": 74}

# stem -> (source file, [(crop box in source px, [(w, h, suffix), ...]), ...], saturation, tint strength)
# Every box has the same aspect ratio as the outputs listed with it.
PHOTOS = {
    # Low sun and haze through a green beech wood. Trunks and the sunburst sit
    # left, the right half is open haze for the headline.
    "cp-hero": ("capabilities-hero-sunlit-forest-haze.jpg", [
        ((0, 50, 2400, 1400),    [(2400, 1350, "wide-2400"), (1600, 900, "wide-1600")]),
        ((350, 0, 1630, 1600),   [(1200, 1500, "tall-1200"), (800, 1000, "tall-800")]),
    ], 0.85, 0.08),
    # Mossy trunk base spreading into roots across leaf litter.
    "cp-01": ("capabilities-01-mossy-trunk-base-roots.jpg", [
        ((0, 500, 2400, 3500),   [(900, 1125, "900"), (600, 750, "600")]),
    ], 0.90, 0.08),
    # One large veined leaf filling the frame, gold midrib running up the centre.
    "cp-02": ("capabilities-02-veined-leaf-closeup.jpg", [
        ((0, 50, 2400, 3050),    [(900, 1125, "900"), (600, 750, "600")]),
    ], 0.85, 0.10),
    # Avenue of mature trees, path vanishing to the centre of the frame.
    "cp-03": ("capabilities-03-tree-lined-avenue.jpg", [
        ((0, 400, 2400, 3400),   [(900, 1125, "900"), (600, 750, "600")]),
    ], 0.90, 0.05),
    # Green acorns clustered on an oak branch in warm sun.
    "cp-04": ("capabilities-04-acorns-on-oak-branch.jpg", [
        ((0, 600, 2400, 3600),   [(900, 1125, "900"), (600, 750, "600")]),
    ], 0.90, 0.05),
    # Backlit leafy branches overlapping against a pale hazy sky, cut to a wide
    # band. Soft background keeps the file light.
    "cp-int": ("capabilities-int-soft-leafy-branches.jpg", [
        ((0, 300, 2400, 1300),   [(2400, 1000, "wide-2400"), (1600, 667, "wide-1600")]),
    ], 0.85, 0.10),
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
