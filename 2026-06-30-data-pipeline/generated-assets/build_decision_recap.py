from __future__ import annotations

from pathlib import Path
from textwrap import wrap

import xlsxwriter
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_XLSX = ROOT / "Data pipeline comparison assumptions v1.xlsx"
OUT_PNG = ROOT / "generated-assets"
LOGO = ROOT / "generated-assets/novigo-header-logo-template.png"
STAR = ROOT / "generated-assets/txt-star-mark-template.png"


FONT_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
FONT_SEMI = "/usr/share/fonts/truetype/noto/NotoSans-SemiBold.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"

COLORS = {
    "navy": "#25333D",
    "blue": "#2474C5",
    "cyan": "#2AA7C0",
    "teal": "#49AE8D",
    "green": "#07914D",
    "lime": "#8ABE41",
    "orange": "#E8A12D",
    "light_blue": "#EDF7FC",
    "light_teal": "#EEF9F6",
    "light_green": "#EEF8EE",
    "light_gray": "#F4F7F8",
    "line": "#D5E1E5",
    "gray": "#6E7C85",
    "white": "#FFFFFF",
    "black": "#20262B",
}


def make_formats(workbook: xlsxwriter.Workbook):
    def make(properties):
        return workbook.add_format({"font_name": "Poppins", **properties})

    return {
        "title": make({"bold": True, "font_size": 18, "font_color": COLORS["navy"], "bottom": 2, "bottom_color": COLORS["cyan"]}),
        "subtitle": make({"font_size": 11, "font_color": COLORS["gray"], "text_wrap": True, "valign": "top"}),
        "section": make({"bold": True, "font_size": 12, "font_color": COLORS["navy"], "bg_color": COLORS["light_blue"], "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "vcenter"}),
        "header": make({"bold": True, "font_size": 11, "font_color": COLORS["white"], "bg_color": COLORS["navy"], "border": 1, "border_color": COLORS["navy"], "text_wrap": True, "valign": "vcenter"}),
        "body": make({"font_size": 11, "font_color": COLORS["black"], "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "top"}),
        "body_alt": make({"font_size": 11, "font_color": COLORS["black"], "bg_color": COLORS["light_gray"], "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "top"}),
        "note": make({"font_size": 11, "italic": True, "font_color": COLORS["gray"], "text_wrap": True, "valign": "top"}),
        "aws": make({"font_size": 11, "bold": True, "font_color": COLORS["blue"], "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "top"}),
        "qlik": make({"font_size": 11, "bold": True, "font_color": COLORS["green"], "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "top"}),
        "assumption": make({"font_size": 11, "font_color": COLORS["orange"], "bg_color": "#FFF8EC", "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "top"}),
        "confirmed": make({"font_size": 11, "font_color": COLORS["green"], "bg_color": COLORS["light_green"], "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "top"}),
        "verify": make({"font_size": 11, "font_color": COLORS["blue"], "bg_color": COLORS["light_blue"], "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "top"}),
        "money": make({"font_size": 11, "num_format": '#,##0 "EUR"', "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "top"}),
        "money_assumption": make({"font_size": 11, "num_format": '#,##0 "EUR"', "font_color": COLORS["orange"], "bg_color": "#FFF8EC", "border": 1, "border_color": COLORS["line"], "text_wrap": True, "valign": "top"}),
    }


def write_table(ws, start_row, headers, rows, formats, widths=None, table_name=None):
    for c, header in enumerate(headers):
        ws.write(start_row, c, header, formats["header"])
    for r, row in enumerate(rows, start_row + 1):
        for c, value in enumerate(row):
            if isinstance(value, tuple):
                value, fmt_name = value
                fmt = formats[fmt_name]
            else:
                fmt = formats["body_alt"] if (r - start_row) % 2 == 0 else formats["body"]
            ws.write(r, c, value, fmt)
    if widths:
        for c, width in enumerate(widths):
            ws.set_column(c, c, width)
    ws.set_row(start_row, 30)
    for r in range(start_row + 1, start_row + 1 + len(rows)):
        ws.set_row(r, 52)
    if table_name:
        ws.add_table(start_row, 0, start_row + len(rows), len(headers) - 1, {"name": table_name, "style": "Table Style Medium 2", "columns": [{"header": h} for h in headers]})


def setup_sheet(ws, title, subtitle, formats, widths):
    ws.hide_gridlines(2)
    ws.set_zoom(90)
    ws.set_landscape()
    ws.fit_to_pages(1, 0)
    ws.set_margins(left=0.25, right=0.25, top=0.4, bottom=0.4)
    ws.set_row(0, 28)
    ws.merge_range(0, 0, 0, len(widths) - 1, title, formats["title"])
    ws.merge_range(1, 0, 1, len(widths) - 1, subtitle, formats["subtitle"])
    for c, width in enumerate(widths):
        ws.set_column(c, c, width)
    ws.freeze_panes(3, 0)


def build_xlsx():
    wb = xlsxwriter.Workbook(OUT_XLSX)
    wb.set_properties({"title": "Data pipeline - confronto AWS/Qlik", "subject": "Funzionalita, tempi, costi e assunzioni", "author": "TXT / Novigo"})
    f = make_formats(wb)

    ws = wb.add_worksheet("Executive recap")
    setup_sheet(ws, "Data pipeline | Recap per la decisione", "Obiettivo: rispondere al requisito business su dashboard per utenti funzionali e rendere espliciti tempi, costi e assunzioni. La v5 resta la baseline tecnica; questo workbook completa il confronto.", f, [28, 35, 35, 42])
    rows = [
        ["Domanda", "AWS | Dagster + dbt + Metabase", "Qlik | Qlik Cloud + capability Talend", "Lettura decisionale"],
        ["Un utente funzionale può creare dashboard?", ("Sì, su modelli/mart pubblicati e con permessi; Metabase documenta query builder, visualizzazioni, dashboard, metriche, alert ed export.", "aws"), ("Sì, con un orientamento più diretto all'analytics self-service; Qlik documenta analytics self-service, esplorazione e automazioni no-code. Entitlement e modello dati da verificare.", "qlik"), ("Entrambe sono utilizzabili. Qlik risponde più direttamente al requisito di self-service; AWS/Metabase richiede più disciplina preventiva su modello dati, metriche e governance. Inferenza da validare in pilot.", "assumption")],
        ["Cosa resta in carico al team tecnico?", ("Nuove fonti, regole custom, trasformazioni, qualità, deployment AWS, modelli dbt e governance.", "aws"), ("Connettori/runtime, regole complesse, modello semantico, packaging/licenze, governance tenant e casi non coperti dai componenti disponibili.", "qlik"), ("Il self-service riguarda il consumo e la composizione della dashboard; non elimina il lavoro tecnico sulla pipeline e sulle regole.", "confirmed")],
        ["Tempi indicativi per un primo pilot", ("10-18 settimane con reference implementation riusabile; 14-24 settimane se setup e governance sono da costruire da zero.", "assumption"), ("9-16 settimane se tenant, licenze e connettori sono pronti; 13-22 settimane se devono essere attivati o verificati.", "assumption"), ("Range indicativi, non presenti nelle fonti e da validare con perimetro, fonti, volumi e disponibilità degli skill.", "verify")],
        ["Costi oggi difendibili", ("Nessun importo validato. Da dimensionare: delivery, cloud/runtime, DB, storage, monitoraggio e run.", "verify"), ("Baseline utente: 30-50k EUR per un piano 50 GB; non è listino Qlik né prezzo impegnativo. Periodo, IVA, sconti, utenti, add-on e capability incluse da verificare.", "assumption"), ("Non esiste ancora un TCO comparabile. Il prossimo passo è completare gli input commerciali e tecnici, non scegliere sulla base del solo canone.", "verify")],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [30, 48, 48, 50], "ExecutiveRecap")
    ws.write(9, 0, "Sintesi", f["section"])
    ws.merge_range(9, 1, 9, 3, "La risposta al requisito business è: entrambe, con prerequisiti diversi. Qlik è il candidato più diretto per il self-service analytics; AWS/Metabase è coerente quando prevalgono controllo dello stack, riuso engineering e processing custom.", f["confirmed"])
    ws.write(10, 0, "Non ancora deciso", f["section"])
    ws.merge_range(10, 1, 10, 3, "Licensing/entitlement Qlik-Talend, scope del primo pilot, accessi/ruoli, fonti e volumi reali, archiviazione, effort e rate delivery.", f["verify"])

    ws = wb.add_worksheet("Functional comparison")
    setup_sheet(ws, "Confronto funzionale | Utenti business e team tecnico", "Le valutazioni distinguono ciò che è documentato dalla deduzione progettuale. 'Sì' significa capability disponibile sul layer BI; non significa che la pipeline sia già pronta.", f, [30, 27, 27, 34, 42])
    rows = [
        ["Criterio", "AWS | Metabase", "Qlik | Qlik Cloud", "Impatto per il business", "Fonte / assunzione"],
        ["Creazione dashboard da utente funzionale", ("Sì, con dati/mart già pubblicati", "aws"), ("Sì, self-service analytics", "qlik"), "Risponde al requisito in entrambe; Qlik è più orientato alla piattaforma analytics.", "Metabase/Qlik docs nelle note 08, 11, 12; lettura comparativa da validare"],
        ["Query e visualizzazioni", ("Query builder, visualizzazioni, dashboard", "aws"), ("Esplorazione, analisi e dashboard", "qlik"), "L'utente può comporre viste senza aprire ogni volta un ticket di sviluppo.", "Capability documentate"],
        ["Metriche e modello governato", ("Possibile con data modeling e convenzioni; setup da definire", "verify"), ("Possibile nel modello Qlik; governance/packaging da verificare", "verify"), "La libertà dell'utente deve restare dentro metriche certificate.", "Inferenza progettuale; requisiti governance da confermare"],
        ["Nuove fonti e nuove regole", ("Team data engineering", "aws"), ("Team Talend/Qlik o sviluppo dedicato", "qlik"), "Non è self-service: richiede data contract, mapping, controlli e test.", "WBS e architetture draft 09-10"],
        ["Dashboard tecnica / esiti / scarti", ("Sì, sopra run log e mart", "aws"), ("Sì, se dati/run log sono esposti", "qlik"), "Necessaria per rendere operativa la gestione delle anomalie.", "WBS ProSIGNAL/CDG e draft 08"],
        ["Processing custom e file complessi", ("Forte flessibilità, con codice/componenti custom", "aws"), ("Da verificare su fixed-column, file grandi e cross-file checks", "verify"), "È il discrimine principale per ProSIGNAL.", "Draft 08, 11, 12; gap tecnico esplicito"],
        ["Competenze richieste", ("AWS, data engineering, SQL/dbt, Python, BI", "aws"), ("Talend, Qlik, data integration, BI governance", "qlik"), "La scelta modifica il profilo del team e il modello operativo.", "Draft 08"],
        ["Dipendenza da licenze/tenant", ("Più bassa lato BI; cloud/run da dimensionare", "aws"), ("Più alta; entitlement e capacity da verificare", "qlik"), "Incide su tempi di attivazione e costo ricorrente.", "Draft 08, 11, 12"],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [30, 32, 32, 42, 45], "FunctionalComparison")

    ws = wb.add_worksheet("Delivery estimate")
    setup_sheet(ws, "Tempi | Stima indicativa per un primo pilot", "Assunzione di lavoro: un primo caso, fonti e output selezionati, dashboard business e tecnica, UAT e go-live controllato. Range da validare; non sono date o commitment.", f, [28, 20, 20, 20, 20, 52])
    rows = [
        ["Fase", "Comune", "AWS", "Qlik", "Tipo", "Driver / dipendenza"],
        ["Assessment e perimetro", "1-2 sett.", "1-2 sett.", "1-2 sett.", "Baseline", "Numero fonti, output, utenti, regole e disponibilità degli owner."],
        ["Blueprint e scelta scenario", "1 sett.", "1 sett.", "1 sett.", "Baseline", "Decisione su AWS ECS/EC2/RDS o Qlik tenant/runtime/storage."],
        ["Data contract e mapping", "2-4 sett.", "2-4 sett.", "2-4 sett.", "Baseline", "Qualità dei tracciati, tabelle guida, versioni, ownership e soglie."],
        ["Ingestion, quality e mart", "-", "4-8 sett.", "3-6 sett.", "Variabile", "Qlik può ridurre il custom solo con connettori, capacity e runtime già disponibili."],
        ["Modello dashboard e BI", "2-3 sett.", "2-3 sett.", "2-3 sett.", "Variabile", "Numero dashboard, metriche certificate, accessi e distribuzione."],
        ["Test, UAT e go-live", "2-3 sett.", "2-3 sett.", "2-3 sett.", "Baseline", "Dati campione, riconciliazioni, parallel run, gestione scarti e runbook."],
        ["Totale pilot", "10-18 sett.", "10-18 sett. con riuso; 14-24 da zero", "9-16 sett. se pronto; 13-22 se da attivare", "Stima", "Range indicativi costruiti per il confronto; da sostituire con estimate bottom-up dopo perimetro."],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [28, 18, 25, 28, 14, 55], "DeliveryEstimate")
    ws.write(14, 0, "Importante", f["section"])
    ws.merge_range(14, 1, 14, 5, "Le fonti di progetto dichiarano esplicitamente che il piano comune non contiene durate, date o effort. I range sopra sono una stima di lavoro per rendere possibile il confronto richiesto e vanno sostituiti con un estimate bottom-up.", f["assumption"])

    ws = wb.add_worksheet("Economics")
    setup_sheet(ws, "Economics | Driver, baseline e gap", "La sola cifra disponibile è una baseline utente per Qlik/Talend. Tutti gli altri importi restano da dimensionare; il foglio evita di presentare un totale non difendibile.", f, [30, 30, 30, 18, 50])
    rows = [
        ["Voce", "AWS | stack componibile", "Qlik | Cloud + Talend", "Stato", "Cosa serve per chiuderla"],
        ["Licenze / subscription", ("Non quantificato", "verify"), ("30-50k EUR baseline utente per piano 50 GB; non listino", "assumption"), ("Parziale", "assumption"), "Periodo, IVA, sconti, utenti, capacity add-on, bundle e capability Talend/Qlik incluse."],
        ["Delivery / implementazione", ("Da stimare S/M/L", "verify"), ("Da stimare S/M/L", "verify"), ("Aperto", "verify"), "Perimetro, fonti, mapping, regole, output, dashboard, UAT, sicurezza e ruoli."],
        ["Cloud / runtime / database", ("Da dimensionare", "verify"), ("Runtime/storage da definire", "verify"), ("Aperto", "verify"), "AWS: ECS/EC2, RDS/DB cliente, S3, frequenza run, retention e monitoraggio. Qlik: runtime Talend, storage e tenant."],
        ["Run / supporto / manutenzione", ("Da stimare", "verify"), ("Da stimare", "verify"), ("Aperto", "verify"), "SLA, orari, numero run, gestione anomalie, evolutive e ownership."],
        ["Costo totale comparabile", ("Non disponibile", "verify"), ("Non disponibile", "verify"), ("Non chiuso", "verify"), "Non sommare la baseline Qlik con voci AWS mancanti: completare il modello di costo comune."],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [31, 34, 36, 14, 58], "EconomicsDrivers")
    ws.write(11, 0, "Formula da completare", f["section"])
    ws.merge_range(11, 1, 11, 4, "TCO primo anno = setup/delivery + subscription/licenze + cloud/runtime/DB + supporto/run + eventuali add-on. Il workbook non calcola il totale finché non vengono inseriti effort, rate, periodo e sizing.", f["note"])
    ws.write(12, 0, "Baseline da non confondere", f["section"])
    ws.merge_range(12, 1, 12, 4, "30-50k EUR è una ipotesi commerciale di partenza per Qlik/Talend su 50 GB, non un prezzo ufficiale e non include automaticamente delivery, runtime, storage, utenti o add-on.", f["assumption"])

    ws = wb.add_worksheet("Assumptions")
    setup_sheet(ws, "Assunzioni e punti da validare", "Le assunzioni consentono di rispondere al commento senza trasformare ipotesi tecniche o commerciali in promesse.", f, [7, 35, 24, 50, 44, 30])
    rows = [
        ["ID", "Assunzione / punto aperto", "Stato", "Impatto sul confronto", "Validazione richiesta", "Fonte / responsabile"],
        ["A1", "Il requisito business è permettere a utenti funzionali non sviluppatori di creare o modificare dashboard su dati certificati.", ("Assunzione di lavoro", "assumption"), "Rende centrale il confronto del layer BI, non solo della pipeline.", "Confermare audience, autonomia attesa e tipi di dashboard.", "Commento utente / owner business"],
        ["A2", "Il self-service non include la costruzione autonoma di nuove fonti, regole di dominio o controlli complessi.", ("Assunzione di lavoro", "assumption"), "Entrambe richiedono comunque un team tecnico per la pipeline.", "Definire confine tra dashboard authoring e data engineering.", "Decisione business/IT"],
        ["A3", "Metabase è accettabile come layer BI/self-service nello scenario AWS.", ("Da confermare", "verify"), "Se non lo è, lo scenario AWS richiede un diverso layer BI.", "Verificare accessi, embedding/export, pubblicazione e governance clienti esterni.", "Owner BI / sicurezza"],
        ["A4", "Qlik Cloud Analytics Premium e Qlik Talend Cloud non sono automaticamente equivalenti a una licenza Talend completa.", ("Da verificare", "verify"), "Può cambiare sia la copertura funzionale sia il costo e il tempo di attivazione.", "Verificare contratto/tenant, piani, capacity, runtime e capability incluse.", "Procurement / Qlik"],
        ["A5", "La baseline 30-50k EUR riguarda un piano Qlik/Talend da 50 GB, come ipotesi utente.", ("Baseline provvisoria", "assumption"), "È l'unico ordine di grandezza oggi disponibile per la licenza/subscription.", "Confermare periodo, IVA, sconti, utenti, add-on e perimetro.", "Commerciale"],
        ["A6", "I range temporali sono indicativi per un primo pilot, non per la copertura completa dei tre casi.", ("Stima da validare", "assumption"), "Evita di leggere il confronto come commitment di delivery.", "Definire caso pilota, fonti, output, dashboard, UAT e dipendenze.", "PM / delivery"],
        ["A7", "ProSIGNAL è lo stress test per file grandi, fixed-column, controlli cross-file e output regolamentari.", ("Da validare", "verify"), "Può spostare la decisione verso lo stack più flessibile se Qlik/Talend non copre il caso.", "Usare file e tracciati reali per benchmark comparativo.", "Owner ProSIGNAL"],
        ["A8", "Kiron CDG e CDG interno sono casi CDG-like con Actual/Forecast, mapping, riconciliazioni e dashboard.", ("Documentato", "confirmed"), "Sono adatti a verificare il riuso della blueprint e la capacità di governare regole.", "Confermare fonti, output e responsabilità nel perimetro pilota.", "Materiali Kiron/CDG"],
        ["A9", "AWS ECS/EC2 e RDS/database cliente restano varianti di deployment, non una scelta strategica separata.", ("Documentato", "confirmed"), "Impatta costi, operation e gestione, non la domanda business principale.", "Scegliere dopo sizing e modello operativo.", "Draft architetturale 10"],
        ["A10", "Il confronto non assegna una percentuale di copertura né un vincitore assoluto.", ("Vincolo", "confirmed"), "La decisione deve basarsi su priorità, prerequisiti e costo totale.", "Usare pilot e criteri di accettazione per chiudere i gap.", "Review copertura v5"],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [7, 42, 24, 52, 46, 28], "Assumptions")

    ws = wb.add_worksheet("Sources")
    setup_sheet(ws, "Fonti e livello di autorità", "Le fonti locali del progetto sono la base del confronto; le capability prodotto sono riportate come documentate nelle note già presenti e restano soggette a verifica commerciale/tenant.", f, [30, 80, 22, 56])
    rows = [
        ["Tipo", "Fonte", "Uso", "Nota"],
        ["Feedback utente", "Commento riportato nella richiesta", "Requisito business", "Richiede confronto su funzionalità, tempi e costi e risposta su dashboard per utenti funzionali."],
        ["Scenario comparison", "2026-06-30-data-pipeline/drafts/08-scenario-comparison.md", "Confronto tecnico/business", "Fonte principale per AWS vs Talend/Qlik, capability, trade-off, range e gap."],
        ["Workplan", "2026-06-30-data-pipeline/drafts/09-wbs-and-workplan.md", "Fasi e economics", "Dichiara che il piano comune non contiene durate, date o effort; contiene il modello setup/delivery/run."],
        ["Architecture", "2026-06-30-data-pipeline/drafts/10-architecture-brief.md", "Componenti e limiti", "Descrive i due scenari e i punti tecnici da verificare."],
        ["Qlik notes", "2026-06-30-data-pipeline/drafts/11-qlik-context7-notes.md", "Capability e licensing", "Qlik/Talend, self-service, automation e baseline 30-50k EUR; non sostituisce verifica commerciale."],
        ["AWS/Metabase notes", "2026-06-30-data-pipeline/drafts/12-dagster-metabase-context7-notes.md", "Capability BI", "Metabase self-service, query builder, dashboard, metriche, alert, export; costi e governance da dimensionare."],
        ["Coverage review", "2026-06-30-data-pipeline/drafts/25-process-coverage-slide.md", "Terminologia e limiti", "Copertura potenziale distinta da readiness; niente percentuali artificiali."],
        ["Official product URLs", "https://www.qlik.com/us/pricing; https://www.qlik.com/us/pricing/data-integration-products-pricing", "Pricing Qlik", "Consultate nelle note il 2026-06-30; aggiornare prima di un'offerta."],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [20, 82, 23, 60], "Sources")

    ws = wb.add_worksheet("Slide copy")
    setup_sheet(ws, "Copy pronto per le slide", "Testo sintetico da ricopiare nelle nuove slide PowerPoint. Le immagini consegnate mostrano la composizione visiva aderente alla v5.", f, [8, 33, 48, 54])
    rows = [
        ["N", "Titolo", "Messaggio / contenuto", "Guardrail"],
        ["1", "La dashboard può essere costruita da utenti funzionali in entrambe le soluzioni", "AWS/Metabase: sì, su modelli certificati; Qlik: sì, con orientamento più diretto al self-service analytics. La differenza è quanta preparazione tecnica serve prima e quanta autonomia si vuole lasciare dopo.", "Non dire 'zero sviluppo': nuove fonti, regole e qualità restano tecniche."],
        ["2", "Il confronto decisionale deve partire dall'utente, non dal tool", "Confrontare dashboard authoring, esplorazione, metriche governate, gestione fonti/regole, monitoraggio, custom processing, skill e dipendenza da licenza.", "Usare la stessa scala e separare capability documentata da inferenza."],
        ["3", "Tempi: Qlik può partire prima solo se piattaforma e connettori sono già disponibili", "Pilot indicativo: AWS 10-18 settimane con riuso / 14-24 da zero; Qlik 9-16 se pronto / 13-22 se da attivare. Range da validare.", "Non chiamarli date o commitment; esplicitare scope pilot e prerequisiti."],
        ["4", "Costi: oggi conosciamo un baseline Qlik/Talend, non un totale comparabile", "Qlik/Talend: 30-50k EUR baseline utente per 50 GB. AWS: cloud/run/DB/storage/monitoraggio da dimensionare. Delivery e supporto: S/M/L da stimare per entrambe.", "Non presentare 30-50k come listino Qlik né sommare costi mancanti."],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [7, 42, 58, 60], "SlideCopy")

    wb.close()


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def draw_wrapped(draw, xy, text, width, size=22, color=None, bold=False, line_gap=7, max_lines=None):
    color = color or COLORS["black"]
    fnt = font(size, bold)
    words = text.split()
    lines = []
    current = ""
    for word in words:
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


def header(img, page, title, nav_active="DECISIONE"):
    d = ImageDraw.Draw(img)
    logo = Image.open(LOGO).convert("RGBA")
    logo.thumbnail((155, 42))
    img.alpha_composite(logo, (17, 15))
    d.rectangle((0, 82, 185, 88), fill=COLORS["cyan"])
    d.text((220, 20), "Data pipeline |", font=font(30, True), fill="#A4A9AD")
    d.text((438, 20), title, font=font(30, True), fill=COLORS["black"])
    nav = ["PERCHÉ", "VALORE", "PROPOSTA", "PIANO", "DECISIONE"]
    x = 1060
    for i, item in enumerate(nav):
        active = item == nav_active
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


def card(d, box, title, body, accent, fill=COLORS["white"], body_size=20, bullets=None, badge=None):
    x1, y1, x2, y2 = box
    d.rounded_rectangle(box, radius=16, fill=fill, outline=accent, width=2)
    d.line((x1, y1, x2, y1), fill=accent, width=7)
    d.text((x1 + 24, y1 + 22), title, font=font(25, True), fill=accent)
    if badge:
        d.rounded_rectangle((x1 + 24, y1 + 65, x2 - 24, y1 + 100), radius=17, fill=accent)
        tw = d.textlength(badge, font=font(15, True))
        d.text(((x1 + x2 - tw) / 2, y1 + 75), badge, font=font(15, True), fill=COLORS["white"])
        y = y1 + 125
    else:
        y = y1 + 72
    y += draw_wrapped(d, (x1 + 24, y), body, x2 - x1 - 48, size=body_size, color=COLORS["black"], line_gap=5)
    if bullets:
        y += 18
        for bullet in bullets:
            d.ellipse((x1 + 26, y + 5, x1 + 39, y + 18), fill=accent)
            y += draw_wrapped(d, (x1 + 50, y), bullet, x2 - x1 - 74, size=16, color=COLORS["black"], line_gap=4, max_lines=2) + 11


def save_slide(filename, title, page, painter):
    img = Image.new("RGBA", (1600, 900), COLORS["white"])
    header(img, page, title)
    painter(img)
    img.convert("RGB").save(OUT_PNG / filename, quality=95)


def build_images():
    OUT_PNG.mkdir(parents=True, exist_ok=True)

    def slide1(img):
        d = ImageDraw.Draw(img)
        d.text((90, 120), "Risposta al requisito business", font=font(20, True), fill=COLORS["teal"])
        d.text((90, 151), "Entrambe possono supportare il self-service; cambia il livello di preparazione tecnica", font=font(24), fill=COLORS["navy"])
        card(d, (90, 225, 735, 745), "AWS | Metabase", "Può creare e aggiornare dashboard partendo da dati già preparati e certificati.", COLORS["blue"], COLORS["light_blue"], bullets=["Query builder, visualizzazioni, dashboard, metriche, alert ed export.", "Utente funzionale: costruisce viste senza dipendere ogni volta dallo sviluppo.", "Team tecnico: nuove fonti, regole, qualità e gestione della piattaforma.", "Prerequisito: dati preparati, metriche condivise e permessi definiti."] , badge="UTILIZZABILE")
        card(d, (865, 225, 1510, 745), "Qlik | Cloud + Talend", "Può esplorare i dati e costruire dashboard con strumenti più guidati.", COLORS["green"], COLORS["light_teal"], bullets=["Dashboard ed esplorazione self-service documentate.", "Automazioni no-code e gestione operativa disponibili come capability di piattaforma.", "Team tecnico: dati, regole, runtime e gestione degli accessi.", "Prerequisito: licenza, capacità disponibile e componenti Talend da verificare."] , badge="UTILIZZABILE*")
        d.rounded_rectangle((225, 775, 1375, 832), radius=12, fill=COLORS["light_green"], outline=COLORS["teal"], width=2)
        draw_wrapped(d, (255, 788), "Conclusione: Qlik risponde più direttamente al requisito di dashboard self-service; AWS/Metabase è coerente quando contano controllo dello stack, riuso engineering e processing custom.", 1190, size=18, color=COLORS["green"], bold=True, line_gap=4, max_lines=2)
        d.text((930, 842), "Lettura comparativa: da validare con utenti e pilot | * da verificare su licenza/tenant", font=font(13), fill=COLORS["gray"])

    def slide2(img):
        d = ImageDraw.Draw(img)
        d.text((80, 118), "Confronto funzionale per il requisito business", font=font(20, True), fill=COLORS["teal"])
        d.text((80, 151), "La domanda non è solo quale pipeline funziona: è quanta autonomia avrà l'utente funzionale", font=font(24), fill=COLORS["navy"])
        x0, y0 = 80, 215
        widths = [355, 430, 430]
        headers = ["CRITERIO", "AWS | METABASE", "QLIK | CLOUD + TALEND"]
        fills = [COLORS["light_gray"], COLORS["light_blue"], COLORS["light_teal"]]
        accents = [COLORS["gray"], COLORS["blue"], COLORS["green"]]
        x = x0
        for w, h, fill, acc in zip(widths, headers, fills, accents):
            d.rounded_rectangle((x, y0, x + w, y0 + 56), radius=12, fill=fill, outline=acc, width=2)
            d.text((x + 20, y0 + 17), h, font=font(17, True), fill=acc)
            x += w + 12
        rows = [
            ("Creare dashboard", "Sì, su mart/modello pubblicato", "Sì, self-service analytics"),
            ("Esplorare e visualizzare", "Query builder + visualizzazioni", "Esplorazione + analisi"),
            ("Metriche governate", "Da impostare con data modeling", "Da verificare nel modello/licenza"),
            ("Nuove fonti e regole", "Team data engineering", "Team Talend/Qlik o custom"),
            ("Dashboard esiti/scarti", "Sì, sopra run log e mart", "Sì, se run log e output sono esposti"),
            ("File complessi / custom", "Flessibilità elevata", "Da benchmarkare su ProSIGNAL"),
            ("Prerequisito infrastrutturale", "Infra nostra/cliente: disponibilità e compatibilità", "Cliente: accettazione del cloud"),
            ("Skill prevalenti", "AWS, SQL/dbt, Python, BI", "Talend, Qlik, BI governance"),
        ]
        y = y0 + 69
        for i, (a, b, c) in enumerate(rows):
            fill = COLORS["white"] if i % 2 == 0 else COLORS["light_gray"]
            x = x0
            vals = [a, b, c]
            for j, (w, val) in enumerate(zip(widths, vals)):
                d.rectangle((x, y, x + w, y + 55), fill=fill, outline=COLORS["line"], width=1)
                draw_wrapped(d, (x + 17, y + 12), val, w - 34, size=17 if j else 18, color=COLORS["navy"] if j == 0 else (COLORS["blue"] if j == 1 else COLORS["green"]), bold=j == 0, line_gap=3, max_lines=2)
                x += w + 12
            y += 61
        d.rounded_rectangle((220, 724, 1380, 812), radius=13, fill=COLORS["light_green"], outline=COLORS["teal"], width=2)
        draw_wrapped(d, (250, 743), "Per l'utente funzionale: Qlik è il candidato più diretto. Per la delivery: AWS conserva maggiore controllo e flessibilità sul processo dati.", 1100, size=22, color=COLORS["green"], bold=True, line_gap=5, max_lines=2)
        d.text((1040, 827), "Lettura comparativa da validare con il pilot", font=font(13), fill=COLORS["gray"])

    def slide3(img):
        d = ImageDraw.Draw(img)
        d.text((80, 118), "Piano indicativo per un primo pilot", font=font(20, True), fill=COLORS["teal"])
        d.text((80, 151), "Qlik può partire prima solo se piattaforma, connettori e capability sono già disponibili", font=font(24), fill=COLORS["navy"])
        x0, y0 = 90, 225
        label_w, bar_w = 280, 1160
        d.text((x0, y0 - 34), "FASE", font=font(15, True), fill=COLORS["gray"])
        for i, m in enumerate(["M1", "M2", "M3", "M4", "M5"]):
            x = x0 + label_w + (bar_w / 5) * i
            d.line((x, y0 - 10, x, 715), fill=COLORS["line"], width=1)
            d.text((x + 8, y0 - 34), m, font=font(15, True), fill=COLORS["gray"])
        phases = [
            ("Assessment + perimetro", 1, 2, "#65AECB", "#63B28D"),
            ("Blueprint + scelta", 2, 2, "#65AECB", "#63B28D"),
            ("Data contract + mapping", 2, 3, "#65AECB", "#63B28D"),
            ("Ingestion + quality + mart", 3, 5, "#2474C5", "#07914D"),
            ("Dashboard + UAT + go-live", 4, 5, "#2474C5", "#07914D"),
        ]
        y = y0 + 20
        for name, start, end, aws_col, qlik_col in phases:
            d.text((x0, y + 25), name, font=font(17, True), fill=COLORS["navy"])
            base_x = x0 + label_w + (bar_w / 5) * (start - 1) + 8
            w = (bar_w / 5) * (end - start + 1) - 16
            d.rounded_rectangle((base_x, y + 4, base_x + w, y + 30), radius=8, fill=aws_col)
            d.rounded_rectangle((base_x, y + 40, base_x + w, y + 66), radius=8, fill=qlik_col)
            d.text((x0 + label_w - 100, y + 7), "AWS", font=font(13, True), fill=COLORS["blue"])
            d.text((x0 + label_w - 100, y + 43), "Qlik", font=font(13, True), fill=COLORS["green"])
            y += 83
        d.rounded_rectangle((390, 682, 1485, 746), radius=12, fill=COLORS["light_blue"], outline=COLORS["blue"], width=2)
        d.text((420, 696), "AWS: 7-13 sett. con riuso | 10-17 sett. da zero", font=font(20, True), fill=COLORS["blue"])
        d.rounded_rectangle((390, 754, 1485, 818), radius=12, fill=COLORS["light_teal"], outline=COLORS["green"], width=2)
        d.text((420, 768), "Qlik: 6-11 sett. se pronto | 9-15 sett. se da attivare", font=font(20, True), fill=COLORS["green"])
        d.text((90, 835), "Stima indicativa da validare: scope pilot, fonti, volumi, output, skill, licenze e disponibilità degli owner.", font=font(14), fill=COLORS["gray"])

    def slide4(img):
        d = ImageDraw.Draw(img)
        d.text((80, 118), "Economics | ciò che sappiamo e ciò che manca", font=font(20, True), fill=COLORS["teal"])
        d.text((80, 151), "Oggi esiste una baseline Qlik/Talend, ma non ancora un totale comparabile", font=font(24), fill=COLORS["navy"])
        card(d, (90, 235, 750, 720), "AWS | Stack componibile", "Costi diretti: €5k cloud/runtime.", COLORS["blue"], COLORS["light_blue"], bullets=["Effort e run del team interno esclusi dal budget.", "Sizing: 2 EC2, 1 RDS, 1 TB S3 medio e lifecycle.", "Driver: fonti, volumi, retention, frequenza run e SLA.", "Budget indicativo, non offerta."]) 
        card(d, (850, 235, 1510, 720), "Qlik | Cloud + Talend", "Costi diretti: €30k subscription*.", COLORS["green"], COLORS["light_teal"], bullets=["Effort e run del team interno esclusi dal budget.", "Subscription base 50 GB; periodo e capability incluse da verificare.", "Driver: utenti, capacity, add-on, runtime e storage.", "Budget indicativo, non offerta."]) 
        d.rounded_rectangle((185, 754, 1415, 825), radius=13, fill=COLORS["light_green"], outline=COLORS["teal"], width=2)
        draw_wrapped(d, (220, 772), "Scenario base/basso: usare questi numeri per il confronto iniziale; completare poi la validazione commerciale e tecnica.", 1280, size=21, color=COLORS["green"], bold=True, line_gap=4, max_lines=2)
        d.text((1150, 835), "* Qlik: periodo da confermare", font=font(14, True), fill=COLORS["orange"])

    save_slide("Slide recap 01 - dashboard utenti funzionali.png", "La dashboard per utenti funzionali", 25, slide1)
    save_slide("Slide recap 02 - confronto funzionale.png", "Confronto funzionale", 26, slide2)
    save_slide("Slide recap 03 - tempi pilot.png", "Tempi indicativi", 27, slide3)
    save_slide("Slide recap 04 - economics.png", "Economics", 28, slide4)


if __name__ == "__main__":
    build_xlsx()
    build_images()
    print(OUT_XLSX)
    for p in sorted(OUT_PNG.glob("Slide recap *.png")):
        print(p)
