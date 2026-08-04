from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated-assets"
SHOWCASE = OUT / "dashboard-showcase"
LOGO = OUT / "novigo-header-logo-template.png"
STAR = OUT / "txt-star-mark-template.png"

FONT_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
FONT_SEMI = "/usr/share/fonts/truetype/noto/NotoSans-SemiBold.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"

COLORS = {
    "navy": "#25333D",
    "blue": "#2474C5",
    "cyan": "#2AA7C0",
    "teal": "#49AE8D",
    "green": "#07914D",
    "light_blue": "#EDF7FC",
    "light_teal": "#EEF9F6",
    "light_green": "#EEF8EE",
    "line": "#D5E1E5",
    "gray": "#6E7C85",
    "white": "#FFFFFF",
    "black": "#20262B",
}


def font(size: int, bold: bool = False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def draw_wrapped(draw, xy, text, width, size=20, color=None, bold=False, line_gap=5, max_lines=None):
    color = color or COLORS["black"]
    fnt = font(size, bold)
    lines = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if draw.textlength(candidate, font=fnt) <= width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(".,;:") + "…"
    draw.multiline_text(xy, "\n".join(lines), font=fnt, fill=color, spacing=line_gap)
    return len(lines) * (size + line_gap)


def draw_url(draw, xy, url, width, size=9, color=None):
    color = color or COLORS["blue"]
    fnt = font(size)
    lines = []
    current = ""
    for char in url:
        candidate = current + char
        if draw.textlength(candidate, font=fnt) <= width or not current:
            current = candidate
        else:
            lines.append(current)
            current = char
    if current:
        lines.append(current)
    draw.multiline_text(xy, "\n".join(lines), font=fnt, fill=color, spacing=1)
    return len(lines) * (size + 1)


def header(img, page, title):
    d = ImageDraw.Draw(img)
    logo = Image.open(LOGO).convert("RGBA")
    logo.thumbnail((155, 42))
    img.alpha_composite(logo, (17, 15))
    d.rectangle((0, 82, 185, 88), fill=COLORS["cyan"])
    d.text((220, 20), "Data pipeline |", font=font(30, True), fill="#A4A9AD")
    d.text((438, 20), title, font=font(30, True), fill=COLORS["black"])
    nav = ["PERCHÉ", "VALORE", "PROPOSTA", "PIANO", "DECISIONE"]
    x = 1060
    for item in nav:
        active = item == "DECISIONE"
        col = COLORS["teal"] if active else COLORS["blue"]
        d.text((x, 20), item, font=font(12), fill=col)
        d.ellipse((x + 4, 43, x + 20, 59), fill=col if active else "#A9AFB2")
        d.line((x + 20, 51, x + 73, 51), fill=COLORS["teal"], width=1)
        x += 88
    d.text((1555, 18), str(page), font=font(16), fill=COLORS["black"])
    d.rectangle((0, 865, 1600, 900), fill=COLORS["white"])
    foot = Image.open(LOGO).convert("RGBA")
    foot.thumbnail((125, 29))
    img.alpha_composite(foot, (17, 868))
    star = Image.open(STAR).convert("RGBA")
    star.thumbnail((42, 42))
    img.alpha_composite(star, (1535, 850))


def rounded_image(img: Image.Image, box, radius=10, background="#FFFFFF"):
    x1, y1, x2, y2 = box
    width, height = x2 - x1, y2 - y1
    fitted = ImageOps.contain(img.convert("RGB"), (width - 8, height - 8), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (width, height), background)
    canvas.paste(fitted, ((width - fitted.width) // 2, (height - fitted.height) // 2))
    mask = Image.new("L", (width, height), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, width - 1, height - 1), radius=radius, fill=255)
    return canvas, mask


def showcase_card(d, img, box, title, body, accent, fill, examples, secondary_link=None):
    x1, y1, x2, y2 = box
    d.rounded_rectangle(box, radius=16, fill=fill, outline=accent, width=2)
    d.line((x1, y1, x2, y1), fill=accent, width=7)
    d.text((x1 + 24, y1 + 20), title, font=font(25, True), fill=accent)
    d.rounded_rectangle((x1 + 24, y1 + 61, x2 - 24, y1 + 94), radius=16, fill=accent)
    badge = "UTILIZZABILE"
    tw = d.textlength(badge, font=font(14, True))
    d.text(((x1 + x2 - tw) / 2, y1 + 69), badge, font=font(14, True), fill=COLORS["white"])
    draw_wrapped(d, (x1 + 24, y1 + 111), body, x2 - x1 - 48, size=17, color=COLORS["black"], line_gap=3, max_lines=2)
    d.text((x1 + 24, y1 + 164), "PREVIEW DI DASHBOARD", font=font(13, True), fill=COLORS["gray"])

    left = x1 + 24
    top = y1 + 190
    gap = 14
    thumb_w = x2 - x1 - 48 if len(examples) == 1 else (x2 - x1 - 48 - gap) // 2
    thumb_h = 215 if len(examples) == 1 and secondary_link else (250 if len(examples) == 1 else 196)
    for i, (path, label, image_url, page_url) in enumerate(examples):
        tx = left + i * (thumb_w + gap)
        source = Image.open(path)
        preview, mask = rounded_image(source, (tx, top, tx + thumb_w, top + thumb_h))
        img.paste(preview, (tx, top), mask)
        d.rounded_rectangle((tx, top, tx + thumb_w, top + thumb_h), radius=10, outline=COLORS["line"], width=2)
        d.text((tx, top + thumb_h + 10), label, font=font(13, True), fill=accent)
        d.text((tx, top + thumb_h + 30), "Immagine:", font=font(9), fill=COLORS["gray"])
        image_url_y = top + thumb_h + 41
        image_url_h = draw_url(d, (tx, image_url_y), image_url, thumb_w, size=8, color=COLORS["blue"])
        page_label_y = image_url_y + image_url_h + 3
        d.text((tx, page_label_y), "Pagina:", font=font(9), fill=COLORS["gray"])
        page_url_h = draw_url(d, (tx, page_label_y + 11), page_url, thumb_w, size=8, color=COLORS["blue"])
        if secondary_link:
            secondary_label, secondary_url = secondary_link
            secondary_label_y = page_label_y + 11 + page_url_h + 3
            d.text((tx, secondary_label_y), secondary_label, font=font(9), fill=COLORS["gray"])
            draw_url(d, (tx, secondary_label_y + 11), secondary_url, thumb_w, size=8, color=COLORS["blue"])


def build():
    img = Image.new("RGBA", (1600, 900), COLORS["white"])
    header(img, 25, "La dashboard per utenti funzionali")
    d = ImageDraw.Draw(img)
    d.text((90, 120), "Risposta al requisito business", font=font(20, True), fill=COLORS["teal"])
    d.text((90, 151), "Esempi reali: Metabase privilegia chiarezza e self-service; Qlik esplorazione ed estendibilità", font=font(24), fill=COLORS["navy"])

    showcase_card(
        d,
        img,
        (90, 215, 735, 745),
        "AWS | Metabase",
        "Esempi ufficiali Metabase: risultati sportivi e impegni globali, con KPI, filtri e mappe.",
        COLORS["blue"],
        COLORS["light_blue"],
        [
            (SHOWCASE / "metabase-uefa-euro-2024.png", "UEFA Euro 2024 | risultati", "https://www.metabase.com/images/examples/euro-2024.png", "https://www.metabase.com/examples"),
            (SHOWCASE / "metabase-unesco-education.png", "UNESCO | impegni education", "https://www.metabase.com/images/examples/education-dashboard.png", "https://www.metabase.com/examples"),
        ],
    )
    showcase_card(
        d,
        img,
        (865, 215, 1510, 745),
        "Qlik | Cloud + Talend",
        "Dashboard Qlik tradizionale: KPI, mappa, trend di vendite e profitti e analisi operative.",
        COLORS["green"],
        COLORS["light_teal"],
        [
            (SHOWCASE / "qlik-business-dashboard.png", "Business Dashboard | KPI e trend", "https://assets.qlik.com/image/upload/w_1240/q_auto/qlik/lp/free-trial/spot-free-trial-qlik-sense_wu7cuh.webp", "https://www.qlik.com/us/demo/qlik-sense-dashboards"),
        ],
        secondary_link=("Esempio avanzato: Global Supply Chain Sankey", "https://community.qlik.com/t5/Explore-Qlik-Gallery/Advanced-Sankey/ba-p/2551042"),
    )

    d.rounded_rectangle((225, 775, 1375, 832), radius=12, fill=COLORS["light_green"], outline=COLORS["teal"], width=2)
    draw_wrapped(d, (255, 788), "Metabase privilegia semplicità, leggibilità e self-service; Qlik abilita analisi più dense e personalizzabili, soprattutto con estensioni.", 1070, size=18, color=COLORS["green"], bold=True, line_gap=4, max_lines=2)
    d.text((625, 842), "Showcase pubblici: applicazioni reali, dati dimostrativi, non dati del cliente", font=font(13), fill=COLORS["gray"])
    output = OUT / "Slide recap 01 - dashboard utenti funzionali.png"
    img.convert("RGB").save(output, quality=95)
    print(output)


if __name__ == "__main__":
    build()
