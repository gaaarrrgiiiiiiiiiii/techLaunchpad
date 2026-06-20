# Tech Launchpad 1.0 — MBA Partner Redesign

This repository contains the complete redesign of the offerings page for **MBA Partner**, developed for the Tech Launchpad 1.0 hackathon.

## 🎯 Project Overview
The objective was to transform the existing MBA Partner Wix website into a visually appealing, dynamic, and intuitive platform for students looking for placement preparation programs.

## ✨ Key Features
- **Modern EdTech Aesthetics:** Replaced strict "institutional" styling with a vibrant, playful palette featuring `Purple (#7A4BFF)` and `Yellow (#FDC742)`, paired with softer pill-shaped buttons, 24px border radii, and diffused shadows.
- **Dedicated Offering Pages:** Moved beyond a single crowded page by creating 5 unique detail pages for each core program:
  - All-In-One Combo
  - Placements Bootcamp
  - Live Projects
  - Case Competitions
  - Certifications
- **Interactive Modals:** Fully functional enrollment and lead-capture modals with auto-filled context based on the user's selected program.
- **Wix Compatibility:** The entire redesign was built using pure HTML, CSS (`shared.css`), and Vanilla JS, ensuring 100% compatibility for an easy HTML block integration within Wix.

## 🛠️ Tech Stack
- **HTML5:** Semantic and accessible structure.
- **CSS3:** Custom design system tokens via a central `shared.css` file.
- **JavaScript (Vanilla):** Dynamic modal states, smooth scrolling, and navigation interactions.
- **Typography:** Google Fonts (`Poppins` for modern dual-colored headings, `Inter` for highly legible body copy).

## 🚀 How to Run Locally
Since this is a static website, you can simply double-click `index.html` to open it in your browser. Alternatively, run a local Python server:
```bash
python -m http.server 9091
```
Then visit `http://localhost:9091` in your browser to view the site.
