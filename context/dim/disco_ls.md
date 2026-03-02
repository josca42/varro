# Lønstruktur-stillingsbetegnelser (DISCO-08 LS) (disco_ls)

Dimensionstabel for lønstruktur-stillingsbetegnelser (disco-08 ls).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 10
2 | Undergruppe | 42
3 | Enhed | 125
4 | Stillingskategori | 423
5 | Stilling | 558

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
0 | Militært arbejde
1 | Ledelsesarbejde
2 | Arbejde, der forudsætter viden på højeste niveau inden for pågældende område
3 | Arbejde, der forudsætter viden på mellemniveau
4 | Almindeligt kontor- og kundeservicearbejde
5 | Service- og salgsarbejde
6 | Arbejde inden for landbrug, skovbrug og fiskeri ekskl. medhjælp
7 | Håndværkspræget arbejde
8 | Operatør- og monteringsarbejde samt transportarbejde
9 | Andet manuelt arbejde

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
0 | 1 | Militært arbejde | NULL
1 | 2 | Militært arbejde på officersniveau | 0
11 | 3 | Militært arbejde på officersniveau | 1
110 | 4 | Militært arbejde på officersniveau | 11
11000 | 5 | Militært arbejde på officersniveau | 110

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.disco_ls d ON f.disco_ls = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.disco_ls detail ON f.disco_ls = detail.kode AND detail.niveau = 5
  JOIN dim.disco_ls mid ON mid.kode = detail.parent_kode AND mid.niveau = 4
  JOIN dim.disco_ls mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 3
  JOIN dim.disco_ls mid3 ON mid3.kode = mid2.parent_kode AND mid3.niveau = 2
  JOIN dim.disco_ls top ON top.kode = mid3.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **disco**: Stillingsbetegnelser (DISCO-08)
