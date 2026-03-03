table: fact.neetsyg
description: Lægebesøg i befolkningen (16-24 år) (eksperimentel statistik) efter NEET-status, nøgletal, sundhedsperson, bopæl, køn og tid
measure: indhold (unit -)
columns:
- statusneet: values [0=Aktive og ikke-aktive i alt, 5=Aktive, 10=Ikke-aktive (NEET)]
- bnogle: values [1000=Kontakter (antal pr. person), 1005=Personer med kontakt (antal), 1010=Personer med kontakt (procent)]
- neetsund: values [TOTAL=Sundhedsperson i alt, 1=Almen læge, 2=Speciallæge, 3=Tandlæge/tandplejer, 4=Kiropraktor, 5=Fysioterapeut, 6=Fodterapeut, 7=Psykolog, 8=Øvrige sundhedspersoner]
- bop: join dim.nuts on bop=kode; levels [1, 2]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- bnogle is a measurement selector — every other dimension combination appears 3 times (once per bnogle value). Always filter to exactly one: bnogle=1000 (kontakter pr. person), bnogle=1005 (antal personer med kontakt), or bnogle=1010 (procent med kontakt). Forgetting this triples all sums.
- neetsund categories (1–8) are NOT mutually exclusive for persons — one person can visit both a GP and a specialist in a year. Sum of individual providers (919k) far exceeds TOTAL (559k). Use neetsund='TOTAL' for unduplicated person counts; never SUM across neetsund values 1–8.
- statusneet=0 is the aggregate (aktive+NEET combined). To compare NEET vs active youth, filter statusneet IN (5, 10). Never sum statusneet 5+10 alongside statusneet=0.
- bop=0 is the national total — not in dim.nuts (LEFT JOIN returns NULL for niveau/titel). To query by region: JOIN dim.nuts ON bop=kode WHERE d.niveau=1 (5 regioner) or d.niveau=2 (11 landsdele). Use ColumnValues("nuts", "titel", for_table="neetsyg") to see the 16 geographic codes used.
- kon=MOK is the both-genders total. Filter kon='MOK' for national totals or filter to 'M'/'K' — never sum all three.
- Sample query — NEET vs active GP contacts per person by region (2022):
  SELECT d.titel, f.statusneet, f.indhold
  FROM fact.neetsyg f JOIN dim.nuts d ON f.bop=d.kode
  WHERE f.bnogle=1000 AND f.neetsund='TOTAL' AND f.kon='MOK'
    AND f.tid='2022-01-01' AND d.niveau=1 AND f.statusneet IN (5,10)
  ORDER BY d.titel, f.statusneet;
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on bop=dim_kode. Exclude bop=0.