# Social status (soc_status)

Dimensionstabel for social status.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedstatus | 3
2 | Delstatus | 5
3 | Understatus | 44

## Niveau 1 — Hovedstatus

kode | titel
--- | ---
1 | Beskæftigede
2 | Arbejdsløse
3 | Personer uden for arbejdsstyrken

## Niveau 2 — Delstatus

kode | titel | parent_kode
--- | --- | ---
11 | Selvstændige | 1
12 | Medarbejdende ægtefæller | 1
13 | Lønmodtagere | 1
21 | Arbejdsløse | 2
31 | Personer uden for arbejdsstyrken | 3

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Beskæftigede | NULL
11 | 2 | Selvstændige | 1
110 | 3 | Selvstændige (primær status ult. nov.) | 11

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.soc_status d ON f.soc_status = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.soc_status detail ON f.soc_status = detail.kode AND detail.niveau = 3
  JOIN dim.soc_status mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.soc_status top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
