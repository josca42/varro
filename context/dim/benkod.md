# Benyttelseskoder (benkod)

Dimensionstabel for benyttelseskoder.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Benyttelseskode | 39

## Niveau 1 — Benyttelseskode

kode | titel
--- | ---
0 | Undtaget fra vurdering
1 | Beboelse
2 | Beboelse og forretning
3 | Forretning
4 | Fabrik og lager
5 | Landbrug, bebygget
6 | Særskilt vurderet skov og plantage
7 | Frugtplantage, gartneri og planteskole
8 | Sommerhus
9 | Ubebygget areal
10 | Statsejendom
11 | Kommunal beboelses- og forretningsejendom
12 | Andre bebyggede kommunale ejendomme
13 | Anden vurdering
14 | Ejendom vurderet til 0
16 | Udgået ejendom eller nummer
17 | Ubebygget landbrugslod, m.v.
20 | Moderejendom for ejerlejligheder
21 | Etagejerlejlighed med 1 lejlighed
22 | Beboelses- og forretningsejerlejlighed
23 | Forretningsejerlejlighed
24 | Fabriks- og lagerejerlejlighed
25 | Øvrige ejerlejligheder
26 | Ejerlejlighed i lav bebyggelse
27 | Ejerlejlighed i rækkehus
28 | Ejerlejlighed til sommerbeboelse på fremmed grund
29 | Anden ejerlejlighed på fremmed grund
31 | Støttet andelsbolig
33 | Private institutions- og serviceejendomme
34 | Visse erhvervsejendomme
41 | Beboelse på fremmed grund
42 | Beboelse og forretning på fremmed grund
43 | Ren forretning på fremmed grund
44 | Fabrik og lager på fremmed grund
45 | Andre bygninger på fremmed grund
48 | Sommerhus (kolonihavehus) på fremmed grund
49 | Arealer med bygning på fremmed grund
78 | Sommerhus på fremmed grund, forbigået ved vurderingen
79 | Anden bygning på fremmed grund, forbigået ved vurderingen

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.benkod d ON f.benkod = d.kode
WHERE d.niveau = 1
```
