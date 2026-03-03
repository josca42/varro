table: fact.krise1
description: Ophold og beboere på krisecentre efter bopælsregion, varighed, beboerstatus og tid
measure: indhold (unit Antal)
columns:
- bopreg: join dim.nuts on bopreg=kode [approx]; levels [1]
- kmdr: values [TOT=I alt, 000001=1 døgn, 002005=2-5 døgn, 006030=6-30 døgn, 031119=31-119 døgn, 120365=120-364 døgn, 365000=Hele året, 999999=Uoplyst]
- bebostat: values [1=Ophold, 2=Ophold med børn, 3=Kvinder, 35=Mænd (2024-), 38=Uoplyst køn (voksne) (2024-), 4=Børn]
- tid: date range 2017-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- bopreg joins dim.nuts but only at niveau=1 (5 regioner: 81–85). No landsdele or kommuner. bopreg=0 is the national total (I alt), bopreg=996 is uoplyst bopæl — neither appears in dim.nuts, so always filter bopreg to avoid the total row when summing.
- bebostat is a measurement selector, not a category for summing. Values measure different things: 1=Ophold (stays/episodes), 2=Ophold med børn (stays with children, subset of 1), 3=Kvinder (adult women residents), 4=Børn (accompanying children), 35=Mænd (adult men residents, 2024 only), 38=Uoplyst køn (adults with unknown gender, 2024 only). Always filter to a single bebostat.
- bebostat=35 and bebostat=38 are zero for 2017–2023 and only contain data from 2024.
- kmdr=TOT is the national aggregate across all duration bands; the 6 duration bands (000001 through 365000) sum exactly to TOT. kmdr=999999 (Uoplyst) listed in the column spec does not actually appear in the data.
- To get total stays by region for a given year: filter kmdr='TOT', bebostat='1', exclude bopreg IN ('0','996'). To include unknown region, add bopreg='996'. bopreg='0' is always redundant when summing regions.
- Map: /geo/regioner.parquet (niveau 1) — merge on bopreg=dim_kode. Exclude bopreg IN ('0', '996').