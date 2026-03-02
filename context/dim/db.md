# Dansk Branchekode 2007 (DB07) (db)

Dansk Branchekode 2007 (DB07), er en 6-cifret branchenomenklatur, der først og fremmest er udarbejdet til statistisk brug. De indledende afsnit til DB07 beskriver regler og retningslinier for tildeling af branchekode til virksomhederne og deres produktionsenheder (arbejdssteder). Dermed sikres, at brancheplaceringen foretages på en ensartet måde i Danmarks Statistiks Erhvervsstatistiske Register (ESR) og dermed også i Det Centrale Virksomhedsregister (CVR).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
2 | Afsnit | 88
3 | Hovedgruppe | 272
4 | Gruppe | 615
5 | Undergruppe | 736

## Niveau 2 — Afsnit

kode | titel
--- | ---
1 | Plante- og husdyravl, jagt og serviceydelser i forbindelse hermed
2 | Skovbrug og skovning
3 | Fiskeri og akvakultur
5 | Indvinding af kul og brunkul
6 | Indvinding af råolie og naturgas
7 | Brydning af metalmalme
8 | Anden råstofindvinding
9 | Serviceydelser i forbindelse med råstofindvinding
10 | Fremstilling af fødevarer
11 | Fremstilling af drikkevarer
12 | Fremstilling af tobaksprodukter
13 | Fremstilling af tekstiler
14 | Fremstilling af beklædningsartikler
15 | Fremstilling af læder og lædervarer
16 | Fremstilling af træ og varer af træ og kork, undtagen møbler; fremstilling af varer af strå og flettematerialer
17 | Fremstilling af papir og papirvarer
18 | Trykning og reproduktion af indspillede medier
19 | Fremstilling af koks og raffinerede mineralolieprodukter
20 | Fremstilling af kemiske produkter
21 | Fremstilling af farmaceutiske råvarer og farmaceutiske præparater
22 | Fremstilling af gummi- og plastprodukter
23 | Fremstilling af andre ikke-metalholdige mineralske produkter
24 | Fremstilling af metal
25 | Jern- og metalvareindustri, undtagen maskiner og udstyr
26 | Fremstilling af computere, elektroniske og optiske produkter
27 | Fremstilling af elektrisk udstyr
28 | Fremstilling af maskiner og udstyr i.a.n.
29 | Fremstilling af motorkøretøjer, påhængsvogne og sættevogne
30 | Fremstilling af andre transportmidler
31 | Fremstilling af møbler
32 | Anden fremstillingsvirksomhed
33 | Reparation og installation af maskiner og udstyr
35 | El-, gas- og fjernvarmeforsyning
36 | Vandforsyning
37 | Opsamling og behandling af spildevand
38 | Indsamling, behandling og bortskaffelse af affald; genbrug
39 | Rensning af jord og grundvand og anden form for forureningsbekæmpelse
41 | Opførelse af bygninger
42 | Anlægsarbejder
43 | Bygge- og anlægsvirksomhed, som kræver specialisering
45 | Handel med biler og motorcykler, og reparation heraf
46 | Engroshandel undtagen med motorkøretøjer og motorcykler
47 | Detailhandel undtagen med motorkøretøjer og motorcykler
49 | Landtransport; rørtransport
50 | Skibsfart
51 | Luftfart
52 | Hjælpevirksomhed i forbindelse med transport
53 | Post- og kurertjenester
55 | Overnatningsfaciliteter
56 | Restaurationsvirksomhed
58 | Udgivervirksomhed
59 | Produktion af film, video- og tv-programmer, lydoptagelser og musikudgivelser
60 | Radio- og tv-virksomhed
61 | Telekommunikation
62 | Computerprogrammering, konsulentbistand vedrørende informationsteknologi og lignende aktiviteter
63 | Informationstjenester
64 | Pengeinstitut- og finansieringsvirksomhed undtagen forsikring og
65 | Forsikring, genforsikring og pensionsforsikring undtagen lovpligtig socialforsikring
66 | Hjælpetjenester i forbindelse med finansieringsvirksomhed og forsikring
68 | Fast ejendom
69 | Juridisk bistand, bogføring og revision
70 | Hovedsæders virksomhed; virksomhedsrådgivning
71 | Arkitekt- og ingeniørvirksomhed; teknisk afprøvning og analyse
72 | Videnskabelig forskning og udvikling
73 | Reklame og markedsanalyse
74 | Andre liberale, videnskabelige og tekniske tjenesteydelser
75 | Dyrlæger
77 | Udlejning og leasing
78 | Arbejdsformidling
79 | Rejsebureauers og rejsearrangørers virksomhed, reservationstjenesteydelser og tjenesteydelser i forbindelse hermed
80 | Vagt- og sikkerhedstjenester og overvågning
81 | Serviceydelser i forbindelse med ejendomme samt landskabspleje
82 | Administrationsservice, kontorservice og anden forretningsservice
84 | Offentlig forvaltning, forsvar og socialsikring
85 | Undervisning
86 | Sundhedsvæsen
87 | Institutionsophold
88 | Sociale foranstaltninger uden institutionsophold
90 | Kreative aktiviteter, kunst og forlystelser
91 | Biblioteker, arkiver, museer og anden kulturel virksomhed
92 | Lotteri- og anden spillevirksomhed
93 | Sport, forlystelser og fritidsaktiviteter
94 | Organisationer og foreninger
95 | Reparation af computere og varer til personligt brug og husholdningsbrug
96 | Andre personlige serviceydelser
97 | Husholdninger med ansat medhjælp
98 | Private husholdningers produktion af varer og tjenesteydelser til eget brug, i.a.n.
99 | Eksterritoriale organisationer og organer

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
1 | 2 | Plante- og husdyravl, jagt og serviceydelser i forbindelse hermed | NULL
11 | 3 | Dyrkning af etårige afgrøder | 1
111 | 4 | Dyrkning af korn (undtagen ris), bælgfrugter og olieholdige frø | 11
11100 | 5 | Dyrkning af korn (undtagen ris), bælgfrugter og olieholdige frø | 111

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.db d ON f.db = d.kode
WHERE d.niveau = 2
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.db detail ON f.db = detail.kode AND detail.niveau = 5
  JOIN dim.db mid ON mid.kode = detail.parent_kode AND mid.niveau = 4
  JOIN dim.db mid2 ON mid2.kode = mid.parent_kode AND mid2.niveau = 3
  JOIN dim.db top ON top.kode = mid2.parent_kode AND top.niveau = 2
GROUP BY top.titel
```

## Relaterede tabeller

- **db_10**: Branchekode 10-gruppering (DB07)
