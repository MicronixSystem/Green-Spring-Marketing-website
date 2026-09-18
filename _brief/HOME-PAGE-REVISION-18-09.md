# Home page revision, 18 September 2026

Built to Linda's direction document of 17 September
(`email/18-09-2026/home page changes/`). Her note was explicit that the visual
direction is right and this round is content hierarchy and pacing, so nothing
about the aesthetic was rethought.

Preview with `python serve.py`, then `index.html?v=25`.

---

## What she asked for, and what was done

| Her instruction | Done |
|---|---|
| Remove the How most firms work / How we work comparison | Removed |
| Remove the 40+ / 25+ / 15+ / 8 statistics | Removed |
| Remove the eight capability service list | Removed |
| Remove When you choose us | Removed |
| Hero: keep the design, use the new copy | Done |
| A firmer foundation: headline becomes Your brand is more than a logo | Done |
| Keep the four disciplines and the staggered photography | Kept |
| Regrade or replace the bright green leaf | Regraded |
| Rework the connected line concept around the four disciplines | Done |
| New section: Better Opportunities. Better Business., on the black leaf | Done |
| Final CTA simplified, nothing after it but the footer | Done |
| Tighten the largest vertical gaps | Done |

The page went from nine sections to six. It is 5,048px tall at desktop, down
from about 6,900px.

Her story order now reads straight down the page: why brand matters, what Green
Spring does, how the disciplines connect, what that means for the client, start
the conversation.

## The photograph she flagged

She was right about the bright green leaf. Measured mean saturation across the
four frames:

| | before | after |
|---|---|---|
| Acorn | 0.14 | 0.14 |
| Leaf | **0.73** | **0.38** |
| Bark | 0.45 | 0.45 |
| Branch | 0.37 | 0.37 |

It was regraded rather than replaced, so Buddy's original selection is kept. It
now sits inside the range of the other three.

## The hero plate, after Rupam flagged it

He was right that the copy looked stranded. Measured: the plate's inner width is
547px, and the two paragraphs were capped at `32ch` and `40ch`, which rendered
at 380px and 359px. Every paragraph line therefore stopped 170 to 190px short of
the plate's right padding, leaving a wedge of bare stone down the right of the
block. The headline was the only thing reaching the edge.

The caps could not simply be dropped: at the current sizes that gave the lede a
six character last line and left the second paragraph with a one word orphan.
The plate is sized to the headline, so the paragraphs had to grow into the same
measure. They are now `clamp(20px,1.91vw,29px)` and `clamp(16px,1.38vw,21px)`,
with `text-wrap:balance` on the lede and `pretty` below it.

The short window queries had the same fault in reverse: the headline steps down
to 60px and then 50px, but the plate stayed 650px wide, so at a 660px window the
headline itself was stranded 203px short. The plate now steps down with it, to
580px and 472px.

Worst line gap in the plate's paragraphs, measured:

| Viewport | Before | After |
|---|---|---|
| 1920x1080 | 396 | 110 |
| 1520x950 | 413 | 119 |
| 1520x820 | 438 | 124 |
| 1520x660 | 465 | 94 |
| 768x1024 | 442 | 197 |

The eyebrow, the italic middle line of the headline and the button are still
short. Those are intrinsically short elements, and that rag is the design.

## Judgment calls she delegated

**"Every enduring brand begins with something worth growing."** Her document
grouped this with STAND APART. LEAD THE MARKET. on the tree image, but offered
the alternative of running it below the hero as a transition into A Firmer
Foundation. It is on the transition, because two blocks of type on the
photograph measured 1.36:1 against white. It now opens the foundation section
above a rule, which is the bridge she described.

**STAND APART. LEAD THE MARKET.** stays on the tree as she asked. Doing that
properly needed a fix: the photograph was anchored at `62%` vertically, so on a
short window the dark band at the foot of the frame was cropped away and the
line fell on lit grass. The image is now anchored to its own bottom, so the
shadowed band is present at every height. Measured on the file: 7.9:1 at the
95th percentile, 5.0:1 at the 99th.

## Two things that follow from the removals

**The nav had dead links.** How we work pointed at a section she moved off the
page, and Services pointed at the eight capability list that is now gone.
Neither of those pages exists yet. The nav is About, Capabilities, Approach for
now, and the two entries come back when those pages are built. The footer's
eight service names now point at the four disciplines in the interim.

**Nothing on the homepage names SEO, web development, email or the rest.** That
is her explicit intent, and it is the right call editorially. Worth her knowing
it removes those terms from the homepage for search, since the Services page
will need to carry them.

## Spelling

Switched to American spelling to match her copy: recognizable, optimization.

## Checks run

- Zero em dashes. No banned phrases, no placeholders, no numbered list markers.
- Seven images, all with real alt text, none repeated.
- Nineteen colour pairs measured, all clear WCAG AA. Type on photography
  measured against the file, not eyeballed.
- Largest empty rectangle per section: hero 0%, foundation 19%, capabilities
  17%, flow 15%, statement 6%, close 0%.
- Hero is exactly one screen minus the nav at 1280x660, 1440x700, 1536x820,
  1600x900 and 1880x1010. Two height queries step the plate down on short
  windows, because her new hero copy is two paragraphs rather than one.
- 390, 768 and desktop checked. No horizontal overflow. Console clean.
- Nav and footer still byte identical with about.html. No duplicate ids, no
  dead anchors on either page.

## Not committed

Held out of git on Rupam's instruction.

---

# Second round, same day

Built to Linda's refinement note of 18 September
(`email/18-09-2026/home page changes/new/`). Her framing: not a redesign, "the
next layer of refinement".

Preview with `python serve.py`, then `index.html?v=31`.

## What she asked for, and what was done

| Her instruction | Done |
|---|---|
| Give "Your brand is more than a logo" a real visual | Built. Left keeps the headline, the photograph takes the right and bleeds off the page edge |
| Tighten the space around the bridge line, Our strategy, One connected system | Done. Those sections came down 237px between them |
| Check rendered heights, not only padding: something may be held open | Found it. `.stmt` carried `min-height:min(92svh,860px)` |
| Balance nature imagery with the actual work | The new photograph is the first image on the page showing what GSM makes |
| Descenders cut off in the hero headline | Fixed |
| Remove the street address from the CTA area and the footer | Removed everywhere it appeared |
| Remove the old footer positioning sentence | Removed. Phone and email take that column |
| Keep hero, connected system, leaf section, final CTA | Untouched |

## The photograph

Rupam generated it from a prompt written to produce **no legible lettering
anywhere**, because small type is where these renders give themselves away.
Linda's own reference shows it: her brand book reads "CH&TITY / CONTRJIVITYY /
GROHECTION".

The real wordmark is composited onto the business card afterwards from
`assets/from-client/09 2026 New GSM Logo.png`, so the only text in the frame is
genuinely the client's and genuinely sharp. The render's printed rules are
removed from the card first, keeping its own lighting and paper grain.

Rebuild with `python _build/brand_world.py`. Source kept unedited at
`assets/from-client/brand-world-source.png`.

Graded to sit with the four pillar photographs: foliage saturation 0.205 to
0.270, against a family range of 0.206 to 0.708.

## Heights before and after, measured at 1520x900

| Section | Before | After | |
|---|---|---|---|
| Hero | 808 | 808 | unchanged |
| A firmer foundation | 672 | 975 | gained the photograph |
| Our strategy gives you the advantage | 924 | 880 | −44 |
| One connected system | 753 | 683 | −70 |
| Better Opportunities. Better Business. | 828 | 738 | −90 |
| Ready to stand apart? | 833 | 800 | −33 |
| **Page** | **5295** | **5337** | **+42** |

The four sections she named lost 237px. The page is 42px longer overall,
because the space she disliked was replaced with a picture rather than simply
closed up.

She was right about a minimum height. `.stmt` was held open 93px past its
content at a 900px window. It is now `min(82svh,740px)` and the content drives
it, with 3px to spare.

## The hero descenders

`.mask` carries `overflow:hidden` for the line-by-line reveal, and the line box
is `.98em`, tighter than the glyphs. The g and the p fell outside it and were
clipped. The clip box now extends `.17em` lower with a matching negative margin,
so nothing moves, and the slide starts at 128% rather than 105% so the next line
still cannot peek through the taller box.

## The hero plate, after Rupam flagged it

He was right that the copy looked stranded. Measured: the plate's inner width is
547px, and the two paragraphs were capped at `32ch` and `40ch`, which rendered
at 380px and 359px. Every paragraph line therefore stopped 170 to 190px short of
the plate's right padding, leaving a wedge of bare stone down the right of the
block. The headline was the only thing reaching the edge.

The caps could not simply be dropped: at the current sizes that gave the lede a
six character last line and left the second paragraph with a one word orphan.
The plate is sized to the headline, so the paragraphs had to grow into the same
measure. They are now `clamp(20px,1.91vw,29px)` and `clamp(16px,1.38vw,21px)`,
with `text-wrap:balance` on the lede and `pretty` below it.

The short window queries had the same fault in reverse: the headline steps down
to 60px and then 50px, but the plate stayed 650px wide, so at a 660px window the
headline itself was stranded 203px short. The plate now steps down with it, to
580px and 472px.

Worst line gap in the plate's paragraphs, measured:

| Viewport | Before | After |
|---|---|---|
| 1920x1080 | 396 | 110 |
| 1520x950 | 413 | 119 |
| 1520x820 | 438 | 124 |
| 1520x660 | 465 | 94 |
| 768x1024 | 442 | 197 |

The eyebrow, the italic middle line of the headline and the button are still
short. Those are intrinsically short elements, and that rag is the design.

## Judgment calls

**The bridge line stays above the split.** That leaves bare stone to the right
of it. Measured, the largest void in the section is 11%, which is inside
tolerance, and it is breathing room around a pull quote rather than a hole in a
content block. Folding it into the left column would close the gap but force the
photograph into a 0.82 frame, which crops the foliage out.

**"Sellersburg, Indiana" is left in the footer's bottom bar.** It is a city, not
a street address, and removing a local firm's location entirely costs them in
search. One line to delete if she wants it gone.

## To raise with her

- The render is 1536x1024. It carries a standard 125% display at full density,
  but it is soft on a 2x screen. A larger render of the same prompt would fix it
  and nothing else would need to change.
- The About page's contact band lost its Office row with the address. Two rows
  left, type sized up so they are not stretched over the old three.

## Not committed

Held out of git on Rupam's instruction.
