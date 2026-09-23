# Design System Master File

> **LOGIC:** When building a specific page, first check `design-system/pages/[page-name].md`.
> If that file exists, its rules **override** this Master file.
> If not, strictly follow the rules below.

> **Source de vérité :** ce fichier est un scaffold généré par la skill
> `design-system` ; il a été corrigé le 2026-09-23 pour refléter la vraie
> identité AgriWin Togo (couleurs, typographie, style) au lieu de la palette
> indigo générique produite par défaut. Le design system canonique du projet,
> publié comme artefact claude.ai, reste **`brand/ds/project/`** — en cas de
> divergence entre les deux, c'est lui qui fait foi. Les tokens ci-dessous
> viennent de `site/css/style.css` (bloc `:root`) et de
> `brand/brandbook/tokens.json`, jamais inventés (règle du projet, voir
> `CLAUDE.md`).

---

**Project:** AgriWin Togo
**Generated:** 2026-09-23 14:54:38 (corrigé le 2026-09-23)
**Category:** Site vitrine agricole — conseil, formation, pépinière, marketplace, élevage (Kégué, Togo)
**Design Dials:** Variance 6/10 (Balanced / Modern) | Motion 4/10 (Standard) | Density 5/10 (Standard)

---

## Global Rules

### Color Palette

| Role | Hex | CSS Variable |
|------|-----|--------------|
| Primary (action) | `#2E7D32` | `--green-700` |
| On Primary | `#FFFFFF` | `--white` |
| Secondary (marque) | `#1B5E20` | `--green-900` |
| On Secondary | `#FFFFFF` | `--white` |
| Accent/CTA | `#E0A83D` | `--gold-500` |
| On Accent/CTA | `#0F3D17` | `--green-950` |
| Background | `#FFFFFF` | `--white` |
| Background (section alternée) | `#F7FAF5` | `--bg-soft` |
| Foreground | `#1A2417` | `--ink-900` |
| Card | `#FFFFFF` | `--white` |
| Card Foreground | `#364033` | `--ink-700` |
| Muted | `#F7FAF5` | `--bg-soft` |
| Muted Foreground | `#5C665A` | `--ink-500` |
| Border | `#E3EBE0` | `--border-soft` |
| Destructive | *non défini* | — |
| Ring (focus) | `#2E7D32` | `--green-700` |
| Service WhatsApp | `#25D366` | `--whatsapp` |

**Color Notes:** Vert agricole + or récolte. Aucune couleur destructive/erreur
n'existe dans la marque AgriWin à ce jour — à définir en respectant le seuil
WCAG AA (4.5:1) si un jour nécessaire, jamais improvisée. `--gold-600`
(#C98A2B, l'or décoratif du site) échoue le contraste sur fond clair
(2.94:1) : `--gold-700` (#9A6412) est le seul or autorisé pour du texte.

### Typography

- **Heading Font:** Poppins (500–800)
- **Body Font:** Inter (400–600)
- **Accent Font:** Playfair Display Italic — accroches et citations, usage rare
- **Mood:** agricole, professionnel, chaleureux, ancré dans le terroir, fiable
- **Google Fonts:** [Poppins + Inter + Playfair Display](https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600&family=Playfair+Display:ital@1&display=swap)

**CSS Import (identique à `site/index.html`) :**
```css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600&family=Playfair+Display:ital@1&display=swap');
```

### Spacing Variables

*Density: 5/10 — Standard. Le site utilise une échelle fluide (`clamp()`),
qui s'adapte à la largeur d'écran ; les valeurs ci-dessous sont les bornes
min/max de `site/css/style.css`.*

| Token | Value (clamp min–max) | Usage |
|-------|------------------------|-------|
| `--space-3xs` | `4px` – `6px` | Écarts très serrés |
| `--space-2xs` | `8px` – `12px` | Écarts d'icônes, espacement en ligne |
| `--space-xs` | `12px` – `16px` | Écarts serrés |
| `--space-sm` | `16px` – `22px` | Padding standard |
| `--space-md` | `24px` – `34px` | Padding de section |
| `--space-lg` | `36px` – `56px` | Grands écarts |
| `--space-xl` | `56px` – `88px` | Marges de section |
| `--space-2xl` | `80px` – `128px` | Padding de hero |

### Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | `8px` | Champs de formulaire, petites pastilles |
| `--radius-md` | `14px` | Cartes, images, blocs de contenu |
| `--radius-lg` | `22px` | Grands blocs, bandeaux, encarts CTA |
| `--radius-pill` | `999px` | Boutons et pastilles de surtitre |

### Shadow Depths

| Level | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 2px 10px rgba(15,61,23,.08)` | Repos des cartes et boutons |
| `--shadow-md` | `0 10px 30px rgba(15,61,23,.12)` | Survol des cartes et boutons |
| `--shadow-lg` | `0 20px 50px rgba(15,61,23,.18)` | Éléments flottants (menu mobile, FAB) |

*Pas de niveau `xl` dans la marque AgriWin — `--shadow-lg` est le maximum.*

---

## Component Specs

Les composants (boutons, cartes, champs, `ProductCard`, `ServiceCard`,
`CtaBand`, etc.) sont documentés et prévisualisables un par un dans
**[`brand/ds/project/components/`](../../brand/ds/project/components/)**
(un `README.md` + un `preview.html` par composant) — c'est la source de
vérité, pour ne pas maintenir deux versions divergentes du même CSS.
Extrait réel du bouton et de la carte (`site/css/style.css`), pour référence
rapide :

```css
/* Bouton — style de base commun */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2xs);
  font-family: var(--font-head);
  font-weight: 600;
  font-size: 15px;
  padding: 13px 26px;
  border-radius: var(--radius-pill);
  border: 2px solid transparent;
  transition: transform .15s ease, box-shadow .15s ease, background .2s ease, color .2s ease;
}
.btn:active { transform: scale(.97); }

/* Bouton principal (or, CTA) */
.btn-primary { background: var(--gold-500); color: var(--green-950); box-shadow: var(--shadow-sm); }
.btn-primary:hover { background: var(--gold-400); box-shadow: var(--shadow-md); }

/* Bouton secondaire (vert plein) */
.btn-green { background: var(--green-700); color: var(--white); box-shadow: var(--shadow-sm); }
.btn-green:hover { background: var(--green-600); box-shadow: var(--shadow-md); }
```

```css
/* Carte */
.card {
  background: var(--white);
  border: 1px solid var(--border-soft);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: transform .2s ease, box-shadow .2s ease;
}
.card:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); }
```

Pour les champs de formulaire, les modales ou tout composant absent de
`brand/ds/project/components/`, suivre les mêmes tokens (couleurs, radius,
ombres, espacements ci-dessus) plutôt qu'improviser des valeurs.

---

## Style Guidelines

**Style:** Agricole moderne & chaleureux

**Keywords:** Naturel, humain, professionnel, terrain, artisanal-pro, lumineux,
photographie de terrain, dégradés verts/or discrets

**Best For:** Conseil et formation agricole, pépinières, marketplace de
produits agricoles, élevage, PME et coopératives rurales

**Key Effects (redesign `ce2c154`) :** espacements et typographie fluides
(`clamp()`), boutons avec balayage lumineux et léger lift au survol, cartes
à bordure dégradée et ombres teintées vert/or, en-tête qui se durcit au
scroll, révélation en cascade des sections via `IntersectionObserver`,
respect strict de `prefers-reduced-motion`

### Page Pattern

**Pattern Name:** Site vitrine multi-pages (pas un funnel de conversion)

- **Structure réelle :** Accueil → Nos Services → Marketplace → Nos
  Réalisations → Parlons projet (contact), + À propos en pied de page
- **Conversion Strategy:** Appels à l'action multiples et directs (Appeler,
  WhatsApp) présents dans l'en-tête et le pied de page de chaque page,
  plutôt qu'un tunnel en étapes
- **CTA Placement:** En-tête (fixe), bande CTA en fin de page, FAB WhatsApp

---

## Motion

Le site est du **HTML/CSS/JS pur, sans dépendance** (règle du projet — voir
`CLAUDE.md`) : **pas de GSAP ni d'autre librairie d'animation.** Les
animations réelles vivent dans `site/js/enhancements.js`, en JavaScript
natif :

```js
// Révélation en cascade au scroll (IntersectionObserver natif, sans lib)
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) entry.target.classList.add('is-visible');
  });
}, { threshold: 0.15 });

document.querySelectorAll('[data-reveal]').forEach((el) => observer.observe(el));
```

**Notes réelles du projet :** effet magnétique subtil sur les boutons
primaires (desktop uniquement) ; verrouillage du scroll quand le menu
mobile est ouvert ; tout se désactive proprement si
`prefers-reduced-motion: reduce` est actif ou si `IntersectionObserver`
n'est pas disponible.

- ✅ Garder les transitions courtes (150–300ms) et les easings déjà définis
  (`--ease-out`, `--ease-in-out`, `--ease-back` dans `site/css/style.css`)
- ❌ Ne pas introduire de dépendance JS (GSAP, animation libs) pour un site
  qui n'en a aucune — ce serait un changement de nature du projet, pas un
  correctif de style
- ⚡ Respecter `prefers-reduced-motion` sur toute nouvelle animation

---

## Anti-Patterns (Do NOT Use)

- ❌ No preview
- ❌ Slow delivery

### Additional Forbidden Patterns

- ❌ **Emojis as icons** — Use SVG icons (le site utilise déjà des SVG inline cohérents)
- ❌ **Missing cursor:pointer** — All clickable elements must have cursor:pointer
- ❌ **Layout-shifting hovers** — Avoid scale transforms that shift layout
- ❌ **Low contrast text** — Maintain 4.5:1 minimum contrast ratio (mesuré, pas jugé à l'œil — voir `brand/brandbook/tokens.json`)
- ❌ **Instant state changes** — Always use transitions (150-300ms)
- ❌ **Invisible focus states** — Focus states must be visible for a11y
- ❌ **Couleur inventée** — toute couleur doit venir de `site/css/style.css`, jamais improvisée (règle du projet)

---

## Pre-Delivery Checklist

Before delivering any UI code, verify:

- [ ] No emojis used as icons (use SVG instead)
- [ ] All icons from consistent icon set (SVG inline, cohérent avec le site)
- [ ] `cursor-pointer` on all clickable elements
- [ ] Hover states with smooth transitions (150-300ms)
- [ ] Light mode: text contrast 4.5:1 minimum (mesuré)
- [ ] Focus states visible for keyboard navigation
- [ ] `prefers-reduced-motion` respected
- [ ] Responsive: 375px, 768px, 1024px, 1440px
- [ ] No content hidden behind fixed navbars
- [ ] No horizontal scroll on mobile
- [ ] Aucune nouvelle dépendance JS/CSS ajoutée au site
