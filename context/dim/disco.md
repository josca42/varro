# Stillingsbetegnelser (DISCO-08) (disco)

DISCO-08 er en sekscifret klassifikation med fem niveauer der anvendes til klassificering og aggregering af oplysninger om arbejdsfunktioner fra forskellige statistiske undersøgelser. Klassifikationen er en revideret udgave af fagklassifikationen fra 1988 (DISCO-88), som den erstatter.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 10
2 | Undergruppe | 42
3 | Enhed | 126
4 | Stillingskategori | 429
5 | Stilling | 564

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
0 | Militært arbejde
1 | Ledelsesarbejde
2 | Arbejde, der forudsætter viden på højeste niveau inden for pågældende område
3 | Arbejde, der forudsætter viden på mellemniveau
4 | Almindeligt kontor- og kundeservicearbejde
5 | Service- og salgsarbejde
6 | Arbejde inden for landbrug, skovbrug og fiskeri ekskl. Medhjælp
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
JOIN dim.disco d ON f.disco = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.disco detail ON f.disco = detail.kode AND detail.niveau = 5
  JOIN dim.disco mid ON mid.kode = detail.parent_kode AND mid.niveau = 4
  JOIN dim.disco mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 3
  JOIN dim.disco mid3 ON mid3.kode = mid2.parent_kode AND mid3.niveau = 2
  JOIN dim.disco top ON top.kode = mid3.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **disco_ls**: Lønstruktur-stillingsbetegnelser (DISCO-08 LS)
