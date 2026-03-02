# Socioøkonomisk status (socio)

Den socioøkonomiske klassifikation (SOCIO13) dannes som hovedregel ud fra oplysninger om den væsentligste indkomstkilde eller beskæftigelse for personen. Ud fra indkomstkilden fastlægges, om personen er selvstændig erhvervsdrivende, medarbejdende ægtefælle, lønmodtager, arbejdsløs, eller uden for arbejdsstyrken, herunder pensionist, kontanthjælpsmodtager (inkl. kontanthjælpsmodtagere i aktivering) eller uddannelsessøgende. SOCIO13 afløste SOCIO02 i 2014 og dækker perioden fra 1991 og frem.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 4
2 | Gruppe | 10
3 | Undergruppe | 21

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
1 | Erhvervsaktive
2 | Midlertidigt ikke erhvervsaktive
3 | Ikke erhvervsaktive
4 | Andre og børn

## Niveau 2 — Gruppe

kode | titel | parent_kode
--- | --- | ---
11 | Selvstændige | 1
12 | Medarbejdende ægtefælle | 1
13 | Lønmodtagere | 1
21 | Arbejdsløs mindst halvdelen af året | 2
22 | Sygedagpenge, orlov mv. | 2
31 | Uddannelsessøgende | 3
32 | Pensionist/efterløn | 3
33 | Kontanthjælp | 3
41 | Andre | 4
42 | Børn | 4

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Erhvervsaktive | NULL
11 | 2 | Selvstændige | 1
110 | 3 | Selvstændige | 11

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.afsta3 f
JOIN dim.socio d ON f.socio = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.afsta3 f
  JOIN dim.socio detail ON f.socio = detail.kode AND detail.niveau = 3
  JOIN dim.socio mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.socio top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
