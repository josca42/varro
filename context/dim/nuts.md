# Regioner og landsdele (NUTS) (nuts)

Med strukturreformen, som trådte i kraft fra 1. januar 2007, blev amterne nedlagt og erstattet af 5 nye regioner. Derudover blev der dannet 98 kommuner, som afløste de hidtidige 271. Til statistiske formål, inddeles de 5 regioner yderligere i 11 landsdele.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Region | 5
2 | Landsdel | 11
3 | Kommune | 99

## Niveau 1 — Region

kode | titel
--- | ---
81 | Region Nordjylland
82 | Region Midtjylland
83 | Region Syddanmark
84 | Region Hovedstaden
85 | Region Sjælland

## Niveau 2 — Landsdel

kode | titel | parent_kode
--- | --- | ---
1 | Landsdel Byen København | 84
2 | Landsdel Københavns omegn | 84
3 | Landsdel Nordsjælland | 84
4 | Landsdel Bornholm | 84
5 | Landsdel Østsjælland | 85
6 | Landsdel Vest- og Sydsjælland | 85
7 | Landsdel Fyn | 83
8 | Landsdel Sydjylland | 83
9 | Landsdel Østjylland | 82
10 | Landsdel Vestjylland | 82
11 | Landsdel Nordjylland | 81

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
84 | 1 | Region Hovedstaden | NULL
1 | 2 | Landsdel Byen København | 84
101 | 3 | København | 1

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.nuts d ON f.nuts = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.nuts detail ON f.nuts = detail.kode AND detail.niveau = 3
  JOIN dim.nuts mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.nuts top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
