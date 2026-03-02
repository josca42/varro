# Urbaniseringsgrad (DEGURBA) (degurba_dst)

Urbaniseringsgrad (DEGURBA) er en klassifikation som inddeler kommuner efter befolkningstæthed og antal indbyggere i største by i kommunen. Klassifikationen bygger på Eurostat's [Degree of Urbanisation (DEGURBA)](https://ec.europa.eu/eurostat/web/degree-of-urbanisation/background). Som supplement til Eurostat's DEGURBA, har Danmarks Statistik til brug i dansk sammenhæng, foretaget en underopdeling af _Medium befolket område_ og _Tyndt befolket område_ etter antal indbyggere i største by i kommunen jf. nedenfor:

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Urbaniseringsgrad | 3
2 | Kommunetype | 6
3 | Kommune | 99

## Niveau 1 — Urbaniseringsgrad

kode | titel
--- | ---
1 | Tæt befolket område
2 | Medium befolket område
3 | Tyndt befolket område

## Niveau 2 — Kommunetype

kode | titel | parent_kode
--- | --- | ---
11 | Tæt befolket område | 1
21 | Medium befolket område, mindst 40.000 indbyggere i største by i kommunen | 2
22 | Medium befolket område, mellem 15.000 og 40.000 indbyggere i største by i kommunen | 2
23 | Medium befolket område, under 15.000 indbyggere i største by i kommunen | 2
31 | Tyndt befolket område, mindst 15.000 indbyggere i største by i kommunen | 3
32 | Tyndt befolket område, under 15.000 indbyggere i største by i kommunen | 3

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Tæt befolket område | NULL
11 | 2 | Tæt befolket område | 1
101 | 3 | København | 11

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.degurba_dst d ON f.degurba_dst = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.degurba_dst detail ON f.degurba_dst = detail.kode AND detail.niveau = 3
  JOIN dim.degurba_dst mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.degurba_dst top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
