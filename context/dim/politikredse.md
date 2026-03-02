# Politikredse (politikredse)

Danmark har siden 2007 været inddelt i 12 politikredse. Hver politikreds ledes af en politidirektør, der har ansvar for politiets virksomhed i politikredsen.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Politikreds | 12
2 | Kommune | 99

## Niveau 1 — Politikreds

kode | titel
--- | ---
1 | Nordjyllands Politi
2 | Østjyllands Politi
3 | Midt- og Vestjyllands Politi
4 | Sydøstjyllands Politi
5 | Syd- og Sønderjyllands Politi
6 | Fyns Politi
7 | Sydsjællands og Lolland-Falsters Politi
8 | Midt- og Vestsjællands Politi
9 | Nordsjællands Politi
10 | Københavns Vestegns Politi
11 | Københavns Politi
12 | Bornholms Politi

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
11 | 1 | Københavns Politi | NULL
101 | 2 | København | 11

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.politikredse d ON f.politikredse = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.politikredse detail ON f.politikredse = detail.kode AND detail.niveau = 2
  JOIN dim.politikredse top ON top.kode = detail.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
