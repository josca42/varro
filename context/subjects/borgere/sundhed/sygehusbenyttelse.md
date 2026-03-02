<fact tables>
<table>
id: sbr01
description: Sygehusbenyttelse i befolkningen efter kommune, ophold på sygehus, alder, køn og tid
columns: kommunedk, ophold_pa_sygehus, alder, kon, tid (time), indhold (unit Antal)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: sbr02
description: Sygehusbenyttelse i befolkningen efter varighed af ophold på sygehus, hoveddiagnosegruppe, akut/ikke-akut, alder, køn og tid
columns: varighed_af_ophold, diagnosehoved, akutejakut, alder, kon, tid (time), indhold (unit Antal)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: sbr03
description: Sygehusbenyttelse i befolkningen efter nøgletal, antal sygehusophold, alder, køn og tid
columns: bnogle, antal_sygehusophold, alder, kon, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: sbr04
description: Sygehusbenyttelse i befolkningen efter nøgletal, sygehusvæsen, alder, køn og tid
columns: bnogle, sygehusvaesen, alder, kon, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: sbr05
description: Sygehusbenyttelse i befolkningen efter nøgletal, sygehustype, alder, køn og tid
columns: bnogle, syghus, alder, kon, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: sbr06
description: Sygehusbenyttelse i befolkningen efter nøgletal, arbejdsmarkedstilknytning, alder, køn og tid
columns: bnogle, arbknyt, alder, kon, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: sbr07
description: Sygehusbenyttelse i befolkningen efter nøgletal, uddannelse, alder, køn og tid
columns: bnogle, uddannelse, alder, kon, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: sbr08
description: Sygehusbenyttelse i befolkningen efter nøgletal, herkomst, alder, køn og tid
columns: bnogle, herkomst, alder, kon, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- sbr01 is the only table with municipal geography (kommunedk → dim.nuts niveau=3). Use it for regional breakdowns. Also has fine-grained age groups (20 bands) and ophold categories including "persons without a stay".
- sbr02 is the only table with diagnosis groups (ICD-10 chapters) and acute/non-acute classification. Use for disease burden or urgency analysis.
- sbr03 is the only table with number-of-stays breakdown (1, 2, 3-5, ≥6 stays). Use for "frequent hospitalisation" analysis.
- sbr04–sbr08 all share the same bnogle and broad alder scheme (4 age groups), differing only in the secondary breakdown: sygehusvæsen (sbr04), sygehustype public/private (sbr05), arbejdsmarkedstilknytning (sbr06), uddannelse (sbr07), herkomst (sbr08).
- bnogle is a measurement selector present in sbr03–sbr08: each row exists once per metric type (count of persons, %, per-person rate). Always filter to a single bnogle value — failing to do so silently multiplies counts.
- All tables with kon and alder include total codes (00/0000 or TOT). Filter these when not aggregating.
- sbr08 herkomst dim join is broken — codes in the fact table (10/20/30/40) do not match dim.herkomst (1/2/3/9). Use inline labels; do not join dim.herkomst.
- sbr04 and sbr05 have "overlap" categories (persons using both somatic+psychiatric, or both public+private). These overlap with the individual categories — use the "all" code (200500 / 200700) for totals, not a sum.
- Map: sbr01 supports choropleth maps at kommune level — context/geo/kommuner.parquet, merge on kommunedk=dim_kode. Exclude kommunedk=0.