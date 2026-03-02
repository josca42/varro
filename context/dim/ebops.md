# Tjenestehandel (EBOPS) (ebops)

Danmarks udenrigshandel med tjenester opgøres på grundlag af FN’s tjenestehandelsnomenklatur [Extended Balance of Payments Services Classification 2010 (EBOPS 2010)](https://unstats.un.org/unsd/classifications/Family/Detail/101), som fremgår af den internationale tjenestehandelsmanual [Manual on Statistics of International Trade in Services 2010 (MSITS 2010)](https://unstats.un.org/unsd/tradeserv/TFSITS/manual.htm), der er udgivet af FN m.fl. senest i 2010. EBOPS er indbygget som nomenklatur i EU’s forordning om betalingsbalance mv.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 13
2 | Gruppe | 32
3 | Undergruppe | 35
4 | Detalje | 11

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
0 | Tjenester i alt
1 | Forarbejdningstjenester
2 | Reparationstjenester
3 | Transporttjenester
4 | Rejser
5 | Bygge- og anlægstjenester
6 | Forsikringstjenester
7 | Finansielle tjenester
8 | Royalties og licenser
9 | Telekommunikations-, computer- og informationstjenester
10 | Andre forretningstjenester
11 | Audiovisuelle tjenester samt tjenester ifm. uddannelse, sundhed, kultur og rekreation
12 | Offentlige tjenester i.a.n.

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
10 | 1 | Andre forretningstjenester | NULL
101 | 2 | Forsknings- og udviklingstjenester (FoU) | 10
1011 | 3 | Forsknings- og udvikling, som øger den samlede viden | 101
10111 | 4 | Forsknings- og udviklingstjenester, som øger den samlede viden | 1011

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.ebops d ON f.ebops = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.ebops detail ON f.ebops = detail.kode AND detail.niveau = 4
  JOIN dim.ebops mid ON mid.kode = detail.parent_kode AND mid.niveau = 3
  JOIN dim.ebops mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 2
  JOIN dim.ebops top ON top.kode = mid2.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
