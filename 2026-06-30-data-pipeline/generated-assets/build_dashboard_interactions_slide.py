from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_decision_recap import COLORS, draw_wrapped, font, header  # noqa: E402


def build():
    img = Image.new("RGBA", (1600, 900), COLORS["white"])
    header(img, 27, "Dashboard interattive")
    d = ImageDraw.Draw(img)

    d.text(
        (80, 118),
        "Confronto delle capability di navigazione e analisi",
        font=font(20, True),
        fill=COLORS["teal"],
    )
    d.text(
        (80, 151),
        "Entrambe supportano dashboard interattive e navigabili, ma con un modello diverso.",
        font=font(24),
        fill=COLORS["navy"],
    )

    x0, y0 = 80, 211
    widths = [300, 485, 485]
    headers = ["CAPABILITY", "METABASE", "QLIK"]
    fills = [COLORS["light_gray"], COLORS["light_blue"], COLORS["light_teal"]]
    accents = [COLORS["gray"], COLORS["blue"], COLORS["green"]]

    x = x0
    for width, title, fill, accent in zip(widths, headers, fills, accents):
        d.rounded_rectangle(
            (x, y0, x + width, y0 + 54),
            radius=12,
            fill=fill,
            outline=accent,
            width=2,
        )
        d.text((x + 20, y0 + 16), title, font=font(17, True), fill=accent)
        x += width + 15

    rows = [
        (
            "Navigazione tra dashboard / schede",
            "Sì, con link configurati su card e visualizzazioni verso altre dashboard, domande o URL.",
            "Sì, nativamente tra sheet, gruppi di sheet e app; anche con menu, pulsanti e API.",
        ),
        (
            "Click su un grafico per filtrare",
            "Sì, il cross-filtering aggiorna le card collegate.",
            "Sì, le selezioni aggiornano le visualizzazioni correlate grazie al modello associativo.",
        ),
        (
            "Drill-through verso il dettaglio",
            "Sì, dai grafici del query builder verso dettaglio, domanda, dashboard o URL.",
            "Sì, con sheet, azioni, link e selezioni; la navigazione va predisposta.",
        ),
        (
            "Drill-down gerarchico",
            "Possibile con filtri, drill-through e dashboard collegate.",
            "Più nativo, con dimensioni e gruppi gerarchici e livelli di analisi.",
        ),
        (
            "Filtri dipendenti",
            "Sì, con linked filters e filtri collegati alle card.",
            "Sì, tramite modello associativo e selezioni tra dimensioni.",
        ),
        (
            "Bookmark / stato di analisi",
            "Parzialmente: filtri e parametri si conservano nei link o nella configurazione.",
            "Sì, i bookmark salvano e ripristinano selezioni e stato di analisi.",
        ),
        (
            "Azioni operative",
            "Sì, con azioni su dashboard, link e destinazioni personalizzate.",
            "Sì, con pulsanti, azioni, automazioni e API; più flessibile per scenari avanzati.",
        ),
        (
            "Insight automatici",
            "Esplorazione e query guidata.",
            "Insight Advisor e analisi assistita integrati nella piattaforma analytics.",
        ),
    ]

    y = y0 + 66
    row_h = 62
    for index, (capability, metabase, qlik) in enumerate(rows):
        fill = COLORS["white"] if index % 2 == 0 else COLORS["light_gray"]
        x = x0
        values = [capability, metabase, qlik]
        for column, (width, value) in enumerate(zip(widths, values)):
            d.rectangle(
                (x, y, x + width, y + row_h),
                fill=fill,
                outline=COLORS["line"],
                width=1,
            )
            color = COLORS["navy"] if column == 0 else (COLORS["blue"] if column == 1 else COLORS["green"])
            draw_wrapped(
                d,
                (x + 17, y + 9),
                value,
                width - 34,
                size=14 if column == 0 else 13,
                color=color,
                bold=column == 0,
                line_gap=3,
                max_lines=3,
            )
            x += width + 15
        y += row_h + 4

    d.rounded_rectangle(
        (220, 824, 1380, 855),
        radius=10,
        fill=COLORS["light_green"],
        outline=COLORS["teal"],
        width=1,
    )
    d.text(
        (245, 831),
        "Lettura executive: entrambe sono navigabili; Qlik è più nativo su gerarchie, bookmark e analisi assistita.",
        font=font(15, True),
        fill=COLORS["green"],
    )

    output = HERE / "Slide recap 05 - dashboard interattive metabase qlik.png"
    img.convert("RGB").save(output, quality=95)
    print(output)


if __name__ == "__main__":
    build()
