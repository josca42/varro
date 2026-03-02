# Forbrugsklassifikation, dansk (ECOICOP-DST) (ecoicop_dst)

ECOICOP (Danmarks Statistik) er en klassifikation, der er udviklet af De Forenede Nationers Statistikafdeling og yderligere opdelt af Eurostat til at klassificere og analysere individuelle forbrugsudgifter afholdt af husholdninger og non-profit institutioner i overensstemmelse med forbrugsudgifternes formål. Danmarks Statistiks version af ECOICOP er opdelt på et endnu mere detaljeret niveau og anvendes i forbruger- og nettoprisindekset. Grupper i ECOICOP, hvor der ikke produceres prisindeks, er ikke medtaget i Danmarks Statistiks version af ECOICOP.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 12
2 | Gruppe | 44
3 | Klasse | 108
4 | Underklasse | 249
5 | Detalje | 454

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
1 | FØDEVARER OG IKKE-ALKOHOLISKE DRIKKEVARER
2 | ALKOHOLISKE DRIKKEVARER OG TOBAK 
3 | BEKLÆDNING OG FODTØJ
4 | BOLIG
5 | MØBLER, HUSHOLDNINGSUDSTYR OG HUSHOLDNINGSTJENESTER
6 | SUNDHED
7 | TRANSPORT
8 | KOMMUNIKATION
9 | FRITID OG KULTUR
10 | UDDANNELSE
11 | RESTAURANTER OG HOTELLER
12 | ANDRE VARER OG TJENESTER

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | FØDEVARER OG IKKE-ALKOHOLISKE DRIKKEVARER | NULL
11 | 2 | Fødevarer | 1
111 | 3 | Brød og kornprodukter | 11
1111 | 4 | Ris | 111
11110 | 5 | Ris | 1111

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.ecoicop_dst d ON f.ecoicop_dst = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.ecoicop_dst detail ON f.ecoicop_dst = detail.kode AND detail.niveau = 5
  JOIN dim.ecoicop_dst mid ON mid.kode = detail.parent_kode AND mid.niveau = 4
  JOIN dim.ecoicop_dst mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 3
  JOIN dim.ecoicop_dst mid3 ON mid3.kode = mid2.parent_kode AND mid3.niveau = 2
  JOIN dim.ecoicop_dst top ON top.kode = mid3.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **ecoicop**: Forbrugsklassifikation (ECOICOP)
