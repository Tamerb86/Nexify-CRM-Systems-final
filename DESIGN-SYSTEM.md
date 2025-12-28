# Nexify CRM Systems - Design System & Project Guide

## 📋 Project Overview

**Company:** Nexify CRM Systems AS  
**Style:** Light – Corporate – Clean – Modern  
**Technology:** Astro SSG + Tailwind CSS 4  
**Languages:** Norwegian (NO), English (EN), Arabic (AR)

---

## 🎨 Brand Identity

### Color Palette

| Color | Value | Usage |
|-------|-------|-------|
| **Primary Blue** | `#0A1B55` | Headers, buttons, text |
| **Primary Light** | Lighter shade | Hover states |
| **Primary Dark** | Darker shade | Active states |
| **Teal Green** | `#00C6A3` | Accents, CTAs, highlights |
| **Secondary Light** | Lighter teal | Backgrounds |
| **Secondary Dark** | Darker teal | Hover states |
| **Gray 50-900** | Neutral scale | Text, borders, backgrounds |

### Typography

**Font Family:** Work Sans (Google Fonts)  
**Weights:** 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold)

| Element | Size | Weight |
|---------|------|--------|
| H1 | 3rem (48px) | 700 |
| H2 | 2.25rem (36px) | 600 |
| H3 | 1.875rem (30px) | 600 |
| H4 | 1.5rem (24px) | 600 |
| Body | 1rem (16px) | 400 |
| Small | 0.875rem (14px) | 400 |

---

## 🧩 Component Classes

### Buttons

```html
<!-- Primary Button -->
<button class="btn btn-primary">Click me</button>

<!-- Secondary Button -->
<button class="btn btn-secondary">Click me</button>

<!-- Outline Button -->
<button class="btn btn-outline">Click me</button>

<!-- Large Button -->
<button class="btn btn-primary btn-lg">Large Button</button>

<!-- Small Button -->
<button class="btn btn-primary btn-sm">Small Button</button>
```

### Cards

```html
<!-- Standard Card -->
<div class="card">
  <h3>Card Title</h3>
  <p>Card content goes here</p>
</div>
```

### Sections

```html
<!-- Standard Section -->
<section class="section">
  <div class="container">
    <h2 class="section-title">Section Title</h2>
    <p class="section-subtitle">Section description</p>
    <!-- Content -->
  </div>
</section>
```

### Badges

```html
<span class="badge">New</span>
```

### Inputs

```html
<input type="text" class="input" placeholder="Enter text..." />
```

---

## 📁 File Structure

```
nexify-site/
├── public/
│   ├── images/           # Static images
│   ├── favicon.svg       # Favicon
│   └── ...
├── src/
│   ├── components/       # Reusable components
│   │   ├── Header.astro
│   │   └── Footer.astro
│   ├── layouts/          # Page layouts
│   │   └── Layout.astro
│   ├── lib/              # Utilities
│   │   └── i18n.ts       # Translation helper
│   ├── pages/            # Route pages
│   │   ├── index.astro   # Home
│   │   ├── services.astro
│   │   ├── projects.astro
│   │   ├── pricing.astro
│   │   ├── about.astro
│   │   ├── contact.astro
│   │   ├── blog.astro
│   │   ├── privacy.astro
│   │   └── terms.astro
│   ├── sections/         # Page sections (to be added)
│   ├── styles/
│   │   └── global.css    # Design system
│   └── translations/     # i18n files
│       ├── no.json
│       ├── en.json
│       └── ar.json
└── astro.config.mjs
```

---

## 🌐 Page Structure

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Landing page with hero, services, CTA |
| Services | `/services` | Service offerings |
| Projects | `/projects` | Portfolio showcase |
| Pricing | `/pricing` | Pricing plans |
| About | `/about` | Company info |
| Contact | `/contact` | Contact form |
| Blog | `/blog` | Articles |
| Privacy | `/privacy` | Privacy policy |
| Terms | `/terms` | Terms & conditions |

---

## 🔤 Translation System

### Usage

```astro
---
import { t } from '../lib/i18n';
const lang = 'no'; // or 'en', 'ar'
---

<h1>{t(lang, 'hero.title')}</h1>
```

### Adding Translations

Edit files in `src/translations/`:
- `no.json` - Norwegian
- `en.json` - English  
- `ar.json` - Arabic (RTL supported)

---

## 🎯 Design Principles

1. **Clean & Professional** - Minimal clutter, clear hierarchy
2. **Consistent Spacing** - Use design system spacing values
3. **Soft Shadows** - Subtle depth without harsh edges
4. **Responsive First** - Mobile-friendly by default
5. **Accessible** - Focus states, contrast ratios
6. **Fast Loading** - Static HTML, optimized assets

---

## 📐 Layout Guidelines

- **Max Width:** 1200px
- **Container Padding:** 1.5rem (24px)
- **Section Padding:** 5rem (80px) vertical
- **Card Padding:** 1.5rem (24px)
- **Border Radius:** 0.5rem (8px) default, 0.75rem (12px) for cards

---

## 🚀 Commands

```bash
# Development
pnpm dev

# Build
pnpm build

# Preview build
pnpm preview
```

---

## 📝 Next Steps

1. **Expand Home Page** - Add full hero, features, testimonials
2. **Build Services Page** - Detailed service cards
3. **Create Projects Page** - Portfolio grid
4. **Design Pricing Page** - Pricing tables
5. **Add Contact Form** - Form with validation
6. **Write Blog Posts** - Content pages
7. **Add Language Routes** - `/en/`, `/ar/` prefixes
