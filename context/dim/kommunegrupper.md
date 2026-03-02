# Kommunegrupper (kommunegrupper)

Med udgangspunkt i tilgængelighed til arbejdspladser og antallet af indbyggere i den største by i kommunen, er Danmarks kommuner grupperet i fem grupper:

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Kommunegruppe | 5
2 | Kommune | 98

## Niveau 1 — Kommunegruppe

kode | titel
--- | ---
1 | Hovedstadskommuner
2 | Storbykommuner
3 | Provinsbykommuner
4 | Oplandskommuner
5 | Landkommuner

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Hovedstadskommuner | NULL
101 | 2 | København | 1

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.kommunegrupper d ON f.kommunegrupper = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.kommunegrupper detail ON f.kommunegrupper = detail.kode AND detail.niveau = 2
  JOIN dim.kommunegrupper top ON top.kode = detail.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
