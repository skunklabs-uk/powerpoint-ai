from __future__ import annotations

from pathlib import Path
import sys

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_decision_recap import COLORS, card, draw_wrapped, font, save_slide  # noqa: E402


def slide3(img):
    d = ImageDraw.Draw(img)
    d.text((80, 118), "Piano indicativo | Pilot decisionale", font=font(20, True), fill=COLORS["teal"])
    d.text((80, 151), "In circa due mesi verifichiamo il valore per gli utenti, la fattibilità e la soluzione da scegliere", font=font(23), fill=COLORS["navy"])

    x_left, x0, x_end = 175, 390, 1490
    axis_y, months = 202, 2
    step = (x_end - x0) / months

    def period_x(value):
        return int(x0 + step * value)

    def vertical_label(label, y1, y2):
        fnt = font(13, True)
        bbox = fnt.getbbox(label)
        tile = Image.new("RGBA", (bbox[2] - bbox[0] + 6, bbox[3] - bbox[1] + 6), (0, 0, 0, 0))
        td = ImageDraw.Draw(tile)
        td.text((3 - bbox[0], 3 - bbox[1]), label, font=fnt, fill=COLORS["navy"])
        tile = tile.rotate(90, expand=True)
        img.alpha_composite(tile, (int(120 - tile.width / 2), int((y1 + y2 - tile.height) / 2)))

    def draw_section(y1, y2, label):
        d.rounded_rectangle((80, y1, 160, y2), radius=8, fill=COLORS["blue"], outline=COLORS["cyan"], width=2)
        d.rounded_rectangle((95, y1 + 7, 150, y2 - 7), radius=8, fill=COLORS["white"])
        vertical_label(label, y1 + 7, y2 - 7)

    def draw_bar(start, solid_end, range_end, y, color):
        bar_h = 22
        sx, ex, rx = period_x(start), period_x(solid_end), period_x(range_end)
        d.rounded_rectangle((sx, y, ex, y + bar_h), radius=5, fill=color, outline=color, width=2)
        if rx > ex:
            d.rectangle((ex, y, rx, y + bar_h), fill=COLORS["white"], outline=color, width=2)
            for hatch_x in range(max(ex - bar_h, sx), rx, 8):
                d.line((hatch_x, y + bar_h - 1, min(hatch_x + bar_h, rx), y + 1), fill=color, width=1)
        d.polygon([(rx, y + bar_h // 2), (rx + 9, y + bar_h // 2 - 8), (rx + 9, y + bar_h // 2 + 8)], fill=color)

    def draw_row(y, label, color, bar):
        d.rectangle((x_left, y - 7, x_end + 12, y + 31), fill=COLORS["white"], outline=COLORS["line"], width=1)
        draw_wrapped(d, (x_left + 10, y - 2), label, x0 - x_left - 24, size=13, color=COLORS["navy"], bold=True, line_gap=1, max_lines=2)
        draw_bar(*bar, y, color)

    # Monthly axis: the detailed weekly ranges remain in the scenario cards below.
    d.line((x0 - 14, axis_y, x_end + 28, axis_y), fill=COLORS["navy"], width=1)
    for index in range(months + 1):
        x = period_x(index)
        d.ellipse((x - 10, axis_y - 10, x + 10, axis_y + 10), fill=COLORS["blue"])
        for grid_y in range(axis_y + 14, 700, 8):
            d.line((x, grid_y, x, min(grid_y + 3, 700)), fill=COLORS["line"], width=1)
        if index < months:
            label = f"MESE {index + 1}"
            tw = d.textlength(label, font=font(15, True))
            d.text((x + step / 2 - tw / 2, 168), label, font=font(15, True), fill=COLORS["gray"])
    d.polygon([(x_end + 28, axis_y), (x_end + 16, axis_y - 6), (x_end + 16, axis_y + 6)], fill=COLORS["blue"])

    draw_section(245, 365, "ANALISI")
    draw_section(370, 535, "REALIZZAZIONE")
    draw_section(540, 700, "TEST")

    draw_row(270, "Obiettivi e dashboard da verificare", COLORS["teal"], (0.0, 0.25, 0.45))
    draw_row(320, "Accessi, fonti e condizioni di partenza", COLORS["gray"], (0.0, 0.35, 0.65))

    draw_row(402, "AWS + Metabase | preparare dati e dashboard", COLORS["blue"], (0.25, 0.95, 1.30))
    draw_row(452, "Qlik Cloud | preparare dati e dashboard", COLORS["green"], (0.25, 0.75, 1.05))

    draw_row(572, "AWS + Metabase | prova con utenti e decisione", COLORS["blue"], (0.90, 1.20, 1.55))
    draw_row(622, "Qlik Cloud | prova con utenti e decisione", COLORS["green"], (0.70, 0.95, 1.30))

    d.rounded_rectangle((175, 720, 815, 780), radius=12, fill=COLORS["light_blue"], outline=COLORS["blue"], width=2)
    d.text((198, 733), "AWS + Metabase", font=font(15, True), fill=COLORS["blue"])
    d.text((198, 756), "3–5 sett. pronto  |  5–7 sett. da zero", font=font(16, True), fill=COLORS["navy"])
    d.rounded_rectangle((850, 720, 1490, 780), radius=12, fill=COLORS["light_teal"], outline=COLORS["green"], width=2)
    d.text((873, 733), "Qlik Cloud", font=font(15, True), fill=COLORS["green"])
    d.text((873, 756), "2–4 sett. pronto  |  4–6 sett. attivazioni", font=font(16, True), fill=COLORS["navy"])

    d.rounded_rectangle((175, 792, 1490, 827), radius=10, fill=COLORS["light_green"], outline=COLORS["teal"], width=2)
    d.text((198, 801), "Perimetro: 1 caso d’uso, 1–2 fonti, 2–3 dashboard, dati campione; nessuna preparazione completa per la messa in produzione.", font=font(14, True), fill=COLORS["green"])
    d.text((175, 840), "Scala mensile relativa. Stime indicative da validare; non costituiscono commitment.", font=font(12), fill=COLORS["gray"])


def slide4(img):
    d = ImageDraw.Draw(img)
    d.text((80, 118), "Economics | Budget frame primo anno", font=font(20, True), fill=COLORS["teal"])
    d.text((80, 151), "Per il POC interno si valorizzano solo cloud e subscription; effort interno escluso", font=font(24), fill=COLORS["navy"])
    card(
        d,
        (90, 235, 750, 720),
        "AWS | Stack componibile",
        "Costi diretti: €5k cloud/runtime.",
        COLORS["blue"],
        COLORS["light_blue"],
        bullets=[
            "Effort e run del team interno esclusi dal budget.",
            "Sizing: 2 EC2, 1 RDS, 1 TB S3 medio e lifecycle.",
            "Driver: fonti, volumi, retention, frequenza run e sizing.",
        ],
    )
    card(
        d,
        (850, 235, 1510, 720),
        "Qlik | Cloud + Talend",
        "Costi diretti: €30k subscription.",
        COLORS["green"],
        COLORS["light_teal"],
        bullets=[
            "Effort e run del team interno esclusi dal budget.",
            "Subscription base: 50 GB per 12 mesi.",
            "Driver: utenti, capacity, add-on, runtime e storage.",
        ],
    )
    d.rounded_rectangle((185, 754, 1415, 825), radius=13, fill=COLORS["light_green"], outline=COLORS["teal"], width=2)
    draw_wrapped(d, (220, 772), "Budget costi diretti POC: AWS €5k | Qlik €30k.", 1280, size=21, color=COLORS["green"], bold=True, line_gap=4, max_lines=2)
    d.text((90, 838), "Nota: importi limitati a cloud/runtime e subscription; effort e supporto interno non sono valorizzati.", font=font(13), fill=COLORS["gray"])


def build():
    save_slide("Slide recap 03 - tempi pilot.png", "Tempi per il primo pilot", 27, slide3)
    save_slide("Slide recap 04 - economics.png", "Economics", 28, slide4)


if __name__ == "__main__":
    build()
