# NOVA Guber — creative handoff

## Intento

Creare un decision pack C-level neutrale, leggibile in pochi minuti e coerente con il linguaggio visivo TXT/Novigo. Il deck deve presentare alternative, non raccomandare una soluzione.

## Guardrail

- formato 16:9, font Poppins;
- palette e asset del template aziendale;
- titoli assertivi e sintetici;
- testo editabile, non rasterizzato;
- economics e confronto in tabelle;
- diagrammi semplici con forme PowerPoint;
- massimo 3–4 messaggi per area;
- nessuna precisione economica oltre i range;
- distinguere fatti, assunzioni e gate;
- non copiare contenuti cliente dai deck di riferimento.

## Famiglie visuali

- cover istituzionale con ampio spazio bianco e motivo geometrico leggero;
- `Contesto / Esigenza / Obiettivi` in tre blocchi numerati;
- AS IS come flusso essenziale;
- mappa scenari come albero `primario / replica`;
- scenario card con architettura minima, pro, attenzioni, gate e fascia TCO;
- modello operativo come due colonne comparabili;
- economics come tabella compatta;
- matrice qualitativa come heatmap discreta;
- sintesi finale come tre famiglie di scelta e lista dei dati da validare.

## Libertà per slide

| Slide | Libertà | Vincolo principale |
|---|---|---|
| 1 | Low | cover coerente con template |
| 2 | Low | pattern Contesto / Esigenza / Obiettivi |
| 3 | Medium | AS IS leggibile a colpo d'occhio |
| 4 | Medium | separare migrazione primario e replica |
| 5–10 | Medium | stessa grammatica visuale per comparabilità |
| 11 | Medium | due modelli operativi, nessun vincitore |
| 12 | Low | tabella economics e note di perimetro |
| 13 | Low | matrice omogenea, scale dichiarate |
| 14 | Medium | chiusura neutrale, nessuna call to action immediata |
| Appendice | Medium | densità superiore ma leggibile |

## Fallback visuale

Prima scelta: forme, tabelle e testi PowerPoint modificabili.

Se un visual complesso non raggiunge la qualità aziendale:

1. usare un'immagine generata solo per illustrazioni o sfondi senza testo;
2. in alternativa inserire un placeholder chiaramente etichettato;
3. salvare il prompt completo in `prompts/visual-placeholder-prompts.md`.

Non usare immagini per economics, matrici, checklist o testo sostanziale.

## Anti-pattern

- slide-documento;
- diagrammi tecnici con troppe connessioni;
- icone decorative senza funzione;
- semafori che implicano una raccomandazione;
- ranking complessivo non supportato;
- costi presentati come preventivi;
- roadmap percepita come impegno già concordato.

