# Home page, build notes

Built 14 September 2026. Static HTML, ready to port into WordPress.

```
index.html
assets/css/site.css      tokens, layout, responsive, reduced-motion
assets/js/site.js        reveals, counters, scroll rule, menu, nav state
assets/img/*.webp        20 files, the 7 photographs cropped and graded
assets/img/favicon.svg   leaf mark
serve.py                 local preview on http://127.0.0.1:8127 with no-store
```

Preview with `python serve.py`. The CSS and JS links carry a version query, so
bump `?v=` when you change either.

---

## What the page is

The client called it a landing page, but it is the site's home page and page one
of a full rebuild. Every word on it is real: taken from their live site, from the
mockup, or from Buddy's two documents. Nothing is invented.

| Section | Ground | Layout | Source of the copy |
|---|---|---|---|
| Hero | photograph | full-bleed photo, copy on its own Stone plate right | mockup |
| A firmer foundation | Stone, white, Forest | one screen tall, head row then two full-bleed panels | mockup + live home page |
| Our strategy gives you the advantage | warm Stone | four frames on a staggered baseline | mockup |
| Your brand is more than a logo | the photograph's own black | leaf left, type right | mockup + live branding page |
| Figures | Forest | four counted figures on one row | live About page |
| One system, eight capabilities | Stone | drawn branching diagram | live service pages |
| When you choose us | light Stone | sticky heading left, stepped list right | live home page |
| The people on your account | Stone | typographic rows, no portraits | live About page |
| Ready to stand apart? | photograph | photo fills the band, line left, Forest plate right | mockup + live contact page |
| Footer | deep Forest | four columns | live contact page |

No two consecutive sections share a ground, a column structure or a reading
direction.

## Decisions you should look at

**The four pillars map onto the eight real services.** That mapping is mine, not
the client's, and it is the one thing on the page they have not already approved:

- Brand Strategy: Branding and Strategy, Content Marketing
- Brand Identity: Website Development, Print Marketing
- Digital Experiences: Search Engine Optimisation, Email Marketing
- Marketing Performance: Online Advertising, Social Media Marketing

**Two of Buddy's photo assignments are swapped.** He put the dark single leaf
under Brand Identity and the bright leaf detail under "more than a logo". I
reversed them. The dark leaf is the only frame in the set whose own black can
carry white type at 21:1, and "more than a logo" is the section that needed type
on a photograph. The bright leaf measures 1.1:1, which no amount of art direction
fixes without a scrim.

**Text sits on photographs in three places, never behind a scrim.** Measured
before placing, and re-measured against the rendered pixels: hero corner 7.1:1,
statement band 21:1, closing line 7.9:1. The closing invitation itself still gets
a solid Forest plate, because the bright half of that photograph measures 2.9:1
and no crop fixes that.

**No portraits in the leadership section.** Linda Long and Chandradip Ghosh are
real people. I will not generate a likeness of either, and there is no photograph
of them in anything the client sent. The section is typographic instead, which
needs no placeholder and reads as deliberate. If they want faces there, the
client has to supply real headshots.

**Nothing else is a placeholder.** All seven photographs are the real files from
Buddy's links, cropped, graded to one look and converted to WebP. No image prompt
is outstanding.

## Two sections reworked after first review

Both were carrying too much empty space.

**A firmer foundation** was a centred statement with the left and right thirds
empty, and the section ran well past a screen. It is now capped at exactly
`100svh` minus the nav and carries no idle space.

The head is one row: the title left, the statement right. Below it two panels run
full bleed to the window edges, white against Forest, and stretch to fill whatever
height is left. The content is the comparison from the client's own home page,
how most marketing firms work against how Green Spring works, three points a side.

Those points divide each panel into three equal bands separated by hairlines,
with the text centred in its band. That way the panel height reads as structure
rather than as gaps, however tall the screen is. Measured at 1440x818 the section
comes to 726px against a 726px budget, and at 1440x860 it is 768 against 768.

On phones the panels have to stack, so one screen is not achievable without
cramming. It settles at 768px there, tightened from 811.

**Ready to stand apart?** had dead sky across the left and an empty strip of
Stone under the photograph. The mountain shot is re-cropped from further down the
frame, so the empty upper sky is gone and the layered ridgelines carry the left
side. The photograph now fills the whole band rather than 62 per cent of it, so
there is no Stone strip. The left holds a real line from the client's contact
page, "The best marketing strategy is the one that grows with you", set straight
on the shadowed valley at a measured 7.9:1.

Below 1180px that line can no longer find a dark part of the photograph, so it
takes its own ground and joins the plate as one block.

## Still open

- The hero photograph is the solitary tree Buddy linked, not the spreading oak in
  the mockup. It is his choice, but it changes the hero's character. Worth showing
  the client before the next page.
- The logo on the page is live type plus an SVG leaf. Buddy also wants a true
  vector logo file for print, presentations and social. That is a separate
  deliverable, not part of the home page.
- Build target still unconfirmed: WordPress theme work on the DreamHost install,
  or keep building static and port at the end.
- Contact goes to `mailto:` for now. If they want a form on the home page, it
  needs the same fields as the live Quick Contact Form.

## Checks run

- Zero em dashes across every file. No banned phrases. No placeholders.
- Every image has real alt text. No photograph used twice. None pasted at
  natural size; each is cropped to its section and graded to match the others.
- Contrast measured, not eyeballed. Every body and label pair clears WCAG AA.
  Sage is 3.04:1 on Stone, so it is used only for the logotype and icon strokes,
  never for text.
- 390, 768 and desktop all checked in the browser. No horizontal overflow at any
  width, menu open or closed.
- Console is clean. Motion is fully disabled under `prefers-reduced-motion`.
