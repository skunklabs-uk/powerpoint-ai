# Image Final v1.0 Manifest

## Output

- Final PDF: `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Image Final v1.0.pdf`
- Source HTML: `sources/data-pipeline-image-final-v1.html`
- Technical render: `previews/source-render-v1.pdf`
- Contact sheet: `previews/image-final-v1-contact.png`
- Slide images: `slides/slide-01.png` ... `slides/slide-20.png`

## Input PDF

Primary source:

- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Explained v0.8.pdf`

Context sources:

- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Explained v0.7.pdf`
- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Template Faithful v0.6.pdf`
- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Template Faithful v0.5.pdf`
- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Visual Draft v0.4.pdf`
- `2026-06-30-data-pipeline/attempts/2026_TXT_001 - Data Pipeline Blueprint - Scenari TO BE v0.3.pdf`

## Visual References

- `docs/template.pdf`
- `docs/template2.pdf`
- `docs/ui/bernadelli-01-copertina-proposta-infrastruttura-server.png`
- `docs/ui/bernadelli-02-contesto-esigenza-obiettivi.png`
- `docs/ui/bernadelli-06-scenario-on-premise-alta-affidabilita.png`
- `docs/ui/bernadelli-07-scenario-cloud-distribuito.png`
- `docs/ui/bernadelli-08-confronto-soluzioni.png`
- `docs/ui/bernadelli-10-costi-simulazione-lungo-periodo.png`
- `docs/ui/bernadelli-11-chiusura-contatti.png`

## Reused Assets

- `../novigo-header-logo-template.png`
- `../template-cover-wave.png`
- `../txt-star-mark-template.png`

The icons used inside the deck are CSS/SVG-like outline treatments built in the HTML source. No external icon package or downloaded image asset was introduced.

## Build Notes

The final PDF is intentionally image-based:

1. HTML source rendered to `previews/source-render-v1.pdf`.
2. PDF pages rasterized to PNG at 160 dpi.
3. PNG slides recomposed into the final PDF with `img2pdf`.

Slide images are 2560 x 1440 pixels, matching a 16:9 layout.

## WBS Revision Notes

Slides 13-16 implement the Gianfranco guideline:

- WBS blueprint first, with common process catalogue and reusable functions.
- Three project WBS slides after the blueprint: ING ProSIGNAL, Kiron CDG, CDG interno.
- First level is always process; second level is always function.
- Common processes are preserved across the three project WBS views.
- Non-applicable common/optional processes remain visible in grey with `N/A`.

## Known Trade-Off

The final PDF has no selectable text because it is built from images. This is intentional for the requested image-based workflow. The HTML source remains available for reconstruction or future edits.
