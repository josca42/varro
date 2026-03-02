# Lande – udenrigshandel med varer (lande_uhv)

Geonomenklatur (GEONOM) gir mulighed for at klassificere lande og territorier i geografiske og økonomiske områder, til statistiske formål. Alle lande og territorier er angivet under en landekode. Landekoder er repræsenteret med to bogstaver (alpha-2), fx er Danmark angivet med DK.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Verdensdel | 6
2 | Region | 7
3 | Underregion | 14
4 | Land | 250
5 | Område | 2

## Niveau 1 — Verdensdel

kode | titel
--- | ---
51 | Europa
52 | Afrika
53 | Amerika
54 | Asien
55 | Oceanien og Polarregionerne
59 | Andre landekoder uden for EU

## Niveau 2 — Region

kode | titel | parent_kode
--- | --- | ---
511 | EU inklusiv uspecificerede lande | 51
519 | Europa uden for EU | 51
520 | Afrika | 52
530 | Amerika | 53
540 | Asien | 54
551 | Oceanien og Polarregionerne | 55
590 | Andre landekoder uden for EU | 59

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
51 | 1 | Europa | NULL
519 | 2 | Europa uden for EU | 51
5190 | 3 | Europa uden for EU | 519
GB | 4 | Storbritannien | 5190
XI | 5 | Nordirland | GB

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.lande_uhv d ON f.lande_uhv = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.lande_uhv detail ON f.lande_uhv = detail.kode AND detail.niveau = 5
  JOIN dim.lande_uhv mid ON mid.kode = detail.parent_kode AND mid.niveau = 4
  JOIN dim.lande_uhv mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 3
  JOIN dim.lande_uhv mid3 ON mid3.kode = mid2.parent_kode AND mid3.niveau = 2
  JOIN dim.lande_uhv top ON top.kode = mid3.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **lande_psd**: Lande – personstatistik
- **lande_uht_bb**: Lande – udenrigshandel
