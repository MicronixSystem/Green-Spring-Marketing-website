# About page revision, 24 September 2026

Source: Linda's "RESENDING About Page", which forwards her 18 September note and
adds three lines on top. Attachments are in `email/18-09-2026/acout page changes/`.

## What she asked for

| # | Her instruction | Status |
|---|---|---|
| 1 | Use the rewritten team bios (`Team Bios.docx`) | Done, all four |
| 2 | Use her new bio (`Linda Long.docx`) | Done |
| 3 | Use her new photo (`Linda Long.png`) | Done |
| 4 | Follow Buddy's layout (`09 17 26 Visual for About.png`) | Partly. See the judgment call |
| 5 | Use a plant that is legal to use for copyright | Nothing to do, already true |
| 6 | Keep her and Chandradip side by side | Done, kept as it was |
| 7 | New title for Chandradip | Done. `Team Bios.docx` already says VP, Project Management |
| 8 | Offer to lengthen Chandradip's bio through Buddy | Take it. See the measurement |

## Copyright on the imagery

Already settled before this round and worth repeating back to her. Every photograph
on the site came from Unsplash or Pexels under their free commercial licence, every
file was inspected for watermarks and third-party branding, and none is on a paid
licence. The provenance table is in `PHOTO-MANIFEST.md`. Her worry almost certainly
came from Buddy's mock, which generated its own plant and its own faces.

## The judgment call on layout

Her two instructions pull in different directions. Buddy's layout gives Linda a
section of her own and puts Chandradip in a row of four with the rest of the team.
Her newer line says she loves them side by side as the page has them now.

The newer line wins, so the leadership band keeps Linda and Chandradip side by side
exactly as built, and the three new people go in a row underneath once there are
photographs. Her pull quote from Buddy's right rail is now the standing quote band
further down the page.

## The measurement behind taking her bio offer

At 1440 the two columns come out:

| Column | Height |
|---|---|
| Linda | 725px |
| Chandradip | 458px |
| Gap | 267px |

Her bio runs about 180 words, his about 70. The column was previously being held
open by `align-self:stretch`, which filled the gap by stretching his box rather than
by giving it anything to hold. That has been removed. The hairline is now drawn on
the grid with `.people::after`, so the divider still runs the full height without
anyone's box being stretched to reach it.

Removing the stretch stopped the box being inflated, but it did not stop the hole:
267px of bare ground sat under his bio, which Rupam picked up on sight.

### How it was actually closed

Waiting on her longer bio was not a fix, so the column was given real content and
both bios were made easier to read at the same time:

- The opening paragraph of each bio is now a standfirst, set larger and in Forest.
  Five even paragraphs of grey gave the reader nowhere to land.
- Each person carries an "Areas of focus" list under the bio, set as a stacked
  hairline list rather than chips. This is the client's own copy from their previous
  site, not anything invented: Linda had three items, Chandradip six, and that
  difference is what does most of the closing.

| | Before | After |
|---|---|---|
| Linda | 725px | 1012px |
| Chandradip | 458px | 923px |
| Gap | 267px | 89px |

89px is about three lines, which is ordinary editorial ragging rather than a hole,
and both columns now end on the same kind of element. Measured across twelve widths
the gap runs between 10 and 105px wherever the two sit side by side.

Worth telling her that the focus lists came back, since she did not ask for them.
They stay useful even when the longer bio arrives.

## The team band

Rupam supplied the three headshots on 24 September, so the band is built.

It is deliberately the opposite of the leadership band above it, because the two
would otherwise read as one long list of people:

| | Leadership | Team |
|---|---|---|
| Ground | Stone `#EDEBE5` | Stone warm `#E3E0D7` |
| Frame | Circle, beside the name | Landscape 7:5 rectangle, above the name |
| Columns | Two, split by a hairline | Three |
| Head | Heading with a lede in a right rail | Heading and line on one baseline |

Type is set to the column it has rather than left small in a wide space: at 1440
the name runs 29px and the bio 18px in a 398px column, which is a 45 character
measure. Nothing is stretched. `align-items:start` on the grid means the three
columns end where their content ends, and because the bios run 44, 55 and 54
words they come out within 57px of each other at the widest.

### The frames were too big on the first pass

Built upright at 4:5 they came out 398 by 498 at 1440, which is 55% of a 900px
window for what is a supporting section. Rupam: "the images are too big. it
takes almost screen."

They are now landscape at 7:5, 398 by 284, which is 32% of the same window. The
band went from 1212px to 999px, so the heading, all three faces, all three names
and all three bios now sit inside one desktop screen.

The crops were re-cut from the sources rather than the 4:5 renders being squashed
into a wider box. The first landscape attempt cropped the tops of two heads off,
because the frame was centred on the face instead of being set above the
hairline. The boxes in `portraits.py` now take the full source width with the top
of the frame above the hair, so a landscape crop still reads as a headshot.

Koushik then came out cut off at the chin, which Rupam spotted. His headshot is
framed tighter than the other two: his head fills 83% of the tallest 7:5 box the
raw file can give, so any crop that clears his hair loses his chin. No crop box
fixes that. His background is a smooth studio grey and the frame never reaches his
shoulders, so `portraits.py` now grows his canvas first, repeating the edge column
and row, and crops from the larger canvas. The padding is invisible on a gradient
and buys the room the crop needs. That is what the `pad` field in `PEOPLE` is for.

The row layout between 521 and 980 went from a 34% picture column to 40% at the
same time, because a landscape frame at 34% came out only 119px tall.

### Two faults found and fixed while checking, not after

- The upright frame collapsed to nothing below 520px. `align-items:start` from
  the row layout was carrying down into the stacked flex layout, and a flex item
  only takes the width of its column when it is allowed to stretch into it.
- Between 521 and 980 the role label drifted up to 44px away from the name. The
  picture spans all three rows there, and its height was being shared out across
  them. Fixed by sizing the rows `max-content max-content 1fr`, so the slack
  lands under the bio instead of between the name and the role.

Measured at 360, 390, 480, 520, 560, 640, 768, 860, 980, 1180, 1440 and 1760.
No overflow at any of them, the frame renders at every width, and the gap
between name and role is a steady 6 to 7px throughout.

## How this page is verified

The Chrome extension could not be used, because the account has several machines
paired and only the one on this desk is allowed. Verification runs instead
against the Chrome installed on this machine, in headless mode, against the local
preview server:

- `_build/measure.html` loads the page in same origin iframes at twelve widths
  and reports frame size, the picture's share of the window, the bio measure in
  characters, the name to role gap, how far the three columns differ, and every
  contrast pair, measured on the rendered page. Driven with `--dump-dom`.
- `_build/shot.html` frames one section for a screenshot. Headless ignores a URL
  hash, and the reveal animation holds everything at opacity 0 until the observer
  fires, so both are forced before the shot is taken.

Both harnesses kill transitions before measuring. A transition outranks even an
`!important` override while it is running, so without that the contrast check
reads every colour as fully transparent and reports a flat 1:1 for the whole
page, which is what it did on the first attempt.

The frame in `shot.html` is sized from the query string rather than `innerWidth`
or `100vw`. Headless reports both before `--window-size` has finished applying,
and the frame ends up wider than the shot, which crops the right edge and makes
a page that does not overflow look like it does.

## Source images

Sources are in `assets/portraits/`, unedited as supplied. `_build/portraits.py`
holds the crop box for each face and regenerates every derivative, so the
framing is reproducible rather than a one off. All three were inspected: no
watermarks, no third party branding, no paid licence. They carry the same
`grayscale(.12)` the leadership circles use, which is what pulls Koushik's grey
studio background and the two office backgrounds into one family.

## Also changed

- `.ab-intro` now answers "why Green Spring Marketing" in her framing: what changed,
  what did not, where we start.
- The standing quote is now hers, attributed to her, replacing the anonymous
  "regardless of your company's size" line.
- The chip lists under each bio are gone. They were not in her layout and the new
  bios carry the detail.
- Two British spellings corrected to American so the page does not mix registers
  with her copy: recognised, optimisation.

## Still to raise with her

- The hero read "Two senior people on the leadership team". Now that the team band
  is in, that counts five, so it reads "Five people you will work with by name".
- The hero still reads "Forty years of experience". That is the client's own
  long-standing claim so it was left alone, but her new copy says three decades,
  and the two sit two sections apart.

## Verified

- Contrast: 16 pairs measured on the rendered page at every width, all pass WCAG AA. Lowest is
  4.95:1 on the team bios against Stone warm.
- No horizontal overflow at any of the twelve widths measured.
- Nav and footer still byte identical to `index.html`, compared by walking the tag
  tree rather than by regex.
- No duplicate ids, no dead anchors, every image has alt text.
- Zero em dashes.
- `about.css?v=34`.
