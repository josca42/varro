# Igangværende uddannelser (AUDD) (ddu_audd)

DDU står for Den Danske Uddannelsesklassifikation og er det danske klassifikationssystem for alle uddannelser i Danmark. Klassifikationen drives af Danmarks Statistik i samarbejde med Uddannelses- og Forskningsministeriet (UFM) samt Børne- og Undervisningsministeriet (BUVM).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedområde | 8
2 | Niveau | 22
3 | Fagområde | 104
4 | Retning | 224
5 | Enkeltuddannelse | 4064

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
0 | 1 | Grundskolen | NULL
1 | 2 | Børnehaveklasse - 9. klasse | 0
11 | 3 | 1. klasse | 1
111 | 4 | 1. klasse | 11
200 | 5 | 1-6 år ivu | 111

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.ddu_audd d ON f.ddu_audd = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.ddu_audd detail ON f.ddu_audd = detail.kode AND detail.niveau = 5
  JOIN dim.ddu_audd mid ON mid.kode = detail.parent_kode AND mid.niveau = 4
  JOIN dim.ddu_audd mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 3
  JOIN dim.ddu_audd mid3 ON mid3.kode = mid2.parent_kode AND mid3.niveau = 2
  JOIN dim.ddu_audd top ON top.kode = mid3.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **ddu_udd**: Højest fuldførte uddannelser (UDD)
