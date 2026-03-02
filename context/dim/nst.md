# Godstransport (NST 2007) (nst)

Standardgodsklassifikationen til transportstatistik forkortet NST (2007) er en statistisk nomenklatur for de varer, der transporteres med lastbiler, tog og skibe.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 20
2 | Varegruppe | 81

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
1 | Produkter fra landbrug, jagt og skovbrug; fisk og fiskeprodukter
10 | Metal; færdige metalprodukter, undtagen maskiner og udstyr
11 | Maskiner og udstyr i.a.n.; kontormaskiner og computere; elektriske maskiner og apparater i.a.n.; telemateriel; medicinske instrumenter, præcisionsinstrumenter og optiske instrumenter; ure 
12 | Transportmidler 
13 | Møbler; andre færdigvarer i.a.n.
14 | Sekundære råmaterialer; kommunalt affald og andet affald
15 | Breve, pakker
16 | Udstyr og materiel til godstransport 
17 | Gods, der flyttes i forbindelse med privat flytning og kontorflytning; bagage og varer, der medføres af passagerer; motorkøretøjer, der flyttes med henblik på reparation; andet gods, der ikke er bestemt til markedet i.a.n. 
18 | Samlegods: En blanding af forskellige typer gods, som transporteres samlet
19 | Uidentificerbart gods: Gods, som af en hvilken som helst grund ikke kan identificeres og derfor ikke kan henføres under gruppe 01-16.
2 | Stenkul og brunkul; råolie og naturgas
20 | Andet gods i.a.n. 
3 | Metalmalm og produkter af anden råstofudvinding; tørv; uran og thorium
4 | Fødevarer, drikkevarer og tobaksprodukter
5 | Tekstiler og beklædningsartikler; læder og lædervarer
6 | Træ og varer af træ og kork (undtagen møbler); varer af strå og flettematerialer; papirmasse, papir og papirvarer; trykt materiale og indspillede medier
7 | Koks og raffinerede mineralolieprodukter 
8 | Kemiske produkter og kemofibre; gummi- og plastprodukter; nukleart brændsel 
9 | Andre ikke-metalholdige mineralske produkter

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 1 | Produkter fra landbrug, jagt og skovbrug; fisk og fiskeprodukter | NULL
01.1 | 2 | Korn | 1

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.nst d ON f.nst = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.nst detail ON f.nst = detail.kode AND detail.niveau = 2
  JOIN dim.nst top ON top.kode = detail.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
