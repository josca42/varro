# Lande – personstatistik (lande_psd)

Dimensionstabel for lande – personstatistik.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Verdensdel | 6
2 | Region | 13
3 | Land | 265

## Niveau 1 — Verdensdel

kode | titel
--- | ---
1 | Europa
2 | Afrika
3 | Amerika
4 | Asien
5 | Oceanien
6 | Statsløse og uoplyst

## Niveau 2 — Region

kode | titel | parent_kode
--- | --- | ---
100 | Danmark | 1
251 | Færøerne | 1
252 | Grønland | 1
361 | EU-27 (uden Storbritannien) | 1
363 | Andre europæiske lande | 1
371 | Afrika | 2
372 | Nordamerika | 3
373 | Syd- og mellemamerika | 3
374 | Asien | 4
375 | Oceanien | 5
381 | Udlandet uoplyst | 6
591 | Statsløse | 6
999 | Helt uoplyst | 6

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
6 | 1 | Statsløse og uoplyst | NULL
999 | 2 | Helt uoplyst | 6
0 | 3 | Helt uoplyst | 999

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.lande_psd d ON f.lande_psd = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.lande_psd detail ON f.lande_psd = detail.kode AND detail.niveau = 3
  JOIN dim.lande_psd mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.lande_psd top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **lande_uht_bb**: Lande – udenrigshandel
- **lande_uhv**: Lande – udenrigshandel med varer
