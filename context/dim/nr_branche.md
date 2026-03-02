# Nationalregnskabsbranche (NR) (nr_branche)

Udgangspunktet for nationalregnskabets branchegruppering er Danmarks Statistiks [Dansk Branchekode 2007 (DB07)](https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/dansk-branchekode-db07) og de standardgrupperinger der er knyttet hertil.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedbranche | 13
2 | Branchegruppe | 21
3 | Branche | 38
4 | Underbranche | 69
5 | Detailbranche | 117

## Niveau 1 — Hovedbranche

kode | titel
--- | ---
A | Landbrug, skovbrug og fiskeri
B | Råstofindvinding
C | Industri
D-E | Forsyningsvirksomhed
F | Bygge og anlæg
G-I | Handel og transport mv.
J | Information og kommunikation
K | Finansiering og forsikring
LA | Ejendomshandel, udlejning af erhvervsejendomme
LB | Boliger
M-N | Erhvervsservice
O-Q | Offentlig administration, undervisning, sundhed
R-S | Kultur, fritid, anden service

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
A | 1 | Landbrug, skovbrug og fiskeri | NULL
A | 2 | Landbrug, skovbrug og fiskeri | A
A | 3 | Landbrug, skovbrug og fiskeri | A
01000 | 4 | Landbrug og gartneri | A
010000 | 5 | Landbrug og gartneri | 01000

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.nr_branche d ON f.nr_branche = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.nr_branche detail ON f.nr_branche = detail.kode AND detail.niveau = 5
  JOIN dim.nr_branche mid ON mid.kode = detail.parent_kode AND mid.niveau = 4
  JOIN dim.nr_branche mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 3
  JOIN dim.nr_branche mid3 ON mid3.kode = mid2.parent_kode AND mid3.niveau = 2
  JOIN dim.nr_branche top ON top.kode = mid3.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
