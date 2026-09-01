# Design Prism

A curated gallery of **40 modern AI company websites** with clean, minimalist design — categorized by design system, with homepage previews and structured metadata.

Inspired by the editorial warmth of [Applied Compute](https://appliedcompute.com) and the institutional rigor of [Hebbia](https://hebbia.com).

## Quick start

```bash
python3 -m http.server 8765
# open http://localhost:8765/ai-design-showcase.html
```

## What's included

| File | Purpose |
|------|---------|
| `ai-design-showcase.html` | Self-contained gallery UI |
| `ai-showcase-sites.json` | 40 sites + 6-category design system taxonomy |
| `ai-showcase-screenshots/` | Homepage preview images (Playwright-captured) |
| `capture_showcase_screenshots.py` | Regenerate screenshots |

## Design system taxonomy

| System | Description |
|--------|-------------|
| **Editorial Warm** | Serif on cream, single confident accent |
| **Monochrome Restraint** | B&W, typography-led |
| **Enterprise Light** | Clean sans, product UI screenshots |
| **Dark Technical** | Dark mode, mono accents, developer-focused |
| **Dark Premium** | Dark with cinematic/luxury gravitas |
| **Utility Minimal** | Product interface is the homepage |

## Regenerate screenshots

```bash
pip install playwright
python3 -m playwright install chromium
python3 capture_showcase_screenshots.py
```

## License

Curated for design inspiration — not affiliated with any listed company.
