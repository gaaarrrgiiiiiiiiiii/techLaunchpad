# Tech Launchpad 1.0 — MBA Partner Offerings Redesign

> **Round 2 Submission** · Tech Launchpad 1.0 Hackathon

A complete redesign of the MBA Partner website's offerings section — transforming a generic Wix site into a visually compelling, fully interactive, and Wix-compatible experience for MBA placement aspirants.

---

## 🎯 Project Overview

The challenge was to redesign the MBA Partner offerings page to be more **dynamic**, **student-friendly**, and **clearly informative** — going well beyond a bare Figma design to deliver a fully functional, end-to-end implementation.

---

## 📄 Pages

| Page | File | Description |
|------|------|-------------|
| Main Offerings Hub | `index.html` | Landing page showcasing all 5 programs with interactive CTAs |
| All-In-One Combo | `offering-all-in-one.html` | Full-stack placement prep bundle detail page |
| Placements Bootcamp | `offering-bootcamp.html` | Domain-specific interview prep program page |
| Live Projects | `offering-live-project.html` | Real client project experience detail page |
| Case Competitions | `offering-case-comp.html` | Structured case-solving prep program page |
| Certifications | `offering-certifications.html` | Technical certification programs page |

---

## ✨ Key Features

- **End-to-End Offering Pages** — Each of the 5 programs has its own fully detailed page covering curriculum, outcomes, pricing, FAQs, and enrollment
- **Functional Interactivity** — All CTAs trigger working modals; "Choose Combo" opens an enrollment popup, "More Info" reveals detailed program highlights
- **Modern EdTech Design System** — Vibrant purple (`#7A4BFF`) + yellow (`#FDC742`) palette, pill-shaped buttons, 24px card radii, diffused shadows, and smooth micro-animations
- **Dual-Colour Headings** — Section headings split into navy + purple to create visual hierarchy and brand consistency
- **Wix-Ready** — Built purely in HTML5 + CSS3 + Vanilla JS with no external dependencies, making it trivially embeddable as an HTML block inside Wix

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Structure | HTML5 (semantic) |
| Styling | CSS3 — single shared design system (`shared.css`) |
| Interactivity | Vanilla JavaScript (no frameworks) |
| Typography | Google Fonts — `Poppins` + `Inter` |
| Deployment | Static hosting / Wix HTML embed |

---

## 🚀 Running Locally

This is a **zero-dependency static website**. No build step or `npm install` needed.

**Option 1 — Double click:**
Open `index.html` directly in any modern browser.

**Option 2 — Local server (recommended for accurate routing):**
```bash
python -m http.server 9091
```
Then visit **[http://localhost:9091](http://localhost:9091)**

---

## 🗂️ File Structure

```
techLaunchpad/
├── index.html                  # Main offerings hub
├── offering-all-in-one.html    # All-In-One Combo detail page
├── offering-bootcamp.html      # Placements Bootcamp detail page
├── offering-live-project.html  # Live Projects detail page
├── offering-case-comp.html     # Case Competitions detail page
├── offering-certifications.html# Certifications detail page
├── shared.css                  # Shared design system (tokens, components)
└── README.md
```

---

## 🔗 Wix Integration

Since Wix supports embedding custom HTML via its **HTML iFrame / Embed** widget, each page can be dropped in directly. The shared design system in `shared.css` is inlined or referenced internally, ensuring no external file dependencies are required inside the Wix environment.
