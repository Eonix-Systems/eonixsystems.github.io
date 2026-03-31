# Eonix Systems — Website Developer Handbook

> **For the developer taking over this project:** Read this entire file before touching a single line of code. It will save you hours.

---

## 📌 Project Overview

This is the **official marketing and engineering manifesto website** for [Eonix Systems](https://eonixsystems.com/) — a hardware company building intelligent, modular power infrastructure for embedded and robotic systems.

The website is deployed as a **static site on GitHub Pages** at:
- **Live URL:** `https://eonixsystems.com/` (custom domain via CNAME)
- **GitHub Repo:** `https://github.com/Eonix-Systems/eonixsystems.github.io`

**No build process. No frameworks. No package.json.** This is vanilla HTML, CSS, and JavaScript. You open a file, you edit it, you push it to GitHub — that's the entire deployment pipeline.

---

## 📁 Folder Structure

```
eonix_systems_website/
│
├── index.html              ← HOME PAGE
├── ecosystem.html          ← ECOSYSTEM / Architecture page
├── product.html            ← PRODUCT / System Explorer page
├── about.html              ← ABOUT / Engineering Manifesto page
├── contact.html            ← CONTACT page
│
├── assets/
│   └── EONIX SYSTEMS LOGO.png   ← Main brand logo (used in nav + favicon)
│
├── css/
│   ├── base.css            ← ⭐ START HERE: Global CSS variables (colors, spacing)
│   ├── layout.css          ← Page wrapper + section max-widths
│   ├── nav.css             ← Fixed top navbar
│   ├── footer.css          ← Site-wide footer
│   ├── animations.css      ← Scroll-reveal animations + hero grid effect
│   ├── home.css            ← Styles specific to index.html
│   ├── product.css         ← Styles specific to product.html (segmented control, diagrams)
│   ├── ecosystem.css       ← Styles specific to ecosystem.html (scroll-spy diagram)
│   ├── about.css           ← Styles specific to about.html (manifesto/blueprint look)
│   └── contact.css         ← Styles specific to contact.html
│
├── js/
│   ├── diagram.js          ← ⭐ COMPLEX: Canvas-based animated system diagram
│   ├── nav.js              ← Simple hamburger menu toggle
│   └── scroll-reveal.js    ← IntersectionObserver for fade-in animations
│
├── _build_scripts/         ← Internal AI-generated helper scripts. IGNORE THESE.
│
├── CNAME                   ← GitHub Pages custom domain config (eonixsystems.com)
├── robots.txt              ← SEO: tells crawlers what to index
├── sitemap.xml             ← SEO: sitemap for search engines
└── README.md               ← You are here.
```

---

## 🎨 Design System

### Colors (defined in `css/base.css` as CSS variables)

| Variable | Value | Usage |
|---|---|---|
| `--bg-main` | `hsl(220, 20%, 6%)` | Main dark background |
| `--bg-soft` | `hsl(220, 18%, 10%)` | Card & section backgrounds |
| `--bg-card` | `hsl(220, 15%, 12%)` | Elevated card backgrounds |
| `--text-primary` | ~White | Headings, primary text |
| `--text-secondary` | ~Cool Grey | Body text, descriptions |
| `--accent-primary` | `#00e5ff` | Cyan — used for highlights, active states, CTAs |
| `--border-subtle` | White @ 8% opacity | Dividers, card borders |

> **IMPORTANT:** Never hardcode color values in page CSS files. Always use the CSS variables from `base.css`. This makes future theming possible.

### Fonts (loaded from Google Fonts in `base.css`)
- **Outfit** — Used for all headings (`h1`–`h6`)
- **Inter** — Used for all body text and UI
- **Space Mono** — Used sparingly in `about.html` for "code-like" technical labels

### Spacing
- `--nav-height: 80px` — All pages have `padding-top: var(--nav-height)` via `.page-wrapper`
- `--section-spacing: 120px` — Standard gap between major page sections
- `max-width` for page content: `1400px` (nav/footer) and `1500px` (content)

---

## 📄 Page-by-Page Breakdown

### `index.html` — Home Page
**Purpose:** First impression. Converts visitors into curious engineers.  
**Key Sections:** Hero → Why Eonix Exists → Built for Deployment → The Gap → Who It's For → Final CTA  
**CSS:** `base.css` + `layout.css` + `nav.css` + `animations.css` + `footer.css` + `home.css`  
**JS:** `scroll-reveal.js`, `nav.js`  
**Key Classes:** `.home-title`, `.home-subtitle`, `.btn-primary`, `.btn-secondary`, `.connected-cards-container`

### `ecosystem.html` — Ecosystem / Architecture
**Purpose:** Technical deep-dive. Shows the 4-layer system architecture using a scroll-driven diagram.  
**Key Feature:** Split-screen layout — left side scrolls through 4 architecture steps; right side shows the animated canvas diagram that STICKS (position: sticky) and reacts to each scroll step.  
**CSS:** Includes `product.css` AND `ecosystem.css` (plus base/nav/footer/home)  
**JS:** `scroll-reveal.js`, `nav.js`, `diagram.js` (the big one)  
**⚠️ WARNING:** The sticky diagram is sensitive. `ecosystem.css` has a comment explaining the `height: 100%` fix. Do NOT add this back.

### `product.html` — Product / System Explorer
**Purpose:** Interactive product showcase. Users can click tabs (Control, Sensing, Power, Actuation) to explore each layer.  
**Key Feature:** Segmented Control Bar (iOS-style sliding tabs) + Canvas Diagram + contextual content panels.  
**CSS:** `base.css` + `layout.css` + `nav.css` + `animations.css` + `footer.css` + `product.css` + `home.css`  
**JS:** `scroll-reveal.js`, `nav.js`, `diagram.js` + inline `<script>` at the bottom of the file  
**⚠️ WARNING:** The inline `<script>` at the bottom of `product.html` is critical for the tab switching logic. The functions `switchSysTab()` and `selectSensor()` are defined there. Do NOT move them to an external file without updating all `onclick="..."` attributes.

### `about.html` — Engineering Manifesto
**Purpose:** Brand authority page. 9-section "manifesto" that tells the Eonix story.  
**Key Feature:** "Blueprint Tech" aesthetic with vertical guide lines, tech dividers, and 2x2 symmetrical grids.  
**CSS:** `base.css` + `layout.css` + `nav.css` + `animations.css` + `footer.css` + `about.css` + `home.css`  
**JS:** `scroll-reveal.js`, `nav.js`  
**Note:** Uses `Space Mono` font (loaded inline in `about.html`'s `<head>`, not in `base.css`).

### `contact.html` — Contact Page
**Purpose:** Direct engineering inquiry channel. Minimal by design.  
**CSS:** `base.css` + `layout.css` + `nav.css` + `animations.css` + `footer.css` + `contact.css`  
**JS:** `nav.js`, `scroll-reveal.js`

---

## ⚙️ JavaScript Files

### `diagram.js` — Canvas Diagram Engine
This is the most complex file in the project. It renders an animated, interactive system architecture diagram using the HTML5 Canvas API.

**How it works:**
- It draws nodes (Motherboard, CAN Bus, Power, Sensors, etc.) on a `<canvas>` element
- It targets a **global variable** `window.activeDiagramStep` (1–4) to know which layer to highlight
- On `ecosystem.html`, the IntersectionObserver in the inline script updates `activeDiagramStep` as the user scrolls
- On `product.html`, the `switchSysTab()` function updates `activeDiagramStep` when a tab is clicked
- It also responds to `window.forceHoverNodeId` so that hovering over bullet points highlights specific diagram nodes

**Do NOT:**
- Remove the global variable `window.activeDiagramStep`
- Change the canvas element's ID from `systemCanvas`
- Change `data-step` attributes on `.arch-scroll-step` elements without updating diagram.js

### `nav.js` — Hamburger Menu
Simple 3-line script. Toggles the `.open` class on `.nav-links` when the hamburger button is clicked. Fully responsive, works on all pages.

### `scroll-reveal.js` — Scroll Animations
Uses the `IntersectionObserver` API. When elements with class `.reveal` enter the viewport, the class `.is-visible` is added, triggering the CSS transition defined in `animations.css`. Supports directional variants: `.reveal-left`, `.reveal-right`, `.reveal-scale`.

---

## 🚀 Deployment

The site is hosted on **GitHub Pages** from the `main` branch.

**To push changes live:**
```bash
# From d:\eonix_systems\Development\eonix_systems_website\
git add .
git commit -m "your descriptive message"
git push origin main
```
Changes go live within ~60 seconds on GitHub Pages.

**Custom Domain:** Configured via the `CNAME` file (contains `eonixsystems.com`). Do NOT delete this file.

---

## ⚠️ Known Pitfalls & Important Notes

1. **CSS Cache:** All CSS/JS imports use a version query string (e.g., `?v=500`). If you make CSS changes that aren't appearing on the live site, increment this number on all `<link>` tags for that specific CSS file.

2. **Image Filenames with Spaces:** The logo file is named `EONIX SYSTEMS LOGO.png` — with spaces. In HTML `src` attributes, reference it as `assets/EONIX SYSTEMS LOGO.png`. Do NOT use `%20` encoding — it has caused favicon bugs in the past.

3. **Sticky Diagram Bug (FIXED):** `ecosystem.css` had `height: 100%` on `.interactive-diagram` which broke `position: sticky`. This was already removed. If the sticky diagram breaks again, check for any `height: 100%` on the parent containers of `.sticky-wrapper`.

4. **No .html URL Removal:** GitHub Pages requires `.html` extensions on all files for routing to work correctly. **Do NOT remove `.html` from navigation `href` attributes** without implementing a custom 404.html redirect strategy.

5. **About Page Font:** `Space Mono` is loaded only in `about.html`'s `<head>`. If you add tech labels (`.tech-label` class) to other pages, add the Google Fonts import for Space Mono there too.

---

## 📬 Contact

**Owner/Founder:** Rishabh — rishabh@eonixsystems.com  
**Instagram:** [@eonixsystems](https://www.instagram.com/eonixsystems/)  
**LinkedIn:** [Eonix Systems](https://www.linkedin.com/company/eonix-systems/)
