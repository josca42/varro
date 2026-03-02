table: fact.off25
description: Offentlig forvaltning og service, funktionel fordeling af udgiftstyper (krydsfordeling) efter funktion, udgiftstype og tid
measure: indhold (unit Mio. kr.)
columns:
- funktion: join dim.cofog on funktion=kode::text [approx]; levels [1]
- udtype: values [1.1=1.1. Aflønning af ansatte, 1.2=1.2. Forbrug i produktionen, 1.3=1.3. Andre produktionsskatter, 1.4=1.4. Sociale ydelser i naturalier, 1.5=1.5. Renter mv. ... 1.14.3=1.14.3. Til andre indenlandske sektorer, 1.14.4=1.14.4. Til udland, 1.15=1.15. Kapitaloverførsler i alt, 1.16=1.16. Kapitaludgifter i alt (13+14), 1.17=1.17. Drifts- og kapitaludgifter i alt (8+16)]
- tid: date range 1998-01-01 to 2024-01-01
dim docs: /dim/cofog.md
notes:
- funktion uses the same dotted COFOG notation as off29 (77 values: TOTAL, 1–10, 1.1–10.9). The same dim.cofog join transforms apply: niveau=1 codes '1'–'10' join directly; niveau=2 codes like '1.1' need REPLACE(funktion, '.', '') to match dim kode '11'. See off29 notes for join SQL.
- udtype is a hierarchical expenditure-type column (same codes as ui in off3): 1.17=Drifts- og kapitaludgifter i alt is the grand total; sub-codes are components. Don't mix hierarchy levels when summing.
- This is a cross-tabulation — each row gives expenditure of type udtype for COFOG function funktion. Summing across all udtype values double-counts because parent codes aggregate child codes.
