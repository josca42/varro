table: fact.regr11
description: Regionernes regnskaber på hovedkonti efter område, hovedkonto, dranst, art, prisenhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- funk1: values [X=I alt hovedkonto 0-5, 1=1 Sundhed, 2=2 Social og specialundervisning, 3=3 Regional udvikling, 4=4 Fælles formål og administration, 5=5 Renter m.v.]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 7=7 Finansiering]
- art: values [UE=Udgifter excl. beregnede omkostninger, UI=Udgifter incl. beregnede omkostninger, TOT=I alt (netto), I=Indtægter, S0=0 Beregnede omkostninger ... S9=9 Interne udgifter og indtægter, 91=9.1 Overførte lønninger, 92=9.2 Overførte varekøb, 94=9.4 Overførte tjenesteydelser, 97=9.7 Interne indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Code 0 = national total (not in dim.nuts); codes 81-85 = 5 regions at niveau=1. JOIN eliminates the national row automatically. Use ColumnValues("nuts", "titel", for_table="regr11") to confirm the 5 regions.
- prisenhed is a measurement selector: LOBM=1.000 kr., INDL=kr. per inhabitant. Every combination is repeated for both units — always filter to one (typically LOBM). Forgetting this silently doubles all sums.
- art has 52 values mixing aggregates and detail lines. TOT=netto total, UE=brutto udgifter excl. beregnede omkostninger, UI=brutto incl., I=indtægter, S0-S9=grouped costs, numeric 00-97=detailed line items. Never SUM across all art values. For total gross expenditure use art='UE'; for net use art='TOT'.
- dranst splits by account type (1=drift, 2=statsrefusion, 3=anlæg, 4=renter, 7=finansiering). For operating expenditure use dranst=1. Summing across all dranst types mixes operating, capital, and financing flows.
- funk1 has 6 high-level sector codes: X=all, 1=Sundhed, 2=Social og specialundervisning, 3=Regional udvikling, 4=Fælles formål og administration, 5=Renter m.v. No dim join — use inline values.
- Minimal filtering example for total regional operating expenditure 2023: WHERE funk1='X' AND dranst='1' AND art='UE' AND prisenhed='LOBM' AND tid='2023-01-01'. All 5 filters required.
- Map: context/geo/regioner.parquet — merge on omrade=dim_kode. Exclude omrade=0.