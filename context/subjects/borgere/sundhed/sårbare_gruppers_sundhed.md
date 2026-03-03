<fact tables>
<table>
id: neetsyg
description: Lægebesøg i befolkningen (16-24 år) (eksperimentel statistik) efter NEET-status, nøgletal, sundhedsperson, bopæl, køn og tid
columns: statusneet, bnogle, neetsund, bop, kon, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: neetmed
description: Køb af receptpligtig medicin i befolkningen (16-24 år) (eksperimentel statistik) efter NEET-status, nøgletal, medicintype, bopæl, køn og tid
columns: statusneet, bnogle, medicintype, bop, kon, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: neetlpr
description: Sygehusbenyttelse i befolkningen (16-24 år) (eksperimentel statistik) efter NEET-status, nøgletal, kontakttype, bopæl, køn og tid
columns: statusneet, bnogle, ktype, bop, kon, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: neetdiag
description: Sygehusbenyttelse i befolkningen (16-24 år) (eksperimentel statistik) efter NEET-status, nøgletal, hoveddiagnosegruppe, bopæl, køn og tid
columns: statusneet, bnogle, diagnosehoved, bop, kon, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All four tables cover the same population (16–24 year olds, 2019–2023) and share the same NEET classification (statusneet: 0=total, 5=aktive, 10=NEET). Pick by health domain: neetsyg=GP/specialist visits, neetmed=prescription medicine, neetlpr=hospital contacts by type, neetdiag=hospital contacts by diagnosis.
- bnogle is a measurement selector present in every table — always filter to exactly one value or all sums are meaningless. The three options are count (antal pr. person / antal med kontakt / antal med diagnose), person count (antal), and percentage. neetdiag has only 2 bnogle values (count + percent).
- The category dimension in each table (neetsund / medicintype / ktype / diagnosehoved) counts persons who are NOT mutually exclusive across categories. TOTAL/TOTAL2/TOTAL3/TOTH gives the deduplicated person count; never sum across individual categories when using the "persons" metric.
- Geography: bop joins dim.nuts at niveau=1 (5 regioner) and niveau=2 (11 landsdele). bop=0 is the national total and is not in dim.nuts — use a LEFT JOIN or exclude it with WHERE bop != 0 when joining.
- These are experimental statistics (eksperimentel statistik) — limited time range (2019–2023) and no municipality-level breakdown.
- Map: all four tables support choropleth at region (niveau 1) and landsdel (niveau 2) level via /geo/regioner.parquet and /geo/landsdele.parquet — merge on bop=dim_kode. No kommune-level breakdown available.