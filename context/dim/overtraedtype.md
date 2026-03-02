# Overtrædelsestyper (overtraedtype)

Dette er en oversigt over de typer af overtrædelser, der optræder i Statistikbanken, og hvad de indeholder på et mere detaljeret niveau. Opdelingen er lavet af Danmarks Statistik og er forskellig fra opdelingen i Rigspolitiets statistik. Både Danmarks statistiks kriminalstatistik og Rigspolitiets statistikker er dog lavet på baggrund af samme datamateriale.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedkategori | 3
2 | Kategori | 12
3 | Underkategori | 88
4 | Overtrædelsestype | 1305

## Niveau 1 — Hovedkategori

kode | titel
--- | ---
1 | Straffelov
2 | Færdselslov
3 | Særlov

## Niveau 2 — Kategori

kode | titel | parent_kode
--- | --- | ---
11 | Seksualforbrydelser | 1
12 | Voldsforbrydelser | 1
13 | Ejendomsforbrydelser | 1
14 | Andre straffelovsforbrydelser | 1
21 | Færdselsuheld uspecificeret | 2
22 | Færdselslov spiritus | 2
24 | Mangler ved køretøj | 2
26 | Færdselslov i øvrigt | 2
32 | Lov om euforiserende stoffer | 3
34 | Våbenloven | 3
36 | Skatte og afgiftslove | 3
38 | Særlove i øvrigt | 3

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Straffelov | NULL
11 | 2 | Seksualforbrydelser | 1
1110 | 3 | Blodskam mv. | 11
111072121 | 4 | Blodskam, børn under 15 år | 1110

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.overtraedtype d ON f.overtraedtype = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.overtraedtype detail ON f.overtraedtype = detail.kode AND detail.niveau = 4
  JOIN dim.overtraedtype mid ON mid.kode = detail.parent_kode AND mid.niveau = 3
  JOIN dim.overtraedtype mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 2
  JOIN dim.overtraedtype top ON top.kode = mid2.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
