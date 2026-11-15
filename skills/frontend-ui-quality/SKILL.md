---
name: frontend-ui-quality
description: Use when building or changing HTML/CSS/JS UI, or reviewing a page for accessibility, responsive layout, forms, focus states and UX copy.
version: 0.2.0
sources:
  - vercel-labs/web-interface-guidelines command.md (MIT) — adapted checklist
  - anthropics/skills skills/frontend-design (Apache-2.0) — adapted ideas
  - W3C WCAG 2.2 — referenced, not copied
---

# Frontend UI Quality (UX, accessibility, responsive)

## When to use
- Adding or changing a page, component, form, modal, list or navigation.
- "Check accessibility", "make it responsive", "review my UI".

## When not to use
- Backend-only changes. Pure visual restyling with no structural change can use the "Visual" part only.

## Read first
- The HTML structure, the CSS that applies to it, and the JS that handles its events.
- Existing design tokens/variables (colors, spacing, fonts). Reuse them; do not invent a new palette unless asked.

## Steps (build)
1. Use semantic HTML first: `<button>` for actions, `<a href>` for navigation, `<label>` for inputs, headings in order. ARIA only when HTML cannot express it.
2. Implement the feature with the project's existing patterns (same naming, same file layout).
3. Apply the quality floor below, but only to elements you created or changed.
4. Check the result at 320 px, ~768 px and desktop widths, with keyboard only, and with the browser console open (see `testing-and-verification`).

## Quality floor (checklist)
**Accessibility** (WCAG 2.2 level AA is the target)
- Every image has `alt` (`alt=""` if decorative); icon-only buttons have `aria-label`.
- Every input has a label; errors appear next to the field and are announced (`aria-live="polite"` or focus the first error).
- Everything clickable works with the keyboard (Tab, Enter/Space, Esc closes modals). No `<div onclick>` as a button.
- Visible focus style; never remove `outline` without a replacement. Use `:focus-visible`.
- Text contrast at least 4.5:1 (3:1 for large text and UI borders/icons). WCAG 1.4.3, 1.4.11.
- Click/tap targets at least 24×24 CSS px (WCAG 2.5.8); 44×44 is better for touch.
- Respect `prefers-reduced-motion`; no motion that cannot be paused if longer than 5 s.
- Do not disable zoom (`user-scalable=no`, `maximum-scale=1`).

**Responsive**
- Works at 320 px width without horizontal scrolling (WCAG 1.4.10). Use flex/grid, not JS measurement.
- Long text and empty data do not break the layout (wrap/truncate; show an empty state).
- Images have `width`/`height` (or aspect-ratio) to avoid layout shift; below-the-fold images `loading="lazy"`.

**Forms**
- Correct input `type` (`email`, `tel`, `number`) and `autocomplete`; never block paste.
- Submit stays enabled until the request starts; show progress while waiting.
- Confirm or allow undo for destructive actions.

**Code**
- No `transition: all`; animate `transform`/`opacity`.
- Keep CSS selector specificity low and consistent so rules do not cancel each other.
- Use `Intl.NumberFormat` / `Intl.DateTimeFormat` for money and dates (e.g. Thai baht).

**Copy**
- Buttons say exactly what happens ("Save changes", not "Submit"); the same action keeps the same name throughout.
- Error messages say what went wrong and how to fix it.

**Visual** (only if the request involves look and feel)
- Follow the user's brief first. If it leaves choices open, choose for this subject; avoid generic defaults (every section a rounded card with the same shadow, decorative gradients, random all-caps labels).
- One memorable element; keep the rest quiet and consistent.

## Do not expand
- Do not restyle or "fix" parts of the page you were not asked to touch; list problems you notice instead.
- Do not add a CSS framework, icon library or build step unless asked.
- Do not rewrite markup structure just to apply the checklist to old code.

## Done when
- The requested UI works and the checklist passes for every element you created or changed.
- Checked at 3 widths and by keyboard, or listed under "Not verified" with steps.

## Report (review mode: terse, file:line)
```
index.html:42 — icon button missing aria-label
style.css:18 — outline: none without focus replacement
script.js:77 — modal does not close on Esc
✓ cart.html — pass
```
Then the standard core report.

## Provenance
| Section | Origin |
|---|---|
| Quality floor items on labels, alt, keyboard, focus-visible, forms, paste, transitions, image dimensions, lazy loading, zoom, destructive actions, Intl, copy, terse file:line review format | Adapted (selected, condensed, made framework-neutral) from vercel-labs/web-interface-guidelines `command.md`, © 2025 Vercel Labs, MIT License |
| "Quality floor" idea, CSS specificity warning, avoid generic defaults, one memorable element, button labels match outcome | Adapted ideas from anthropics/skills `frontend-design`, © 2026 Anthropic, PBC, Apache License 2.0. Changes: reworded and shortened; vendor-specific text removed |
| WCAG criterion numbers and thresholds (1.4.3, 1.4.10, 1.4.11, 2.5.8) | Facts referenced from W3C WCAG 2.2 (https://www.w3.org/TR/WCAG22/); no W3C text copied |
| When/When not, Read first, build steps, 3-width check, Do not expand, Done when | Authored for this kit |
