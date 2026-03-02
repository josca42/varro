# Social beskyttelse (ESSPROS) (esspros)

Dimensionstabel for social beskyttelse (esspros).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedfunktion | 9
2 | Underfunktion | 50

## Niveau 1 — Hovedfunktion

kode | titel
--- | ---
1 | Sygdom og sundhed
2 | Invaliditet
3 | Alderdom
4 | Efterladte
5 | Familier
6 | Arbejdsløshed
7 | Bolig
8 | Øvrige sociale ydelser
9 | Administrationsudgifter

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Sygdom og sundhed | NULL
11 | 2 | Offentlig sygeskring | 1

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.esspros d ON f.esspros = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.esspros detail ON f.esspros = detail.kode AND detail.niveau = 2
  JOIN dim.esspros top ON top.kode = detail.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
