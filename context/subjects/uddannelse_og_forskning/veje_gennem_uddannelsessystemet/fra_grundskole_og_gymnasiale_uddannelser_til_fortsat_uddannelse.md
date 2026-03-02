<fact tables>
<table>
id: forlob10
description: Fra grundskole til fortsat uddannelse efter afgangsårgang, afgangseksamen, afgangsinstitutionsregion, uddannelsesstatus, statustidspunkt efter afgang, uddannelse, køn, herkomst og tid
columns: afgaarg, afgklas, afgreg, uddstat, statustid, uddannelse, koen, herkomst, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2024-01-01
</table>
<table>
id: forlob15
description: Fra gymnasiale uddannelser til fortsat uddannelse efter afgangsårgang, afgangseksamen, afgangsinstitutionsregion, uddannelsesstatus, statustidspunkt efter afgang, uddannelse, køn, herkomst og tid
columns: afgaarg, afgklas, afgreg, uddstat, statustid, uddannelse, koen, herkomst, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- forlob10 = grundskole graduates (7.–10. klasse, from 2003); forlob15 = gymnasium graduates (STX/HF/HHX/HTX/IB, from 2008). Choose based on the starting education level in the question.
- Both tables track cohorts (afgaarg) longitudinally via statustid (3 months to 19 years after graduation). They are NOT time-series tables — tid is the publication snapshot year, not the analysis year. Always filter tid = '2024-01-01'.
- statustid is never additive. Pick one time point. The values 3, 15, 27, 39, ... (months elapsed) tell you where the cohort stood at that moment.
- Both tables share the same uddstat categories (1=i gang, 2=fuldført, 3=afbrudt, 4=ej påbegyndt) and uddannelse types (TOT, H15–H90). There is no uddstat total row — sum all 4 values to get cohort size.
- Regional breakdown is limited to niveau=1 (5 regioner, afgreg 81–85). afgreg=0 is the national total and does not join dim.nuts.
- Minimum filters to avoid overcounting: tid='2024-01-01', plus one statustid, plus afgklas='TOT', uddannelse='TOT' (or specific value), koen='10', herkomst='0'. Forgetting any of these inflates results.
- Map: both tables support choropleth at région level via context/geo/regioner.parquet — merge on afgreg=dim_kode. Exclude afgreg=0.