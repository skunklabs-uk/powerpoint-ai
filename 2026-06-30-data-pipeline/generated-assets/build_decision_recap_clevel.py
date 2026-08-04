from __future__ import annotations

import sys
from pathlib import Path

import xlsxwriter


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_decision_recap import COLORS, make_formats, setup_sheet, write_table  # noqa: E402


ROOT = HERE.parent
OUT = ROOT / "Data pipeline comparison C-level v2.xlsx"


def build():
    wb = xlsxwriter.Workbook(OUT)
    wb.set_properties({
        "title": "Data pipeline - confronto C-level AWS/Qlik",
        "subject": "Funzionalita, tempi, economics e assunzioni",
        "author": "TXT / Novigo",
    })
    f = make_formats(wb)

    # 1. Executive recap
    ws = wb.add_worksheet("Executive recap")
    setup_sheet(
        ws,
        "Data pipeline | Recap per la decisione",
        "Le due strade rispondono a priorità diverse: Qlik punta di più sul self-service, AWS lascia più controllo sullo stack.",
        f,
        [28, 40, 40, 44],
    )
    rows = [
        ["Tema", "AWS | Dagster + dbt + Metabase", "Qlik | Cloud + capability Talend", "Cosa significa per la scelta"],
        ["Utenti funzionali", ("Sì: possono costruire e aggiornare dashboard sui dati preparati dal team tecnico.", "aws"), ("Sì: possono esplorare i dati e creare dashboard con un'esperienza più guidata.", "qlik"), ("Entrambe funzionano; Qlik è più vicino al bisogno espresso.", "confirmed")],
        ["Pilot tecnico", ("3-5 settimane con componenti riusabili. 5-7 da zero.", "assumption"), ("2-4 settimane se pronto. 4-6 se le attivazioni sono da completare.", "assumption"), ("Perimetro ristretto: 1 caso d'uso, 1-2 fonti e 2-3 dashboard.", "verify")],
        ["Costi diretti primo anno", ("€5k", "aws"), ("€30k*", "qlik"), ("Solo cloud AWS o subscription Qlik; effort interno escluso.", "assumption")],
        ["Passo successivo", ("Test su ProSIGNAL e conferma del sizing AWS.", "aws"), ("Verifica del tenant e test su ProSIGNAL.", "qlik"), ("La scelta va presa dopo un pilot misurabile, non guardando solo il canone.", "confirmed")],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [28, 42, 42, 46], "ExecutiveClevel")
    ws.write(10, 0, "Messaggio", f["section"])
    ws.merge_range(10, 1, 10, 3, "Qlik è più diretto per il self-service business. AWS offre più controllo su pipeline, riuso e logiche custom.", f["confirmed"])
    ws.write(11, 0, "Nota", f["section"])
    ws.merge_range(11, 1, 11, 3, "* Qlik: subscription base di 30k EUR per 12 mesi; periodo e perimetro sono da confermare. Effort e supporto del team interno sono esclusi.", f["assumption"])
    ws.write(13, 0, "Disclaimer", f["section"])
    ws.merge_range(13, 1, 13, 3, "Tempi, dimensionamenti ed economics derivano dalle assunzioni del workbook; non costituiscono un commitment di delivery né un'offerta commerciale.", f["note"])

    # 2. Functional comparison
    ws = wb.add_worksheet("Functional comparison")
    setup_sheet(
        ws,
        "Confronto funzionale | Cosa cambia per il business",
        "Il confronto riguarda ciò che l'utente può fare e ciò che resta al team tecnico.",
        f,
        [29, 38, 38, 46],
    )
    rows = [
        ["Cosa osserviamo", "AWS | Metabase", "Qlik | Cloud + Talend", "Lettura per il business"],
        ["Creare dashboard", ("Sì, sui dati già preparati dal team tecnico.", "aws"), ("Sì, con strumenti guidati per esplorare i dati.", "qlik"), "Entrambe sono utilizzabili dagli utenti funzionali."],
        ["Esplorare i dati", ("Query builder, grafici e dashboard.", "aws"), ("Esplorazione e analisi guidata.", "qlik"), "Qlik offre un'esperienza più ricca e orientata all'analisi."],
        ["Metriche condivise", ("Vanno definite e governate nel modello dati.", "verify"), ("Vanno definite e governate nel modello e nel tenant.", "verify"), "La libertà dell'utente parte da metriche affidabili."],
        ["Nuove fonti e regole", ("Restano al team data engineering.", "aws"), ("Restano al team Talend/Qlik o a uno sviluppatore.", "qlik"), "Il self-service riguarda la dashboard, non la costruzione della pipeline."],
        ["File complessi e logiche custom", ("Ampia libertà di personalizzazione.", "aws"), ("Da provare sui casi ProSIGNAL.", "verify"), "È il test più importante per la scelta tecnica."],
        ["Prerequisito per partire", ("Serve un'infrastruttura nostra o del cliente disponibile e compatibile.", "verify"), ("Serve che il cliente accetti di portare i dati in cloud.", "verify"), "È una decisione di contesto, prima ancora che di prodotto."],
        ["Componente di gestione", ("Sì: infrastruttura, runtime, monitoraggio, backup e accessi.", "aws"), ("Non per la piattaforma cloud; restano tenant, licenze e governance.", "qlik"), "AWS richiede un layer operativo dedicato; Qlik Cloud riduce la gestione della piattaforma."],
        ["Gestione operativa", ("Più componenti da gestire.", "aws"), ("Più dipendenza da licenze e tenant.", "qlik"), "Trade-off tra controllo tecnico e semplicità di piattaforma."],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [29, 40, 40, 48], "FunctionalClevel")

    # 3. Delivery estimate
    ws = wb.add_worksheet("Delivery estimate")
    setup_sheet(
        ws,
        "Tempi | Pilot tecnico e implementazione riusabile",
        "Perimetro pilot tecnico: 1 caso d'uso, 1-2 fonti, 2-3 dashboard, dati campione e nessun hardening produttivo completo.",
        f,
        [31, 20, 20, 48],
    )
    rows = [
        ["Livello", "AWS", "Qlik", "Cosa può cambiare i tempi"],
        ["Pilot tecnico | prerequisiti pronti", "3-5 sett.", "2-4 sett.", "AWS: componenti riusabili e infrastruttura pronta. Qlik: tenant, licenze e connettori pronti."],
        ["Pilot tecnico | prerequisiti da completare", "5-7 sett.", "4-6 sett.", "AWS: setup da zero. Qlik: attivazioni, accessi o connettori da completare."],
        ["Perimetro", "1 caso / 1-2 fonti / 2-3 dashboard", "1 caso / 1-2 fonti / 2-3 dashboard", "Dati campione; validazione capability e prerequisiti; niente hardening produttivo completo."],
        ["Fuori perimetro", "Hardening e industrializzazione", "Hardening e industrializzazione", "Niente go-live produttivo completo, parallel run esteso o runbook operativo definitivo."],
        ["Prima implementazione riusabile", "7-13 sett. con riuso\n10-17 da zero", "6-11 sett. se pronto\n9-15 se da attivare", "Include perimetro più ampio, quality gate, UAT, riconciliazioni, go-live controllato e runbook."],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [34, 28, 28, 58], "DeliveryClevel")
    ws.write(10, 0, "Base di calcolo", f["section"])
    ws.merge_range(10, 1, 10, 3, "Il pilot tecnico serve a decidere; la prima implementazione riusabile è un livello successivo.", f["note"])

    # 4. Economics with figures
    ws = wb.add_worksheet("Economics")
    setup_sheet(
        ws,
        "Economics | Budget frame primo anno",
        "Costi diretti del primo anno per il POC interno; effort e supporto del team non sono valorizzati.",
        f,
        [30, 20, 20, 58],
    )
    rows = [
        ["Voce", "AWS", "Qlik", "Cosa comprende / da cosa dipende"],
        ["Effort persone interno", "Escluso", "Escluso", "Il POC è interno: il tempo del team non entra nel budget."],
        ["Cloud / subscription 12 mesi", "=Assumptions!C8", "=Assumptions!C9", "AWS: EC2, RDS e S3. Qlik: subscription base da 30k EUR."],
        ["Run e supporto interno", "Escluso", "Escluso", "Gestione interna; non valorizzata nel POC."],
        ["Costi diretti primo anno", "=SUM(B5:B7)", "=SUM(C5:C7)", "AWS €5k cloud; Qlik €30k subscription. Effort interno escluso."],
    ]
    for c, header in enumerate(rows[0]):
        ws.write(3, c, header, f["header"])
    for r, row in enumerate(rows[1:], 4):
        for c, value in enumerate(row):
            if c in (1, 2) and isinstance(value, str) and value.startswith("="):
                cached = {1: 5000, 2: 30000}[c]
                ws.write_formula(r, c, value, f["money"], cached)
            elif c in (1, 2) and value == "Escluso":
                ws.write(r, c, value, f["assumption"])
            else:
                fmt = f["body_alt"] if (r - 3) % 2 == 0 else f["body"]
                ws.write(r, c, value, fmt)
    ws.set_row(3, 30)
    for r in range(4, 8):
        ws.set_row(r, 52)
    for c, width in enumerate([30, 20, 20, 58]):
        ws.set_column(c, c, width)
    ws.add_table(3, 0, 7, 3, {"name": "EconomicsClevel", "style": "Table Style Medium 2", "columns": [{"header": h} for h in rows[0]]})
    ws.write(10, 0, "Non incluso", f["section"])
    ws.merge_range(10, 1, 10, 3, "Restano fuori IVA, sconti, add-on, SLA premium, evolutive, migrazione estesa e change management.", f["assumption"])

    # 5. Assumptions
    ws = wb.add_worksheet("Assumptions")
    setup_sheet(
        ws,
        "Assumptions | Base usata per tempi ed economics",
        "Le voci sotto spiegano i costi diretti; l'effort del team interno resta fuori budget.",
        f,
        [8, 46, 22, 27, 58],
    )
    rows = [
        ["ID", "Voce", "Valore", "Unità", "Perché serve"],
        ["A1", "Rate delivery", "Non applicato", "POC interno", "L'effort del team non entra nel budget."],
        ["A2", "Effort AWS", 110, "person-days", "Dimensionamento tecnico della delivery; non valorizzato economicamente."],
        ["A3", "Effort Qlik", 80, "person-days", "Dimensionamento tecnico della delivery; non valorizzato economicamente."],
        ["A4", "Costo cloud AWS", (5000, "money"), "EUR / 12 mesi", "2 EC2 t3.medium always-on, 1 RDS db.t4g.medium, 100 GB DB, 1 TB S3 medio, backup/log/egress inclusi come buffer."],
        ["A5", "Subscription Qlik", (30000, "money"), "EUR / 12 mesi", "Subscription base 50 GB; capability Talend da verificare."],
        ["A6", "Run e supporto", "Interno", "non valorizzato", "Gestione interna; esclusa dai costi diretti del POC."],
        ["A7", "Rate run e supporto", "Non applicato", "POC interno", "Non serve per il budget del POC."],
        ["A8", "Perimetro pilot tecnico", "1 caso / 1-2 fonti / 2-3 dashboard", "scope ristretto", "È il perimetro usato per il pilot decisionale."],
        ["A9", "Configurazione AWS", "2 EC2 / 1 RDS", "architettura", "Sizing usato nel budget; ECS/EC2 e DB cliente restano da scegliere."],
        ["A10", "Storage e retention", "1 TB / lifecycle 90 gg", "storage", "Corrisponde allo scenario di landing/raw e storico."],
        ["A11", "Periodo Qlik", "12 mesi", "licenza", "Serve per rendere comparabile il budget del primo anno."],
        ["A12", "Perimetro prima implementazione riusabile", "1 caso / 5 fonti / 6 dashboard", "scope esteso", "Spiega i tempi più lunghi; non è il perimetro del pilot tecnico."],
    ]
    write_table(ws, 3, rows[0], rows[1:], f, [8, 46, 22, 27, 58], "AssumptionsClevel")
    ws.set_column("C:C", 18)
    ws.set_row(3, 30)
    for r in range(4, 16):
        ws.set_row(r, 42)
    ws.write(16, 0, "Da validare", f["section"])
    ws.merge_range(17, 1, 17, 4, "Restano da raccogliere: fonti e volumi reali, frequenza run, retention, SLA, utenti Qlik, capability Talend e criteri di UAT.", f["verify"])

    wb.close()
    print(OUT)


if __name__ == "__main__":
    build()
