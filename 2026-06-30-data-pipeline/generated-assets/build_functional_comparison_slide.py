from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_decision_recap import COLORS, draw_wrapped, font, header  # noqa: E402


def build():
    img = Image.new("RGBA", (1600, 900), COLORS["white"])
    header(img, 26, "Confronto funzionale")
    d = ImageDraw.Draw(img)
    d.text((80, 118), "Confronto funzionale per il requisito business", font=font(20, True), fill=COLORS["teal"])
    d.text((80, 151), "La scelta dipende anche dai prerequisiti di avvio, non solo dalle capability della dashboard", font=font(24), fill=COLORS["navy"])

    x0, y0 = 80, 215
    widths = [355, 430, 430]
    headers = ["CRITERIO", "AWS | METABASE", "QLIK | CLOUD + TALEND"]
    fills = [COLORS["light_gray"], COLORS["light_blue"], COLORS["light_teal"]]
    accents = [COLORS["gray"], COLORS["blue"], COLORS["green"]]
    x = x0
    for w, h, fill, acc in zip(widths, headers, fills, accents):
        d.rounded_rectangle((x, y0, x + w, y0 + 52), radius=12, fill=fill, outline=acc, width=2)
        d.text((x + 20, y0 + 15), h, font=font(17, True), fill=acc)
        x += w + 12

    rows = [
        ("Creare dashboard", "Sì, su dati già preparati", "Sì, self-service analytics"),
        ("Esplorare e visualizzare", "Query builder + visualizzazioni", "Esplorazione + analisi guidata"),
        ("Metriche governate", "Da predisporre con data modeling", "Da predisporre e verificare sul tenant"),
        ("Nuove fonti e regole", "Team data engineering", "Team Talend/Qlik o sviluppo dedicato"),
        ("File complessi / custom", "Flessibilità elevata", "Da benchmarkare su ProSIGNAL"),
        ("Prerequisito infrastrutturale", "Infra nostra/cliente: disponibilità e compatibilità", "Cliente: accettazione dei dati in cloud"),
        ("Componente di gestione", "Sì: infra, runtime, monitoraggio, backup e accessi", "Non per la piattaforma cloud; restano tenant, licenze e governance"),
        ("Skill prevalenti", "AWS, SQL/dbt, Python, BI", "Talend, Qlik, BI governance"),
    ]
    y = y0 + 64
    row_h = 45
    for i, (criterion, aws, qlik) in enumerate(rows):
        fill = COLORS["white"] if i % 2 == 0 else COLORS["light_gray"]
        x = x0
        for j, (w, value) in enumerate(zip(widths, [criterion, aws, qlik])):
            d.rectangle((x, y, x + w, y + row_h), fill=fill, outline=COLORS["line"], width=1)
            color = COLORS["navy"] if j == 0 else (COLORS["blue"] if j == 1 else COLORS["green"])
            draw_wrapped(d, (x + 17, y + 7), value, w - 34, size=14 if j else 15, color=color, bold=j == 0, line_gap=2, max_lines=2)
            x += w + 12
        y += row_h + 5

    d.rounded_rectangle((220, 700, 1380, 794), radius=13, fill=COLORS["light_green"], outline=COLORS["teal"], width=2)
    draw_wrapped(d, (250, 718), "Prerequisito decisionale: AWS richiede un'infrastruttura nostra o del cliente disponibile e compatibile; Qlik richiede l'accettazione del cliente di portare i dati in cloud.", 1100, size=19, color=COLORS["green"], bold=True, line_gap=4, max_lines=3)
    d.text((1040, 812), "Lettura comparativa da validare con il pilot", font=font(13), fill=COLORS["gray"])

    output = HERE.parent / "generated-assets/Slide recap 02 - confronto funzionale.png"
    img.convert("RGB").save(output, quality=95)
    print(output)


if __name__ == "__main__":
    build()
