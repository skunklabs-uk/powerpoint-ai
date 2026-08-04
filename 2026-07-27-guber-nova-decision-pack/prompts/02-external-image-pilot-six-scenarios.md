# Prompt pilota — mappa dei sei scenari NOVA

## Immagini da allegare

Allegare come reference visuali:

1. `visual-references/data-pipeline-v5-05-process-model.png`
2. `visual-references/data-pipeline-v5-10-comparison-model.png`
3. `visual-references/data-pipeline-v5-12-decision-criteria.png`

Le immagini servono esclusivamente come riferimento per stile, composizione, densità, tipografia, icone e sistema grafico. Non copiarne testi, nomi, loghi tecnologici o contenuti.

## Prompt da usare

Create a polished 16:9 executive PowerPoint slide image for a C-level presentation to Guber.

Use the attached slides as the primary visual reference. Match their information density, visual hierarchy, corporate whitespace, icon treatment, thin outlines, teal/blue palette, typography proportions, recurring top navigator and structured diagram quality. The result must feel like another slide from the same presentation family, not like a generic presentation template or a dashboard.

### Slide purpose

Explain six alternative infrastructure scenarios for the NOVA database. The slide must make immediately clear that there are two different strategies:

1. decide where the primary database resides;
2. keep the current primary database and provide Guber with a read-only replica.

Do not recommend or rank any scenario.

### Format and corporate structure

- 1920 × 1080, landscape, 16:9.
- White background.
- TXT/Novigo corporate header in the same style as the reference slides.
- Header text, verbatim: `NOVA | Le alternative di collocazione`
- Page number: `4`
- Thin teal line below the logo area and short blue line at the upper-right edge.
- Small recurring navigator in the upper-right:
  `PERCHÉ · ALTERNATIVE · MODELLO OPERATIVO · ECONOMICS · SINTESI`
- Highlight `ALTERNATIVE` as the current section.
- Small TXT/Novigo footer mark at the bottom.

### Main title

Use this exact title:

`Sei scenari, due strategie per rispondere al requisito dati`

Use this short supporting message:

`Il confronto distingue la collocazione del database primario dalla replica read-only presso Guber.`

### Main diagram

Create one central, information-rich decision diagram.

At the top centre place a compact node:

`REQUISITO GUBER`

Inside or immediately below it:

`Accesso SQL governato per verifiche ed estrazioni`

From this node create two clear branches.

#### Left branch

Branch title:

`COLLOCAZIONE DEL DATABASE PRIMARIO`

Create four vertically or horizontally coordinated scenario modules:

1. `01 · Infrastruttura attuale`
   - icon: current server environment;
   - ownership label: `Ambiente corrente`;
   - access label: `SQL governato`.

2. `02 · Primario su Azure Guber`
   - icon: Azure cloud;
   - ownership label: `Account e chiavi Guber`;
   - access label: `SQL sul primario`.

3. `03 · Primario su AWS Guber`
   - icon: AWS cloud;
   - ownership label: `Account e chiavi Guber`;
   - region label: `Francoforte`;
   - access label: `SQL sul primario`.

4. `04 · Primario on-premise Guber`
   - icon: Guber data centre;
   - ownership label: `Infrastruttura Guber`;
   - access label: `SQL sul primario`.

#### Right branch

Branch title:

`PRIMARIO ATTUALE + REPLICA READ-ONLY`

Show the current primary database once, connected through a visible replication flow to two alternatives:

5. `05 · Replica on-premise Guber`
   - icon: database replica in Guber data centre;
   - label: `Accesso SQL locale`;
   - label: `Primario invariato`.

6. `06 · Replica su Azure Guber`
   - icon: database replica in Azure;
   - label: `Identity e audit Azure`;
   - label: `Primario invariato`.

Use directional connectors that clearly show that scenarios 5 and 6 receive data from the current primary database. Add a small visual indicator for asynchronous replication, without introducing technical detail beyond the text provided.

### Bottom synthesis band

Create a light-blue or very pale teal horizontal band at the bottom with one small icon and this exact statement:

`Un unico requisito dati può essere soddisfatto trasferendo il primario oppure replicando i dati presso Guber.`

### Visual requirements

- Information-rich but readable in under 30 seconds.
- Use consistent, professional line icons.
- Use shapes, connectors, labels and visual grouping comparable to the attached reference slides.
- Use teal, blue, dark blue and pale blue; no large dark backgrounds.
- Use subtle coloured headers for the two branches.
- Maintain clear reading order and strong alignment.
- Use restrained rounded corners comparable to the references.
- Make the architecture and decision logic the visual focus.

### Text requirements

- Preserve every supplied Italian phrase exactly.
- Use correct accents and punctuation.
- Keep body text large enough to read in a presentation.
- Do not invent additional explanations.
- Do not introduce recommendations, scores, rankings, costs, risks, benefits, assumptions or calls to action.

### Avoid

- generic six-card dashboard;
- six identical floating boxes without relationships;
- sparse editorial slide;
- decorative illustrations;
- photorealistic imagery;
- 3D effects;
- excessive gradients or shadows;
- tiny text;
- invented logos;
- watermark;
- any text not explicitly supplied above.

