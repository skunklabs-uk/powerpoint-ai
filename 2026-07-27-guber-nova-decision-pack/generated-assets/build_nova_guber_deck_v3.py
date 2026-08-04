from pathlib import Path

from pptx.enum.text import PP_ALIGN

import build_nova_guber_deck_v2 as base
from build_visual_prototype_v2 import box, bullets, connector, header, slide, textbox, title


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali v3.pptx"


def context_slide(prs):
    s = slide(prs)
    header(s, "NOVA", "Contesto, esigenza e obiettivi", 2)
    xline = 5.2
    connector(s, xline, 3.0, xline, 15.6, "teal", 1.1)

    rows = [
        (
            "Contesto",
            "NOVA opera oggi su OutSystems; il database è collocato nello stesso ambiente",
            "Novigo ha sviluppato NOVA per la gestione dei portafogli NPL. Parallelamente sta razionalizzando alcuni processi Guber che potrebbero evolvere in nuove automazioni basate sullo stesso patrimonio dati.",
        ),
        (
            "Esigenza",
            "Definire una collocazione dati coerente con NOVA e con le possibili evoluzioni",
            "La soluzione deve garantire accesso SQL governato, continuità, sicurezza e tracciabilità, valutando il possibile uso della stessa istanza database anche con schemi separati.",
        ),
        (
            "Obiettivi",
            "Confrontare sei alternative su criteri omogenei",
            "Il confronto considera collocazione del primario, replica read-only, modello operativo, rischio, reversibilità, capacità evolutiva ed economics.",
        ),
    ]

    for i, (label, lead, body) in enumerate(rows):
        y = 3.0 + i * 4.35
        textbox(s, 1.1, y + 0.3, 3.6, 0.4, label, 10, "dark_teal", True, PP_ALIGN.RIGHT)
        textbox(s, 6.2, y, 24.7, 0.75, lead, 11.4, "text", True)
        textbox(s, 6.2, y + 0.95, 24.7, 1.45, body, 9.2, "text")

    textbox(
        s,
        6.2,
        15.9,
        24.7,
        0.42,
        "Le automazioni e la condivisione dell'istanza sono possibilità da valutare, non decisioni già assunte.",
        7.8,
        "gray",
        False,
    )
    base.star(s)


def as_is_slide(prs):
    s = slide(prs)
    header(s, "NOVA", "Situazione attuale e possibile evoluzione", 3)
    title(s, "La collocazione del database deve supportare NOVA e le possibili automazioni future")
    textbox(
        s,
        0.8,
        2.4,
        31.0,
        0.45,
        "NOVA è realizzato con OutSystems; la razionalizzazione dei processi Guber può generare nuovi workload sullo stesso patrimonio dati.",
        9,
        "gray",
    )

    box(s, 0.9, 3.5, 16.0, 10.7, "white", "teal", True)
    textbox(s, 1.4, 3.9, 15.0, 0.4, "AS IS NOVA", 8, "dark_teal", True, PP_ALIGN.CENTER)
    nodes = [
        ("Processi NPL", "portafogli e operatività"),
        ("NOVA su OutSystems", "applicazione e logica"),
        ("Database primario", "ambiente OutSystems"),
    ]
    for i, (label, sub) in enumerate(nodes):
        y = 5.0 + i * 2.45
        base.architecture_node(s, 4.1, y, 9.6, label, sub, "pale_blue" if i == 1 else "white")
        if i < 2:
            connector(s, 8.9, y + 1.45, 8.9, y + 2.35)

    textbox(s, 18.3, 3.8, 12.0, 0.4, "EVOLUZIONE POSSIBILE", 9, "dark_teal", True)
    bullets(
        s,
        18.3,
        4.5,
        13.0,
        [
            "Razionalizzazione di alcuni processi Guber",
            "Possibili automazioni ancora da definire",
            "Riutilizzo ragionevole dello stesso patrimonio dati",
        ],
        9.3,
    )

    textbox(s, 18.3, 9.2, 12.0, 0.4, "IMPLICAZIONE ARCHITETTURALE", 9, "blue", True)
    bullets(
        s,
        18.3,
        9.9,
        13.0,
        [
            "Valutare una stessa istanza database con schemi separati",
            "Isolare workload applicativi, SQL e automazioni",
            "Definire ownership, accessi, capacità e responsabilità operative",
        ],
        9.3,
    )
    base.star(s)


def build():
    base.OUT = OUT
    base.context_slide = context_slide
    base.as_is_slide = as_is_slide
    base.build()


if __name__ == "__main__":
    build()
