## Slide 1
DECISION PACK
NOVA — alternative infrastrutturalie modelli operativi
Confronto preliminare per Guber
31 luglio 2026
Range di pianificazione

## Slide 2
CONTESTO / ESIGENZA / OBIETTIVI
Il perimetro combina accesso ai dati, controllo e continuità
La replica read-only presso Guber è considerata accettabile; la scelta della collocazione resta aperta.
01
Contesto
Guber richiede accesso SQL ai dati NOVA per verifiche ed estrazioni.
02
Esigenza
Rendere i dati accessibili senza compromettere operatività, sicurezza e responsabilità.
03
Obiettivo
Confrontare sei alternative di collocazione e gestione, senza anticipare la scelta.
Punto fermo: l'accesso ai dati è confermato; la necessità di migrare il database primario non è ancora dimostrata.

## Slide 3
AS IS
Oggi NOVA concentra dati e operatività sull'ambiente corrente
Il requisito SQL è chiaro; dimensionamento e vincoli infrastrutturali devono ancora essere validati.
Sorgenti
ODT · AV · LDT
NOVA
History e consolidamento
Database primario
Operatività applicativa
Guber
Verifiche ed estrazioni SQL
Fatto confermato
•  Accesso SQL richiesto | •  Replica read-only accettata | •  AM Novigo end-to-end disponibile
Da proteggere
•  Disponibilità del transazionale | •  History e riconciliazione | •  Accessi, audit e segregazione
Dati mancanti
•  Motore, sizing e licensing | •  SLA, RPO/RTO e rete | •  Standard cloud e capacità Guber

## Slide 4
ALTERNATIVE
Sei alternative separano due scelte: collocare il primario o la replica
La mappa evita di confondere il requisito di accesso ai dati con una migrazione completa della piattaforma.
COME SODDISFARE IL REQUISITO?
COLLOCAZIONE DEL PRIMARIO
PRIMARIO ATTUALE + REPLICA
01
Infrastruttura attuale
Continuità e cambiamento minimo
02
Primario su Azure Guber
Ownership Guber e governance Azure
03
Primario su AWS Guber
Ownership Guber e target AWS Francoforte
04
Primario on-premise Guber
Controllo infrastrutturale diretto
05
Replica on-premise Guber
Replica read-only presso Guber
06
Replica su Azure Guber
Replica read-only presso Guber

## Slide 5
SCENARIO 01
Infrastruttura attuale: continuità e cambiamento minimo
Profilo preliminare; fattibilità e costo dipendono dai gate tecnici indicati.
PRIMARIO
Guber
Accesso SQL governato
NOVA attuale
PUNTI DI FORZA
•  Tempi più rapidi | •  Rischio migrazione contenuto | •  Alta reversibilità
ATTENZIONI
•  Ownership Guber limitata | •  Accesso da segregare | •  Dipendenza dall'ambiente corrente
GATE DA VALIDARE
•  Viste / schema read-only | •  Audit e capacità | •  SLA operativo
UNA TANTUM
€ 15k–38k
PIATTAFORMA / MESE
€ 0,7k–2,4k
TCO PIATTAFORMA · 3 ANNI
€ 40k–124k
Range di pianificazione · AM Novigo, team sostitutivo, licenze non note e DR geografico esclusi.

## Slide 6
SCENARIO 02
Primario su Azure Guber: ownership guber e governance azure
Profilo preliminare; fattibilità e costo dipendono dai gate tecnici indicati.
PRIMARIO
Utenti / sistemi
Azure Guber
DB NOVA primario
PUNTI DI FORZA
•  Account e chiavi Guber | •  Elasticità | •  PaaS se compatibile
ATTENZIONI
•  Migrazione del primario | •  Dipendenza dalla rete | •  Run da assegnare
GATE DA VALIDARE
•  Landing zone | •  Compatibilità DB | •  Networking privato
UNA TANTUM
€ 49k–128k
PIATTAFORMA / MESE
€ 1,75k–5,3k
TCO PIATTAFORMA · 3 ANNI
€ 112k–319k
Range di pianificazione · AM Novigo, team sostitutivo, licenze non note e DR geografico esclusi.

## Slide 7
SCENARIO 03
Primario su AWS Guber: ownership guber e target aws francoforte
Profilo preliminare; fattibilità e costo dipendono dai gate tecnici indicati.
PRIMARIO
Utenti / sistemi
AWS eu-central-1
DB NOVA primario
PUNTI DI FORZA
•  Account e chiavi Guber | •  Servizi gestiti | •  Coerenza con S3
ATTENZIONI
•  Migrazione del primario | •  Compatibilità RDS | •  Responsabilità operative
GATE DA VALIDARE
•  Standard AWS Guber | •  VPC e connettività | •  Motore / licensing
UNA TANTUM
€ 49k–128k
PIATTAFORMA / MESE
€ 1,65k–5,2k
TCO PIATTAFORMA · 3 ANNI
€ 108k–315k
Range di pianificazione · AM Novigo, team sostitutivo, licenze non note e DR geografico esclusi.

## Slide 8
SCENARIO 04
Primario on-premise Guber: controllo infrastrutturale diretto
Profilo preliminare; fattibilità e costo dipendono dai gate tecnici indicati.
PRIMARIO
Utenti / sistemi
Data center Guber
DB NOVA primario
PUNTI DI FORZA
•  Ownership Guber | •  Integrazione con rete interna | •  Controllo diretto
ATTENZIONI
•  Capacità e licensing | •  HA / DR | •  Carico operativo
GATE DA VALIDARE
•  Infrastruttura disponibile | •  Competenze | •  Backup e secondo sito
UNA TANTUM
€ 71k–208k
PIATTAFORMA / MESE
€ 1,4k–4,5k
TCO PIATTAFORMA · 3 ANNI
€ 121k–370k
Range di pianificazione · AM Novigo, team sostitutivo, licenze non note e DR geografico esclusi.

## Slide 9
SCENARIO 05
Replica on-premise Guber: autonomia sui dati senza spostare il transazionale
Profilo preliminare; fattibilità e costo dipendono dai gate tecnici indicati.
REPLICA
Primario attuale
Replica asincrona
On-premise Guber
PUNTI DI FORZA
•  Migrazione contenuta | •  Accesso locale | •  Alta reversibilità
ATTENZIONI
•  Lag e riconciliazione | •  Ownership divisa | •  Compatibilità replica
GATE DA VALIDARE
•  Motore / licenze | •  Frequenza e SLA | •  Viste e monitoring
UNA TANTUM
€ 25k–64k
PIATTAFORMA / MESE
€ 0,9k–3,2k
TCO PIATTAFORMA · 3 ANNI
€ 57k–179k
Range di pianificazione · AM Novigo, team sostitutivo, licenze non note e DR geografico esclusi.

## Slide 10
SCENARIO 06
Replica su Azure Guber: accesso governato ai dati con servizi azure
Profilo preliminare; fattibilità e costo dipendono dai gate tecnici indicati.
REPLICA
Primario attuale
Replica asincrona
Azure Guber
PUNTI DI FORZA
•  Autonomia sui dati | •  Identity e audit Azure | •  Scalabilità
ATTENZIONI
•  Connettività cross-environment | •  Lag ed egress | •  Compatibilità replica
GATE DA VALIDARE
•  Subscription e rete privata | •  Replica supportata | •  Retention
UNA TANTUM
€ 25k–64k
PIATTAFORMA / MESE
€ 0,9k–3,2k
TCO PIATTAFORMA · 3 ANNI
€ 57k–179k
Range di pianificazione · AM Novigo, team sostitutivo, licenze non note e DR geografico esclusi.

## Slide 11
MODELLO OPERATIVO
Il run operativo resta una scelta trasversale a tutti gli scenari
Ownership di account e chiavi non implica che Guber debba eseguire direttamente tutte le attività operative.
AM NOVIGO END-TO-END
•  Un presidio operativo coordinato | •  Applicazione, database e infrastruttura | •  Monitoring, backup, patching e sicurezza | •  Incident, capacity e release management | •  Accessi delegati e tracciati
GUBER / TERZA PARTE
•  Maggiore autonomia di sourcing | •  Competenze e copertura da garantire | •  Handover e documentazione operativa | •  Rischio di responsabilità frammentate | •  Coordinamento multi-fornitore
In entrambi i modelli servono RACI, SLA, key ownership, audit ed exit plan.

## Slide 12
ECONOMICS
I range delimitano il confronto, ma non sostituiscono il sizing
TCO piattaforma = una tantum + 36 mesi; Application Maintenance valorizzata separatamente.
AWS verificato su Francoforte, eu-central-1
AM e team sostitutivo esclusi
Licenze non note e DR geografico esclusi
Confidenza bassa fino al sizing reale

## Slide 13
CONFRONTO
La matrice evidenzia trade-off differenti, non un vincitore
Lettura qualitativa preliminare: da rivedere dopo la verifica dei gate tecnici e degli standard Guber.
Valutazione preliminare: standard Guber, compatibilità del motore e capacità on-premise possono modificare il posizionamento.

## Slide 14
SINTESI
Le alternative restano aperte; cambiano le informazioni necessarie
Il deck presenta tre famiglie di scelta senza attribuire oggi una preferenza.
CONTINUITÀ
Scenario 1
Mantenere il primario sull'ambiente corrente
TRASFERIMENTO DEL PRIMARIO
Scenari 2–4
Azure, AWS oppure on-premise Guber
ACCESSO DATI SENZA MIGRAZIONE
Scenari 5–6
Replica on-premise oppure Azure Guber
INFORMAZIONI CHE RIDUCONO L'INCERTEZZA
Motore e sizing
Standard cloud
Capacità on-premise
SLA / RPO / RTO
Connettività
Licensing
Modello operativo

## Slide 15
APPENDICE
APPENDICE
Assunzioni, economics eapprofondimenti tecnici
Materiale di supporto — range preliminari

## Slide 16
APPENDICE | GROUNDING
Fatti, deduzioni e dati mancanti restano separati
FATTI CONFERMATI
•  Accesso SQL richiesto | •  Replica read-only accettata | •  Azure e on-premise in agenda | •  AWS aggiunto su conferma utente | •  AM Novigo end-to-end
DEDUZIONI DICHIARATE
•  Migrare il primario non è l'unico modo | •  La replica riduce il rischio sul transazionale | •  DB remoto rende la rete parte dell'architettura | •  Key ownership è una scelta di governance
DATI MANCANTI
•  Motore, versione e licensing | •  Sizing, crescita e IOPS | •  SLA, RPO / RTO e downtime | •  Landing zone e connettività | •  Capacità on-premise e contratti

## Slide 17
APPENDICE | ECONOMICS
Il modello economico usa un carico di riferimento esplicito
Le assunzioni rendono comparabili gli scenari, ma non sostituiscono i dati NOVA.
NON INCLUSO
•  AM Novigo | •  Team sostitutivo | •  Licenze non note | •  DR geografico | •  Costi interni Guber | •  IVA e sconti contrattuali

## Slide 18
APPENDICE | SCENARIO 01
Infrastruttura attuale — struttura del range economico
Componenti indicative da ricalcolare dopo assessment e sizing.
UNA TANTUM
•  Assessment e hardening | •  Accesso SQL / viste | •  Audit e test | •  Documentazione
RICORRENTE
•  Capacità incrementale | •  Backup e logging | •  Monitoring | •  Networking
SENSIBILITÀ
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi, crescita e IOPS | •  Licenze e contratti
Una tantum  € 15k–38k
Mensile  € 0,7k–2,4k
TCO 3 anni  € 40k–124k

## Slide 19
APPENDICE | SCENARIO 02
Primario su Azure Guber — struttura del range economico
Componenti indicative da ricalcolare dopo assessment e sizing.
UNA TANTUM
•  Assessment PaaS / IaaS | •  Landing zone e rete | •  Migrazione e test | •  Cutover e rollback
RICORRENTE
•  Compute / database | •  Storage e backup | •  Logging e security | •  Networking
SENSIBILITÀ
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi, crescita e IOPS | •  Licenze e contratti
Una tantum  € 49k–128k
Mensile  € 1,75k–5,3k
TCO 3 anni  € 112k–319k

## Slide 20
APPENDICE | SCENARIO 03
Primario su AWS Guber — struttura del range economico
Componenti indicative da ricalcolare dopo assessment e sizing.
UNA TANTUM
•  Assessment RDS / EC2 | •  Landing zone e VPC | •  Migrazione e test | •  Cutover e rollback
RICORRENTE
•  RDS / EC2 | •  Storage e backup | •  CloudWatch / security | •  Networking
SENSIBILITÀ
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi, crescita e IOPS | •  Licenze e contratti
Una tantum  € 49k–128k
Mensile  € 1,65k–5,2k
TCO 3 anni  € 108k–315k

## Slide 21
APPENDICE | SCENARIO 04
Primario on-premise Guber — struttura del range economico
Componenti indicative da ricalcolare dopo assessment e sizing.
UNA TANTUM
•  Assessment e capacity | •  Provisioning e licensing | •  Migrazione e test | •  HA, backup e cutover
RICORRENTE
•  Capacità e manutenzione | •  Backup | •  Monitoring | •  Energia / data center
SENSIBILITÀ
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi, crescita e IOPS | •  Licenze e contratti
Una tantum  € 71k–208k
Mensile  € 1,4k–4,5k
TCO 3 anni  € 121k–370k

## Slide 22
APPENDICE | SCENARIO 05
Replica on-premise Guber — struttura del range economico
Componenti indicative da ricalcolare dopo assessment e sizing.
UNA TANTUM
•  Assessment replica | •  Provisioning on-premise | •  Setup e riconciliazione | •  Accessi e monitoring
RICORRENTE
•  Compute / database replica | •  Storage e backup | •  Monitoring del lag | •  Connettività
SENSIBILITÀ
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi, crescita e IOPS | •  Licenze e contratti
Una tantum  € 25k–64k
Mensile  € 0,9k–3,2k
TCO 3 anni  € 57k–179k

## Slide 23
APPENDICE | SCENARIO 06
Replica su Azure Guber — struttura del range economico
Componenti indicative da ricalcolare dopo assessment e sizing.
UNA TANTUM
•  Assessment replica | •  Subscription e rete | •  Setup e riconciliazione | •  Accessi e monitoring
RICORRENTE
•  Database replica | •  Storage e backup | •  Monitor e audit | •  Rete / egress
SENSIBILITÀ
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi, crescita e IOPS | •  Licenze e contratti
Una tantum  € 25k–64k
Mensile  € 0,9k–3,2k
TCO 3 anni  € 57k–179k

## Slide 24
APPENDICE | SICUREZZA
Account, chiavi e run possono avere ownership differenti
ACCOUNT E INFRASTRUTTURA
Guber
CHIAVI E POLICY
Guber / doppio controllo
RUN OPERATIVO
Novigo oppure Guber / terzo
AUDIT E GOVERNANCE
Guber
CONTROLLO MINIMO COMUNE
•  TLS e cifratura a riposo · accesso privato · MFA e federation · logging e SIEM · backup protetti · rotazione e revoca delle chiavi

## Slide 25
APPENDICE | STORAGE
La tecnologia di storage dipende dal requisito, non dal nome del provider
Prima di scegliere S3 va chiarito se il requisito è AWS-specifico o genericamente object storage.
AWS S3
•  Coerenza con AWS | •  Lifecycle e versioning | •  Valutare egress e KMS
AZURE STORAGE
•  Coerenza con Azure | •  Identity e policy | •  Valutare tier e rete
OBJECT STORAGE ON-PREMISE
•  Controllo locale | •  Capacity e operations | •  Durabilità da progettare
Criteri comuni: volume e crescita · access pattern · retention · immutabilità · cifratura · data residency · costo di trasferimento.

## Slide 26
APPENDICE | ORCHESTRATORE
Separare database e orchestratore rende la rete parte dell'architettura
DB-ONLY
Il database migra o replica; applicazione e orchestratore restano dove sono.
Più rapido
Dipendenza WAN
PHASED
Replica o DB come prima fase; componenti spostati dopo verifica.
Rischio progressivo
Transitorio da governare
FULL-STACK
Applicazione, database e orchestratore migrano insieme.
Coerenza target
Scope e cutover maggiori
Un'architettura DB-only può essere una fase controllata; non deve diventare implicitamente un target fragile.

## Slide 27
APPENDICE | DEPLOYMENT DB
PaaS o IaaS è un gate di compatibilità, non un dettaglio implementativo
SERVIZIO GESTITO · PaaS / RDS
•  Patching e backup maggiormente gestiti | •  HA e monitoring standardizzati | •  Minor carico operativo | •  Compatibilità del motore da verificare | •  Vincoli e feature specifiche del servizio
VM / EC2 · SELF-MANAGED
•  Maggiore compatibilità e controllo | •  Responsabilità DBA e sistema operativo | •  Backup, HA e patching da costruire | •  TCO operativo più elevato | •  Licensing da verificare
PRIMO GATE: MOTORE · VERSIONE · FEATURE · LICENZE

## Slide 28
APPENDICE | RACI
Il modello di run deve coprire l'intero servizio, non soltanto l'applicazione

## Slide 29
APPENDICE | APPROFONDIMENTO
Un eventuale approfondimento può ridurre l'incertezza in quattro passaggi
Sequenza indicativa, non obiettivo immediato né impegno di progetto.
01
Assessment
1–2 settimane
Motore, sizing, licenze e compatibilità
02
Economics
1 settimana
TCO, contratti e modello AM
03
Prova tecnica
2–4 settimane
Replica o migrazione pilota
04
Piano di transizione
Da definire
Cutover, rollback, RACI e SLA
L'attivazione del percorso dipende dalla successiva scelta di approfondire una o più alternative.