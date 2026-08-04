# Decision recap AWS / Qlik

## Scope

Questo pacchetto risponde al feedback finale sulla v5 senza modificare il PPTX:

- quale soluzione può essere usata da utenti funzionali non sviluppatori per creare dashboard;
- quali sono i principali trade-off funzionali/business;
- quali tempi indicativi usare per un primo pilot;
- quali costi sono noti, quali sono solo baseline e quali restano da stimare.

**Disclaimer:** tempi, dimensionamenti ed economics derivano dalle assunzioni riportate nel workbook; non costituiscono un commitment di delivery né un'offerta commerciale.

## Risposta executive

Entrambe le alternative possono supportare dashboard self-service su dati e modelli già pubblicati.

- **Qlik:** candidato più diretto per il requisito di analytics self-service e di esplorazione da parte dell'utente business; la lettura è comparativa e va validata su tenant, licenza, modello dati e utenti reali.
- **AWS / Metabase:** utilizzabile per dashboard, query, metriche, alert ed export; richiede una maggiore preparazione del modello dati, delle metriche e della governance da parte del team tecnico.
- **Gestione operativa:** AWS richiede anche un layer dedicato per infrastruttura, runtime, monitoraggio, backup e accessi; Qlik Cloud non richiede la stessa gestione della piattaforma, ma mantiene attività di tenant, licenze e governance.
- **Confine comune:** nuove fonti, regole di dominio, trasformazioni complesse, quality gate e governance applicativa restano in carico al team tecnico.

Il prerequisito di avvio è diverso: AWS dipende dalla disponibilità e compatibilità dell'infrastruttura nostra o del cliente; Qlik dipende dall'accettazione del cliente di portare i dati in cloud.

## Tempi e perimetro

I materiali di progetto dichiarano che il piano comune non contiene date, durate o effort. I valori sotto si riferiscono a un primo pilot; la definizione finale dipende da:

- caso pilota, fonti, output e numero di dashboard;
- volumi, frequenze, retention e requisiti di accesso;
- disponibilità di tenant/licenze/connettori Qlik/Talend;
- riuso della reference implementation AWS e disponibilità degli skill;
- criteri di UAT, riconciliazione, parallel run e go-live.

Valori utilizzati per il confronto:

- **Pilot tecnico / decision gate:** AWS 3-5 settimane con componenti riusabili e infrastruttura pronta; 5-7 settimane partendo da zero. Qlik 2-4 settimane con tenant, licenze e connettori pronti; 4-6 settimane se le attivazioni sono da completare.
- **Prima implementazione riusabile:** AWS 7-13 settimane con riuso; 10-17 settimane da zero. Qlik 6-11 settimane con piattaforma pronta; 9-15 settimane se attivazione e capability sono da verificare.

Il pilot tecnico presuppone 1 caso d'uso, 1-2 fonti, 2-3 dashboard, dati campione e nessun hardening produttivo completo. I range più lunghi includono invece 5 fonti, 6 dashboard, quality gate, UAT, riconciliazioni, go-live controllato e runbook.

## Assunzioni per gli economics

È stata usata la soglia inferiore della baseline utente: **30k EUR per un piano Qlik/Talend da 50 GB**. Non è listino Qlik e il periodo è da confermare.

Trattandosi di un POC interno, il budget considera solo i costi diretti incrementali:

- **AWS: €5k** per cloud/runtime;
- **Qlik: €30k** per subscription base di 12 mesi.

Delivery, run e supporto del team interno non sono valorizzati né inclusi nei totali. L'effort resta riportato come dimensionamento tecnico, non come costo commerciale.

## Gate finale

- **Critic:** nessuna raccomandazione assoluta; assunzioni e prerequisiti sono espliciti; il requisito dashboard è separato dalla costruzione della pipeline.
- **Review:** il workbook contiene confronto funzionale, tempi, economics, assunzioni, punti aperti e fonti; le immagini seguono il pattern visivo della v5.
- **Humanize:** titoli e messaggi sono orientati alla decisione e non al tool; il testo evita di promettere autonomia totale.

## Output

- `Data pipeline comparison C-level v2.xlsx` (versione sintetica per il management)
- `attempts/archive/legacy-workbooks/Data pipeline comparison assumptions v1.xlsx` (versione dettagliata archiviata)
- `generated-assets/Slide recap 01 - dashboard utenti funzionali.png`
- `generated-assets/Slide recap 02 - confronto funzionale.png`
- `generated-assets/Slide recap 03 - tempi pilot.png`
- `generated-assets/Slide recap 04 - economics.png`
- `generated-assets/Slide recap 05 - dashboard interattive metabase qlik.png`
