# Bygherrekategorier (bygherre)

Bygherreforhold følger de koder, der findes i [Bygnings- og BoligRegistret (BBR)](https://teknik.bbr.dk/kodelister), men grupperes til statistiske formål.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedkategori | 3
2 | Underkategori | 10

## Niveau 1 — Hovedkategori

kode | titel
--- | ---
1 | Private bygherrer
2 | Boligforeninger
3 | Offentlige myndigheder

## Niveau 2 — Underkategori

kode | titel | parent_kode
--- | --- | ---
10 | Privatpersoner eller interessentskab | 1
20 | Alment boligselskab | 2
30 | Aktie-, anpart- eller andet selskab (undtagen interessentskab) | 1
40 | Forening, legat eller selvejende institution | 1
41 | Privat andelsboligforening | 1
50 | Den kommune, hvori ejendommen er beliggende | 3
60 | Anden primærkommune | 3
70 | Region | 3
80 | Staten | 3
90 | Andet, herunder moderejendomme | 1

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Private bygherrer | NULL
10 | 2 | Privatpersoner eller interessentskab | 1

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.bygv01 f
JOIN dim.bygherre d ON f.bygherre = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.bygv01 f
  JOIN dim.bygherre detail ON f.bygherre = detail.kode AND detail.niveau = 2
  JOIN dim.bygherre top ON top.kode = detail.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
