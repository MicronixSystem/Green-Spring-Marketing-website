# Green Spring Marketing, website rebuild

Rebuild of [greenspringmarketing.com](https://greenspringmarketing.com/), one page
at a time. The home page is page one. A new logo is part of the same brief.

## Preview

```bash
python serve.py          # http://127.0.0.1:8127, served with Cache-Control: no-store
```

The CSS and JS links carry a `?v=` query. Bump it when you change either file, or
browsers will hold the old copy.

## Layout

```
index.html                 the home page
assets/css/site.css        tokens, layout, responsive, reduced-motion
assets/js/site.js          reveals, counters, scroll rule, menu, nav state
assets/img/                cropped, graded WebP plus the favicon
assets/photos/             the seven source photographs at 2400px
assets/from-client/        the four files the client sent, untouched
_brief/                    brief, photo manifest, build notes
serve.py                   local preview server
```

## Brand

Palette is Buddy's tip sheet, sampled exactly. The greens are accents, not the
ground: the page is warm neutrals, white space, photography and dark type.

| Role | Name | Hex |
|---|---|---|
| Primary | Forest | `#173D2E` |
| Secondary | Sage | `#6B8F71` |
| Soft accent | Moss | `#A7B89F` |
| Background | Stone | `#EDEBE5` |
| Body text | Charcoal | `#2B2B2B` |

Sage measures 3.04:1 on Stone, so it is used only for the logotype and icon
strokes, never for text.

Type is Fraunces for display and Jost for everything else.

## Credentials

WordPress and SFTP logins are **not** in this repository. They live in
`_brief/CREDENTIALS.local.md`, which `.gitignore` excludes. Ask Rupam.

## Where to start reading

`_brief/HOME-PAGE-NOTES.md` covers what each section is, the decisions that need
the client's sign-off, and what is still open. `_brief/PROJECT-BRIEF.md` is the
original brief. `_brief/PHOTO-MANIFEST.md` lists every photograph with its source
and licence.
