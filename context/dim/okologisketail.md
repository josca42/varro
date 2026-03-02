# Økologiske detailtal (okologisketail)

Dimensionstabel for økologiske detailtal.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedkategori | 14
2 | Underkategori | 87

## Niveau 1 — Hovedkategori

kode | titel
--- | ---
100 | Ris, brød, pasta, mel, gryn, kager
200 | Kød, pålæg og indmad inkl. dybfrost
300 | Fisk, skaldyr inkl. dybfrost
400 | Mælk, ost, æg
500 | Fedtstoffer, madolier
600 | Frugt
700 | Grøntsager
800 | Sukker, syltetøj, chokolade, slik, is o.l.
900 | Krydderier, suppeterninger o.l.
1000 | Kaffe, te, kakao o.l.
1100 | Juice, frugtsaft o.l.
1200 | Vin, hedvin og cider
1300 | Øl
1400 | Andre økologiske produkter

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
100 | 1 | Ris, brød, pasta, mel, gryn, kager | NULL
101 | 2 | Ris, inkl. dybfrost | 100

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.okologisketail d ON f.okologisketail = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.okologisketail detail ON f.okologisketail = detail.kode AND detail.niveau = 2
  JOIN dim.okologisketail top ON top.kode = detail.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
