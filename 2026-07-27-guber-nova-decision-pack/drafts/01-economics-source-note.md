# NOVA Guber — nota fonti e assunzioni economics

## Uso corretto

Gli importi del deck sono **range di pianificazione**, non preventivi. Il TCO di piattaforma a tre anni è calcolato come:

`una tantum + 36 × costo mensile ricorrente`

Il canone Application Maintenance Novigo e l'eventuale costo di un team operativo sostitutivo restano separati per evitare doppio conteggio.

## Carico di riferimento

- produzione: 4–8 vCPU, 16–32 GB RAM, operatività 24x7 e alta disponibilità;
- non produzione: un ambiente al 50% della produzione;
- database: 500 GB iniziali, crescita del 20% annuo;
- documentale: 1 TB iniziale;
- backup: 30 giorni;
- DR geografico e licenze proprietarie: non inclusi.

Queste sono assunzioni di lavoro del decision pack e devono essere sostituite con dati NOVA e contratti Guber.

## Verifica AWS — Francoforte

La verifica è stata eseguita sul listino AWS ufficiale della regione **Europe (Frankfurt), `eu-central-1`**, pubblicato il 27 luglio 2026.

Come controllo di coerenza, per Amazon RDS Multi-AZ il listino riporta:

| Motore e taglia di riferimento | Prezzo orario USD | Equivalente mensile indicativo a 730 ore |
|---|---:|---:|
| PostgreSQL `db.m6i.xlarge` | 0,848 | 619 |
| PostgreSQL `db.m6i.2xlarge` | 1,696 | 1.238 |
| MySQL `db.m6i.xlarge` | 0,812 | 593 |
| MySQL `db.m6i.2xlarge` | 1,624 | 1.186 |

Il calcolo mensile sopra copre soltanto il compute database di produzione. Il range del deck include anche ambiente non produttivo, storage, backup, logging, networking e componenti di sicurezza. Per questo il range AWS complessivo di **€ 1,65k–5,2k/mese** è mantenuto come envelope prudenziale, con confidenza bassa finché non saranno noti motore, versione, licensing, carico e sconti contrattuali.

Per una conversione orientativa è stato considerato il cambio di riferimento BCE del 24 luglio 2026, pari a **1 EUR = 1,1377 USD**. Il cambio è informativo e non rappresenta un tasso di transazione.

## Range normalizzati nel deck

| Scenario | Una tantum | Piattaforma mensile | TCO piattaforma 3 anni |
|---|---:|---:|---:|
| Infrastruttura attuale | € 15k–38k | € 0,7k–2,4k | € 40k–124k |
| Azure Guber | € 49k–128k | € 1,75k–5,3k | € 112k–319k |
| AWS Guber, Francoforte | € 49k–128k | € 1,65k–5,2k | € 108k–315k |
| On-premise Guber | € 71k–208k | € 1,4k–4,5k | € 121k–370k |
| Primario attuale + replica on-premise Guber | € 25k–64k | € 0,9k–3,2k | € 57k–179k |
| Primario attuale + replica Azure Guber | € 25k–64k | € 0,9k–3,2k | € 57k–179k |

I due scenari di replica usano deliberatamente lo stesso envelope del materiale sorgente: non ci sono dati sufficienti per attribuire un differenziale difendibile tra Azure e on-premise. Cambiano i driver da validare, non il range preliminare.

## Esclusioni e sensibilità

Non sono inclusi:

- AM Novigo;
- team Guber o terza parte alternativo all'AM;
- licenze database, sistema operativo, virtualizzazione o backup non note;
- DR geografico;
- costi interni Guber;
- IVA;
- sconti, commitment o accordi enterprise.

Le variabili con maggiore sensibilità sono: motore e versione DB, compatibilità PaaS, HA/DR, volumi e crescita, IOPS, egress, capacità on-premise già disponibile e licensing.

## Fonti autorevoli

- AWS Price List Bulk API, struttura e uso dei file di offerta: <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/reading-service-price-list-file-for-services.html>
- AWS Price List per Amazon RDS, `eu-central-1`: <https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/current/eu-central-1/index.json>
- BCE, tassi di cambio di riferimento dell'euro: <https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.it.html>

