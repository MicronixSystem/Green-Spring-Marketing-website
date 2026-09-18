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
