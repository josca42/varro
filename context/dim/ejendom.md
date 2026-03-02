# Ejendomskategorier (ejendom)

Dimensionstabel for ejendomskategorier.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedkategori | 11
2 | Underkategori | 23

## Niveau 1 — Hovedkategori

kode | titel
--- | ---
111 | Enfamiliehuse
129 | Ejendomme med 2 eller 3 lejligheder
149 | Ejendomme med 4 lejligheder eller derover
201 | Blandet beboelse-forretning
301 | Rene forretningsejendomme
401 | Fabriks- og lagerejendomme
509 | Landbrug, i alt
801 | Sommerhuse
903 | Grunde, i alt
2103 | Ejerlejligheder, i alt
9901 | Andet bebygget

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
111 | 1 | Enfamiliehuse | NULL
111 | 2 | Enfamiliehuse | 111

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.ejendom d ON f.ejendom = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.ejendom detail ON f.ejendom = detail.kode AND detail.niveau = 2
  JOIN dim.ejendom top ON top.kode = detail.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
