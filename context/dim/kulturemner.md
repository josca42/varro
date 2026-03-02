# Kulturemner (kulturemner)

Kulturområdet i Danmarks Statistik, er klassificeret i 28 kulturemner, der er defineret med udgangspunkt i UNESCOS strukturering af kulturen i [2009 UNESCO Framework for Cultural Statistics](http://colectica:25233/File/782e8546-24c0-49c4-baa7-b2f3668b57e7). Kulturemnerne er tilpasset danske forhold og fastlagt i samarbejde med Kulturministeriet, men der findes endnu ikke statistik for alle kulturemner.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedemne | 6
2 | Underemne | 28

## Niveau 1 — Hovedemne

kode | titel
--- | ---
1 | Idræt og fritid
2 | Kulturarv
3 | Medier, biblioteker og litteratur
4 | Scene og musik
5 | Visuel kunst og design
6 | Anden kulturel aktivitet

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
3 | 1 | Medier, biblioteker og litteratur | NULL
K02 | 2 | Biblioteker | 3

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.kulturemner d ON f.kulturemner = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.kulturemner detail ON f.kulturemner = detail.kode AND detail.niveau = 2
  JOIN dim.kulturemner top ON top.kode = detail.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
