"""Photo pipeline for the Editorial page.

Downloads the five sources from Pexels (free commercial licence) at 2400px wide
into assets/photos/, then crops each to a deliberate box around a chosen focal
point, gives it a light grade (saturation pull plus a warm ivory tint), resizes
with LANCZOS and writes WebP into assets/img/.

Every frame is green and in leaf, and none repeats a frame already used on the
home, about, approach or capabilities pages.

Run from the project root:  python _build/editorial_photos.py
Pass --no-download to re-run the conversion against the files already on disk.
"""
import sys
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "photos"
OUT = ROOT / "assets" / "img"

WARM = (255, 244, 224)  # warm ivory tint colour, same as the other two pages

# Pexels photo id per source file. The download URL is the standard Pexels
# delivery path; w=2400 is the widest size the other pages were built from.
SOURCES = {
    "editorial-hero-green-summer-woodland.jpg": 35598596,
    "editorial-01-lone-tree-on-green-hillside.jpg": 18010149,
    "editorial-02-misty-green-valley-hillside.jpg": 17596403,
    "editorial-03-ivy-on-pale-stone-column.jpg": 18109193,
    "editorial-more-fern-stream-in-green-wood.jpg": 35639154,
}

# Dense summer foliage is expensive, so the big frames are saved lower than the
# default 88. Each was checked by eye for banding and muddy shadows.
QUALITY = {
    "ed-hero-wide-2400": 72, "ed-hero-wide-1600": 76, "ed-hero-wide-1200": 80,
    "ed-hero-tall-1200": 76, "ed-hero-tall-800": 80,
    "ed-more-wide-2200": 74, "ed-more-wide-1400": 78,
    "ed-01-1200": 82, "ed-02-1200": 82, "ed-03-1200": 84,
}

# stem -> (source file, [(crop box in source px, [(w, h, suffix), ...]), ...],
#          saturation, tint strength)
# Every box carries the same aspect ratio as the outputs listed with it.
PHOTOS = {
    # Summer woodland interior: dark trunks, a green understorey across the
    # bottom and small gaps of pale sky. Cut to a wide band for the hero.
    # The tall box is for phones, where the band is nearly square and the wide
    # crop would show one narrow vertical slice of it.
    "ed-hero": ("editorial-hero-green-summer-woodland.jpg", [
        ((0, 190, 2400, 1190), [(2400, 1000, "wide-2400"),
                                (1600, 667, "wide-1600"),
                                (1200, 500, "wide-1200")]),
        ((660, 0, 1740, 1350), [(1200, 1500, "tall-1200"),
                                (800, 1000, "tall-800")]),
    ], 0.88, 0.10),
    # One broad lime standing clear of the treeline on a green hillside. The
    # source is already 3:2, and a tighter box cut the top of the crown and
    # turned the tree into a hedge, so the full frame is kept. The saturation
    # pull is mostly there to take the hard blue out of the sky.
    "ed-01": ("editorial-01-lone-tree-on-green-hillside.jpg", [
        ((0, 0, 2400, 1600), [(1200, 800, "1200"), (800, 533, "800")]),
    ], 0.86, 0.10),
    # Layered green hillside under morning mist. Cropped left and high to drop
    # the village in the foreground and the houses on the right.
    "ed-02": ("editorial-02-misty-green-valley-hillside.jpg", [
        ((0, 400, 1650, 1500), [(1200, 800, "1200"), (800, 533, "800")]),
    ], 0.92, 0.05),
    # Ivy in leaf against the moulded base of a pale stone column: the brief's
    # "refined architectural lines" without a line of office stock in sight.
    "ed-03": ("editorial-03-ivy-on-pale-stone-column.jpg", [
        ((0, 1000, 2400, 2600), [(1200, 800, "1200"), (800, 533, "800")]),
    ], 0.88, 0.06),
    # Fern fronds over a narrow stream, the water carrying the warm brown of
    # the bed. Cut to a long shallow strip. The box sits low in the source:
    # higher up the frame is all out of focus and the strip read as mud.
    "ed-more": ("editorial-more-fern-stream-in-green-wood.jpg", [
        ((0, 2150, 2294, 2880), [(2200, 700, "wide-2200"),
                                 (1400, 445, "wide-1400")]),
    ], 0.88, 0.08),
}


def download():
    import requests

    SRC.mkdir(parents=True, exist_ok=True)
    for name, pid in SOURCES.items():
        dest = SRC / name
        if dest.exists():
            print(f"have  {dest.relative_to(ROOT)}")
            continue
        url = (f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg"
               f"?auto=compress&cs=tinysrgb&w=2400")
        r = requests.get(url, timeout=90, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        dest.write_bytes(r.content)
        print(f"got   {dest.relative_to(ROOT)}  {len(r.content) // 1024} KB")


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
    if "--no-download" not in sys.argv:
        download()
    total = 0
    for stem, spec in PHOTOS.items():
        build(stem, *spec)
    for p in OUT.glob("ed-*.webp"):
        total += p.stat().st_size
    print(f"\ned-*.webp on disk: {total / 1024:.0f} KB")


if __name__ == "__main__":
    main()
