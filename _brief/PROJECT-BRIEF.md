# Green Spring Marketing - Landing Page + Logo Rebuild

**Source email:** "New Landing Page and Logo for Green Spring Marketing website"
**From:** rajdeepdas.micronixsystem@gmail.com
**To:** rupam.micronixsystem@gmail.com | **Cc:** sumit.micronixsystem@gmail.com
**Received:** 14 September 2026, 08:59 UTC
**Message-ID:** CAHQ=Vf+7ypvyABRX6Z035_G=9K14-Tv5nzSiZ=U6Rr5CQ8YFhw@mail.gmail.com
**Thread ID:** 1a09f246c51e7ac3
**Addressed in body to:** Chandradip

---

## 1. The ask

A complete overhaul of the Green Spring Marketing website, delivered one page at
a time. The **landing page is page one**. A **brand new logo** is in the same scope.
Nothing moves to page two until this page is signed off.

Client's reasons, in their own words:

- The site has to be redone before they go looking for new business.
- The new look should let them target **high-end construction companies in other
  US markets, and any type of company**. It must not read as niche-limited.
- They will not approach **Pav** for referrals or testimonials until the whole
  site is finished, so it has to earn confidence at first look.

## 2. Access

Live site: https://greenspringmarketing.com/ (DreamHost, WordPress).

WordPress admin and SFTP credentials are **not** in this repository. They are in
`_brief/CREDENTIALS.local.md`, which `.gitignore` excludes. Ask Rupam if you need
them.

## 3. People

| Name | Role |
|---|---|
| Rajdeep Das | Sender, client contact on the thread |
| Chandradip | Addressed directly in the email body |
| Buddy | Wrote the photo direction and the logo palette tip sheet |
| Pav | Referrals and testimonials, to be asked only after launch |
| Sumit | Cc'd |

---

## 4. Logo

Supplied as `assets/from-client/09 2026 New GSM Logo.png` (1935 x 795 px, flat art).

Mark is a stacked horizontal lockup: **GREEN SPRING** in wide-tracked caps, a
thin rule either side of a **leaf** glyph, and **MARKETING** in letter-spaced
caps beneath.

**Buddy's specification:**

| Element | Colour |
|---|---|
| GREEN SPRING | Forest `#173D2E` |
| Leaf | Sage `#6B8F71` |
| Rules | Forest `#173D2E` |
| MARKETING | Sage `#6B8F71` |

**Rebuild it as a true vector SVG.** Buddy is explicit: the PNG is a design
reference only, not the production asset. Recreate it precisely so there is a
crisp scalable mark for web, print, presentations and social profiles.

**On the landing page, use the horizontal logo with no tagline.** The logo inside
the mockup is a placeholder, a different vertical lockup carrying the tagline
"BRANDS FOR A BRIGHTER FUTURE". Ignore it.

## 5. Palette

Buddy's instruction, verbatim in spirit: a tight palette, not ten different
greens. Sophisticated and natural rather than overtly green.

| Role | Name | Hex |
|---|---|---|
| Primary brand | Forest, deep almost-black green | `#173D2E` |
| Secondary | Sage, muted natural green | `#6B8F71` |
| Soft accent | Moss, pale gray-green | `#A7B89F` |
| Background | Stone, warm off-white | `#EDEBE5` |
| Primary text | Charcoal, soft black | `#2B2B2B` |
| Clean space | White | `#FFFFFF` |

Usage rules from the document:

- **Forest** for the logo wordmark, primary buttons, major accents, possibly the footer.
- **Sage** much more sparingly: the leaf, "MARKETING", small accents, hover states.
- **Stone** matters. The site must not be stark white throughout. Alternate white
  with a subtle warm stone ground for the editorial quality they liked in the mockup.
- **Charcoal**, not pure black, for body copy. Softer against natural photography.
- His headline note: **do not turn this into a green website.** The greens are
  accents. The dominant impression should be white space, warm neutrals, beautiful
  photography and dark typography, with green used strategically.

## 6. Photography

Seven images, all downloaded from source at 2400px wide into `assets/photos/`.
See `_brief/PHOTO-MANIFEST.md` for filenames, source URLs and dimensions.

Buddy's direction:

- **Licensing:** these are not public domain. The photographers retain copyright.
  They are free commercial-use stock under the Unsplash and Pexels licenses. Use
  that wording.
- **Download from the source photo page**, not from Google and not from the
  mockup, so the high-resolution file and the license are both confirmed at
  download time. Done.
- His closing observation: the real photographs make the nature system feel more
  sophisticated than the generated ones. The acorn, leaf and bark in particular
  read like an editorial magazine series rather than website stock.

## 7. Page structure from the mockup

`assets/from-client/09 26 Landing Page Visual.png` (1030 x 1540 px).

| Section | Content in the mockup |
|---|---|
| Nav | Logo left. Home / About / Services / Our Work / Insights, Forest "Contact" button right |
| Hero | Split. Left: "STRONG BRANDS" serif display over "OUTPERFORM STRONG MARKETING", italic sub "Every enduring brand begins with something worth growing.", Forest button "LET'S START THE CONVERSATION". Right: the tree photograph, with "STAND APART. LEAD THE MARKET." set small over its lower right |
| A Firmer Foundation | Stone ground, centred, short rule under the heading, one sentence of body |
| Our Strategy Gives You The Advantage | Four image cards: Brand Strategy / Brand Identity / Digital Experiences / Marketing Performance, each with a one-line description |
| Your Brand Is More Than A Logo | Two panels side by side. Left: full-bleed leaf photo with white copy over it. Right: off-white panel, "A MORE SIGNIFICANT APPROACH", "Better Opportunities. Better Business.", body, italic line, Forest button "LET'S BUILD WHAT'S NEXT" |
| Ready To Stand Apart? | Full-bleed misty mountain photo, centred heading, "Let's build a brand with staying power.", outlined button "START THE CONVERSATION" |

## 8. Things to resolve before building

- **Build target.** Nothing in the email says whether this is a WordPress theme
  or template edit on the existing DreamHost install, or a static build to be
  ported in afterwards. Both accesses were supplied, so either is possible. Ask.
- **The four-card strategy row** is the one part of the mockup that reads as a
  generic feature grid. Worth differentiating in the build while keeping the
  content and order intact.
- **Hero photograph.** The supplied link is a solitary tree at sunrise with palms
  on the horizon, not the spreading oak shown in the mockup. It is the image
  Buddy actually linked, so it is the approved one, but it changes the hero's
  character. Flag it to the client before building.
- **Contrast.** Hero copy and the "STAND APART. LEAD THE MARKET." line both sit
  over photography in the mockup. Measure against WCAG AA and solve with layout
  rather than a scrim.

## 9. Status

- [x] Email read, all details captured
- [x] Four attachments downloaded to `assets/from-client/`
- [x] Palette and photo direction extracted
- [x] All seven photographs downloaded from source at 2400px, inspected, no
      watermarks or third-party branding
- [x] Live site content harvested: all 8 service pages, About, Contact, Home
- [x] Photos cropped, graded, converted to WebP with real alt text
- [x] Home page built in HTML, verified at 390 / 768 / desktop
- [ ] Logo redrawn as a true vector SVG file for print and social
- [ ] Confirm the four-pillar to eight-service mapping with the client
- [ ] Confirm the build target with the client
- [ ] Remaining pages, once the home page is signed off

See `_brief/HOME-PAGE-NOTES.md` for the build notes and open decisions.
