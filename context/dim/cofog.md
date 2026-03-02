# Offentlige udgifter efter formål (COFOG) (cofog)

COFOG er en klassifikation af det offentliges udgifter fordelt efter formål. COFOG anvendes således til at danne et overblik over, hvad de offentlige udgiftskroner bruges til og dermed de overordnede udgiftsmæssige prioriteringer, inden for offentlig forvaltning og service.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 10
2 | Gruppe | 69
3 | Undergruppe | 109

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
1 | Generelle offentlige tjenester
2 | Forsvar
3 | Offentlig orden og sikkerhed
4 | Økonomiske anliggender
5 | Miljøbeskyttelse
6 | Boliger og offentlige faciliteter
7 | Sundhedsvæsen
8 | Fritid, kultur og religion
9 | Undervisning
10 | Social beskyttelse

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Generelle offentlige tjenester | NULL
11 | 2 | Udøvende og lovgivende organer, skatte- og finansvæsen, udenrigstjenesten | 1
111 | 3 | Udøvende og lovgivende organer (Kollektive tjenesteydelse) | 11

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.obesk1 f
JOIN dim.cofog d ON f.cofog = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.obesk1 f
  JOIN dim.cofog detail ON f.cofog = detail.kode AND detail.niveau = 3
  JOIN dim.cofog mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.cofog top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
