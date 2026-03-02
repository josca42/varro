table: fact.regr31
description: Regionernes regnskaber efter region, hovedkonto, dranst, art, prisenhed og tid
measure: indhold (unit 1.000 kr.)
columns:
- regi07: join dim.nuts on regi07=kode; levels [1]
- funk1: values [11001=1.10.01 Somatiske sygehuse, 11002=1.10.02 Psykiatriske sygehuse og afdelinger, 12010=1.20.10 Almen lægehjælp, 12011=1.20.11 Speciallægehjælp, 12012=1.20.12 Medicin ... 55576=5.55.76 Anden langfristet gæld med udenlandsk kreditor, 55578=5.55.78 Gæld vedr. kvalitetsfondsinvesteringer, 57578=5.75.78 Kurstab og kursgevinster i øvrigt, 58095=5.80.95 Refusion af købsmoms, 59099=5.90.99 Overførsel - Renter m.v.]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 7=7 Finansiering]
- art: values [UE=Udgifter excl. beregnede omkostninger, UI=Udgifter incl. beregnede omkostninger, TOT=I alt (netto), I=Indtægter, S0=0 Beregnede omkostninger ... S9=9 Interne udgifter og indtægter, 91=9.1 Overførte lønninger, 92=9.2 Overførte varekøb, 94=9.4 Overførte tjenesteydelser, 97=9.7 Interne indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- regi07 joins dim.nuts. Code 0 = national total (not in dim.nuts); codes 81-85 = 5 regions at niveau=1. JOIN filters out the national row automatically.
- funk1 has 110 detailed sub-function codes (e.g. 11001=Somatiske sygehuse, 12010=Almen lægehjælp, 21050=Dag- og døgntilbud). There is no total/aggregate funk1 code — use regr11 if you only need the 5 high-level sectors. Use ColumnValues("regr31", "funk1") to browse available codes.
- prisenhed is a measurement selector: LOBM=1.000 kr., INDL=kr. per inhabitant. Always filter to one — silently doubles all sums if not filtered.
- art has 52 values with the same hierarchy as regr11 (TOT, UE, UI, I, S0-S9, numeric 00-97). Filter to a single aggregate value; never SUM across all art values.
- dranst has 5 account types. Same pitfall as regr11: summing across all dranst mixes operating and capital flows.
- For detailed breakdown of health expenditure by region: filter funk1 to 1xxxx codes, dranst=1, art='UE', prisenhed='LOBM'.
- Map: context/geo/regioner.parquet — merge on regi07=dim_kode. Exclude regi07=0.