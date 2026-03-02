# Landbrugslandsdele (landbrugslandsdele)

Landbrugslandsdele indfører et niveau mellem regioner og landsdele til klassifikationen [Regioner, landsdele og kommuner](/da/Statistik/dokumentation/nomenklaturer/regioner--landsdele-og-kommuner). Landbrugslandsdele aggregerer således de 11 landsdele til 8 landbrugslandsdele, angivet med _LL_ i koden.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Region | 5
2 | Landsdel | 8
3 | Landbrugslandsdel | 11
4 | Kommune | 99

## Niveau 1 — Region

kode | titel
--- | ---
081 | Region Nordjylland
082 | Region Midtjylland
083 | Region Syddanmark
084 | Region Hovedstaden
085 | Region Sjælland

## Niveau 2 — Landsdel

kode | titel | parent_kode
--- | --- | ---
LL1 | Hovedstaden (uden Bornholm) | 084
LL2 | Bornholm | 084
LL3 | Sjælland | 085
LL4 | Fyn | 083
LL5 | Sydjylland | 083
LL6 | Østjylland | 082
LL7 | Vestjylland | 082
LL8 | Nordjylland | 081

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
084 | 1 | Region Hovedstaden | NULL
LL1 | 2 | Hovedstaden (uden Bornholm) | 084
01 | 3 | Landsdel Byen København | LL1
101 | 4 | København | 01

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.landbrugslandsdele d ON f.landbrugslandsdele = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.landbrugslandsdele detail ON f.landbrugslandsdele = detail.kode AND detail.niveau = 4
  JOIN dim.landbrugslandsdele mid ON mid.kode = detail.parent_kode AND mid.niveau = 3
  JOIN dim.landbrugslandsdele mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 2
  JOIN dim.landbrugslandsdele top ON top.kode = mid2.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
