# Lande – udenrigshandel (lande_uht_bb)

Dimensionstabel for lande – udenrigshandel.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Verdensdel | 6
2 | Region | 11
3 | Underregion | 14
4 | Land | 237

## Niveau 1 — Verdensdel

kode | titel
--- | ---
A1 | Amerika
E1 | Europa
F1 | Afrika
O1 | Oceanien og Polarregionerne
ORG | Organisationer
S1 | Asien

## Niveau 2 — Region

kode | titel | parent_kode
--- | --- | ---
A2 | Nordamerika | A1
A5 | Centralamerika | A1
A7 | Sydamerika | A1
B6 | EU-27 (uden Storbritannien) | E1
D6 | Extra EU-27 | E1
F2 | Andre afrikanske lande | F1
F4 | Nordafrika | F1
O2 | Oceanien og Polarregionerne | O1
ORG | Organisationer | ORG
S3 | Nær- og mellemøstlige lande | S1
S6 | Andre Asiatiske lande | S1

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
E1 | 1 | Europa | NULL
B6 | 2 | EU-27 (uden Storbritannien) | E1
4Y | 3 | Alle EU-institutioner, organer og organismer, inkl. ECB og ESM | B6
4A | 4 | EU-institutioner | 4Y

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.lande_uht_bb d ON f.lande_uht_bb = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.lande_uht_bb detail ON f.lande_uht_bb = detail.kode AND detail.niveau = 4
  JOIN dim.lande_uht_bb mid ON mid.kode = detail.parent_kode AND mid.niveau = 3
  JOIN dim.lande_uht_bb mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 2
  JOIN dim.lande_uht_bb top ON top.kode = mid2.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **lande_psd**: Lande – personstatistik
- **lande_uhv**: Lande – udenrigshandel med varer
