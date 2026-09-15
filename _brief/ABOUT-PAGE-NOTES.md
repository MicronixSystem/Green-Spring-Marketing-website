# About page, build notes

Built 15 September 2026. Page two of the rebuild.

```
about.html
assets/css/about.css      About only. Shares every token with site.css.
assets/photos-about/      3 new source photographs at 2400px
assets/portraits/         the two real portraits harvested from the live site
```

Loads `site.css` for the system, then `about.css` for this page's sections.
`site.js` is shared, no About-specific script.

---

## Same system, no repeated sections

Linda asked for the same theme without the same design. Every token, the type,
the buttons, the nav and the footer are shared with the home page. Not one
section structure is reused.

| | Home page | About page |
|---|---|---|
| Hero | photo full bleed, plate floated on it | type led on Stone, photo as a band at the foot |
| Opening | head row, two full bleed panels | one statement, then three plain facts |
| List | branching diagram with icons | a ledger of full width rows, no icons |
| Photo + copy | photo left, type right, black ground | plate overlapping the photograph's edge |
| People | compact typographic rows, no portraits | portraits, full bios, second row mirrored |
| Statement | white type on the photograph's own black | Forest type on Stone, photo as a panel right |
| Close | photograph with a Forest plate on it | type only, no photograph |

The statement sections are deliberate mirrors of each other: home runs photo
left with white type on black, About runs type left in Forest on Stone with the
photograph as a full height panel on the right.

## Content

Every word is from the client's own live About page, or from their home page
where noted. Nothing invented.

- The forty years, the nationally recognised firms, B2B and B2C, and the seven
  expertise areas are all verbatim from the live About page.
- Both leadership bios are theirs, lightly trimmed.
- "We help you grow to capacity" and the engagement paragraphs come from their
  live home page and were not used on our home page.
- The pull quote is their sentence, unchanged.

The seven expertise descriptions are the only new copy on the page. They
describe what each discipline is, and make no claim about the client.

## Photographs

Three new ones, none shared with the home page, all Pexels licence, verified
"Free to use" on each photo page before download.

| Use | File | Source |
|---|---|---|
| Hero band | `ab-hero-*` | pexels.com/photo/14845820 |
| Growth | `ab-growth-tall-*` | pexels.com/photo/327856 |
| Statement panel | `ab-branches-*` | pexels.com/photo/30606192 |

All three are cropped to their section and run through the same grade as the
home page photographs, so the two pages read as one series.

## The portraits

The live About page carries real photographs of both leaders, so the home page's
"no portraits" problem is solved with the client's own assets rather than by
inventing anything.

They are weak, and you should ask for better ones:

- **Linda Long** is only 397 x 398 px. That is enough at the size used here and
  nowhere near enough for anything larger.
- **Chandradip Ghosh** is a full length shot in different light, from 2021, with
  a black border baked into the file.

Both are cropped to the face, desaturated toward each other and held small so
the mismatch does not dominate. It works, but two proper headshots taken the
same way would lift the page considerably.

## Shared nav and footer

The nav, mobile menu and footer markup is now byte identical on both pages,
verified by hash. Links are written page qualified (`index.html#services`), and
`site.js` collapses them to a plain hash when they already point at the current
page, so the home page keeps its smooth scrolling. The current page gets
`aria-current`, which draws the small underline under About.

The home page nav gained About and Services and lost Approach and Team, so the
same five entries work from both pages. The home page's leadership section now
ends with a link through to About.

## One correction to the home page notes

The home page notes said every label pair cleared AA. That was measured on the
solid colours, not on the labels set at reduced opacity. Three small caps labels
at `.6` opacity measured 3.4 to 3.7:1, which passes only as large text and these
are 10.5 to 12px. Every Forest label on both pages is now at `.78`, measured
between 5.17:1 and 6.15:1 depending on the ground.

## Filling the sections

Rupam flagged dead space in three sections. Rather than patch only those, I
measured every section: sampling a grid over each one, counting the share
actually covered by content, and finding the largest single empty rectangle.
That showed the opening and closing bands were worse than the three named.

| Section | Filled before | after | Largest void before | after |
|---|---|---|---|---|
| Growth | 47% | 100% | 31% | 0% |
| Leadership | 51% | 83% | 31% | 12% |
| Expertise | 62% | 67% | 31% | 8% |
| Statement | 56% | 61% | 20% | 18% |
| Hero | 55% | 60% | 21% | 15% |
| Close | 26% | 33% | 27% | 19% |
| Opening | 15% | 25% | 35% | 27% |

What changed:

- **Growth** is now a full bleed band with both columns running the whole
  height, the photograph left and the white plate overlapping it from the
  right. The plate carries the three stages of an engagement, which fills it.
- **Leadership** rows are the grid themselves. The portrait is a tall panel
  bled to the page edge, the bio runs in two columns so it reaches the far
  side, and the second row is mirrored on white.
- **Expertise** rows now anchor both edges the way an index is set: name flush
  left, description flush right, a mark at the far edge. The dead right third
  is gone.
- **Opening** statement runs the full measure instead of stopping two thirds
  across, and the three facts sit directly beneath it.
- **Close** is three columns, heading and action left, the lede centred in the
  middle, contact details dividing the right into equal bands.

The opening and closing bands still read low on the coverage measure. Both are
type on a flat ground with no photograph, so the number is always going to be
low there; what matters is that neither has a hole in it any more.

## Second pass on height and alignment

Rupam asked for three more things: fix the empty top of the hero, and cap both
"How an engagement starts" and the leadership section at one screen.

**Hero.** The eyebrow was being pushed to the top of the column by a
`space-between`, orphaning it above a large hole. It now sits with the headline,
and the two counted figures moved into the foot of the same column, so a tall
window fills with content instead of air. Both columns bottom align.

**How an engagement starts** is now `100svh` minus the nav. It was overrunning
that by 248px because the photograph's `height:100%` fell back to its own
intrinsic height inside an auto height grid item; the image is now absolutely
positioned so it fills without contributing height. Inside the white plate the
three stages divide the lower part into equal bands, so the plate has no idle
white in it.

**Leadership** was redesigned. It used to be two stacked rows with the portrait
blown up into a tall bled panel, which upscaled Linda's 397px file badly. It is
now a single screen: both people side by side, split by one hairline, each with
a small square portrait beside the name, then the bio, then the tags, with the
three blocks spread over the column height.

Because these sections hold real copy, a short window cannot always take them at
full size. Two height queries step the type and spacing down below 900px and
again below 740px. Verified at 1440x700, 1600x900 and 1880x1010: all three
sections land exactly on the budget at every one.

## Checks run

- Zero em dashes. No banned phrases. No placeholders. No numbered list markers.
- Every image has real alt text. No photograph appears on both pages.
- Contrast measured on all seventeen pairs, and against the rendered pixels
  where type sits on a photograph. The hero band line is 9.9:1 at phone and
  tablet width and 10.5:1 on desktop.
- Nav checked at 1181, 1280, 1366 and 1440: no crowding.
- 390, 768 and desktop checked. No horizontal overflow anywhere.
- Portraits are held at a size their source files can carry. Below 980px they
  stop stretching into panels and sit as squares, because Linda's original is
  only 397px and was visibly upscaled and over cropped as a tall panel.
- Hero is capped at one screen minus the nav, matching the home page.
