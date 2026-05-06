# Marketing Portfolio — Cristine Cabugao

Single-page portfolio site for Cristine Cabugao (Social Media Manager &amp; Content Strategist).

## Stack
- Static HTML + Tailwind (CDN) + vanilla JS — no build step.
- Fonts: Space Grotesk (display/headlines), Inter (body), Material Symbols (icons).
- Design source: Stitch project "Liquid Glass Cinematic Portfolio" (`projects/15101050954201332242`).

## Run locally
Open `index.html` in a browser, or:

```
python -m http.server 8080
```

then visit `http://localhost:8080`.

## Structure
```
index.html
assets/
  freshnest/        # FreshNest Cleaning brand samples (1-6.png)
  sparkle-clean/    # Sparkle Clean Co. brand samples (1-6.png)
  maid-with-love/   # Maid With Love brand samples (1-2.png)
```

## Design system — Liquid Glass (dark glassmorphism)

| Token | Value |
|---|---|
| `background` / `surface` | `#051424` (deep midnight) |
| `surface-container-lowest` | `#010f1f` |
| `primary` | `#c0c6de` |
| `secondary` (electric violet) | `#d2bbff` |
| `secondary-container` (button bg) | `#6001d1` |
| `tertiary` (cyan) | `#4cd7f6` |
| `on-surface` | `#d4e4fa` |

Glass cards: `rgba(255,255,255,0.03)` background + `backdrop-filter: blur(30px)` + 1px white/10 border. Hover scales to 1.02× with deeper blur.

## Sections
1. Hero — headline + gradient accent, 3 stats
2. Strategy Meets Story — 3 value props (glass cards)
3. Featured Work — 4 case studies (FreshNest, Sparkle Clean, Synergy/SDI, Maid With Love)
4. My Expertise — 6 services in expandable list pattern
5. Testimonials — 3 client quotes
6. Contact — inquiry form (glass card)
7. Footer
