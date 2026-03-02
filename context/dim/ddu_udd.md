# Højest fuldførte uddannelser (UDD) (ddu_udd)

Dimensionstabel for højest fuldførte uddannelser (udd).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedområde | 8
2 | Niveau | 22
3 | Fagområde | 104
4 | Retning | 269
5 | Enkeltuddannelse | 4224

## Niveau 1 — Hovedområde

kode | titel
--- | ---
0 | Grundskolen
1 | Forberedende uddannelser og øvrige ungdomsudd.
2 | Gymnasiale uddannelser
3 | Erhvervsfaglige uddannelser
5 | Korte videregående uddannelser
6 | Mellemlange videregående uddannelser
7 | Lange videregående uddannelser
8 | Ph. d. mv.

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
5 | 1 | Korte videregående uddannelser | NULL
59 | 2 | Øvrige korte videregående uddannelser | 5
594 | 3 | Samfundsfaglige og merkantile, KVU | 59
5941 | 4 | Samfundsfaglige og merkantile, KVU | 594
014100 | 5 | Formidl.-erhvervsspr. una - udvekslingstud. (kort vidg.) | 5941

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.ddu_udd d ON f.ddu_udd = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.ddu_udd detail ON f.ddu_udd = detail.kode AND detail.niveau = 5
  JOIN dim.ddu_udd mid ON mid.kode = detail.parent_kode AND mid.niveau = 4
  JOIN dim.ddu_udd mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 3
  JOIN dim.ddu_udd mid3 ON mid3.kode = mid2.parent_kode AND mid3.niveau = 2
  JOIN dim.ddu_udd top ON top.kode = mid3.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **ddu_audd**: Igangværende uddannelser (AUDD)
