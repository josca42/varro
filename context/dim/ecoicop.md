# Forbrugsklassifikation (ECOICOP) (ecoicop)

Dimensionstabel for forbrugsklassifikation (ecoicop).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 12
2 | Gruppe | 47
3 | Klasse | 117
4 | Underklasse | 303

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
1 | FØDEVARER OG IKKEALKOHOLISKE DRIKKEVARER
2 | ALKOHOLISKE DRIKKEVARER, TOBAK OG EUFORISERENDE STOFFER
3 | BEKLÆDNING OG FODTØJ
4 | BOLIGBENYTTELSE, VAND, ELEKTRICITET, GAS OG ANDET BRÆNDSEL
5 | BOLIGUDSTYR, HUSHOLDNINGSUDSTYR OG RUTINEMÆSSIG VEDLIGEHOLDELSE AF BOLIG
6 | SUNDHED
7 | TRANSPORT
8 | MEDDELELSE
9 | FRITID OG KULTUR
10 | UNDERVISNING
11 | RESTAURANTER OG HOTELLER
12 | DIVERSE VARER OG TJENESTER

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | FØDEVARER OG IKKEALKOHOLISKE DRIKKEVARER | NULL
11 | 2 | Fødevarer | 1
111 | 3 | Brød og kornprodukter | 11
1111 | 4 | Ris | 111

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.ecoicop d ON f.ecoicop = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.ecoicop detail ON f.ecoicop = detail.kode AND detail.niveau = 4
  JOIN dim.ecoicop mid ON mid.kode = detail.parent_kode AND mid.niveau = 3
  JOIN dim.ecoicop mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 2
  JOIN dim.ecoicop top ON top.kode = mid2.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **ecoicop_dst**: Forbrugsklassifikation, dansk (ECOICOP-DST)
