<fact tables>
<table>
id: statusv1
description: 25-45 åriges videregående uddannelse efter uddannelsesstatus, uddannelse, alder, køn, herkomst og tid
columns: uddstat, uddannelse, alder, kon, ietype, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusv2
description: 25-45 årige efter status for videregående uddannelse, alder, forældres højest fuldførte uddannelse og tid
columns: statusvid, alder1, forudd1, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusv3
description: 25-45 årige efter uddannelsesstatus, alder, forældres indkomstniveau og tid
columns: uddstat, alder, forind, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusv4
description: 25-45 årige efter uddannelsesstatus, alder, forældres beskæftigelsesstatus og tid
columns: uddstat, alder, forbesk, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusv5
description: 25-45 årige efter uddannelsesstatus, uddannelse, grundskolens beliggenhed og tid
columns: uddstat, uddannelse, grundbel, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusv6
description: 25-45 årige efter uddannelsesstatus, alder, ungdomsuddannelses karakter og tid
columns: uddstat, alder, grundkar, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All 6 tables cover 25–45 year olds from 2008–2024 with the same uddstat dimension (AA_TOTAL, FULDFOERT, IGANG, AFBRUDT, INGENREG). The tables differ only in which background variable they cross with education status.
- statusv1 is the richest: uddannelse type + alder + kon (gender) + ietype (herkomst/ethnic origin). Use it for gender gaps, herkomst breakdowns, or education-level breakdowns. Only table with gender and herkomst.
- statusv2/3/4 are parental background tables — choose by what you're measuring: statusv2=forældrenes uddannelse, statusv3=forældrenes indkomst, statusv4=forældrenes beskæftigelse. All three are useful for social mobility and inequality analysis.
- statusv5 has grundbel (primary school municipality, 98 communes). Use for geographic analysis of where educational inequalities originate. Note ~19.5% have unknown municipality.
- statusv6 has grundkar (primary school grade in bands). Use to study how early academic performance predicts higher education outcomes. Note ~54% uoplyst overall; most useful filtered to FULDFOERT/IGANG.
- Common gotcha: total codes are NOT uniform across tables. uddstat always uses 'AA_TOTAL', but parent/context dimension totals vary: forudd1='TOT', alder1='IALT' (statusv2); forind='0' (statusv3); forbesk='TOT' (statusv4); grundbel='0' (statusv5); grundkar='0' (statusv6). Check each column's total code before summing.
- All Uoplyst categories are large (~19–20% for parent background, 54% for grundkar). Always decide whether to include or exclude Uoplyst before reporting.