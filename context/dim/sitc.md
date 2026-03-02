# Udenrigshandel (SITC) (sitc)

Udenrigshandelsstatistikken opgøres på varegrupperingen efter FN’s [Standard International Trade Classification (SITC)](https://unstats.un.org/unsd/trade/sitcrev4.htm). Princippet for varerenes gruppering i SITC-nomenklatur er varernes forarbejdningsgrad (råvarer, halvfabrikata, færdigvarer). De metoder og fremgangsmåder, som anvendes ved udarbejdelse af udenrigshandelsstatistikken er beskrevet i publikationen [Udenrigshandel og betalingsbalance - Kilder og metoder](/da/Statistik/Publikationer/VisPub?cid=28426), løbende årgange.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Afdeling | 11
2 | Gruppe | 66
3 | Undergruppe | 3215

## Niveau 1 — Afdeling

kode | titel
--- | ---
0 | Næringsmidler og levende dyr
0-9 | I alt
1 | Drikkevarer og tobak
2 | Råstoffer, ikke spiselige
3 | Mineral. brændsels- og smørestoffer
4 | Animalske og veg. olier, fedtstoffer og voks
5 | Kemikalier og kemiske produkter
6 | Bearbejdede varer, hovedsagligt halvfabrikata
7 | Maskiner og transportmidler
8 | Bearbejdede varer i.a.n.
9 | Diverse varer og transaktioner, i.a.n. (beregnes ikke)

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
0 | 1 | Næringsmidler og levende dyr | NULL
00 | 2 | Levende dyr, spiselige | 0
00111 | 3 | Hornkvæg til avlsbrug | 00

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.oeko66 f
JOIN dim.sitc d ON f.sitc = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.oeko66 f
  JOIN dim.sitc detail ON f.sitc = detail.kode AND detail.niveau = 3
  JOIN dim.sitc mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.sitc top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
