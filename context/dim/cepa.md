# Miljøbeskyttelsesformål (CEPA) (cepa)

Miljøbeskyttelsesaktiviteter (CEPA) anvendes til at klassificere udgifter og indtægter på aktiviteter, hvis primære formål er miljøbeskyttelse.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 9
2 | Gruppe | 46
3 | Undergruppe | 20

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
1 | Beskyttelse af luft og klima
2 | Spildevandshåndtering
3 | Affaldshåndtering
4 | Beskyttelse af jord, grundvand og overfladevand
5 | Støj- og vibrationsbekæmpelse
6 | Beskyttelse af biodiversitet og landskab
7 | Beskyttelse mod stråling
8 | Forskning og udvikling
9 | Andre miljøbeskyttelsesaktiviteter

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Beskyttelse af luft og klima | NULL
11 | 2 | Forebyggelse af forurening gennem ændringer i processen | 1
111 | 3 | til beskyttelse af luften | 11

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.cepa d ON f.cepa = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.cepa detail ON f.cepa = detail.kode AND detail.niveau = 3
  JOIN dim.cepa mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.cepa top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
