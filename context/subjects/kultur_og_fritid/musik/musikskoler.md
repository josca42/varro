<fact tables>
<table>
id: skolm01
description: Musikskoler efter kommune, nøgletal og tid
columns: komk, aktp, tid (time), indhold (unit -)
tid range: 2021 to 2025
</table>
<table>
id: skolm02a
description: Elevers aktiviteter på musikskoler efter kommune, fag, alder, køn og tid
columns: komk, faget, alder, kon, tid (time), indhold (unit Antal)
tid range: 2021 to 2025
</table>
<table>
id: skolm02b
description: Elever på musikskoler efter kommune, alder, køn og tid
columns: komk, alder, kon, tid (time), indhold (unit Antal)
tid range: 2021 to 2025
</table>
<table>
id: laby41
description: Elevers aktiviteter på musikskoler pr. 1000 indbygger efter kommunegruppe, fag og tid
columns: komgrp, faget, tid (time), indhold (unit Antal)
tid range: 2021 to 2025
</table>
<table>
id: skolm03
description: MGK-elever på musikskoler efter MGK-centre, alder og køn og tid
columns: mgk, alderk, tid (time), indhold (unit Antal)
tid range: 2021 to 2025
</table>
<table>
id: skolm04a
description: Ansattes årsværk på musikskolerne efter kommune, arbejdsfunktion, fagområde og tid
columns: komk, arbfunk, fagomr, tid (time), indhold (unit -)
tid range: 2021 to 2025
</table>
<table>
id: skolm04b
description: Ansatte på musikskolerne efter køn, alder, uddannelse og tid
columns: kon, alder, uddannelse, tid (time), indhold (unit Antal)
tid range: 2021 to 2025
</table>
<table>
id: skolm04c
description: Ansatte på musikskolerne efter køn, alder, arbejdsstedsregion og tid
columns: kon, alder, arbreg, tid (time), indhold (unit Antal)
tid range: 2021 to 2025
</table>
<table>
id: skolm05
description: Musikskolernes økonomi efter kommune, økonomiske nøgletal og tid
columns: komk, oeknogl, tid (time), indhold (unit Kr.)
tid range: 2012 to 2025
</table>
<table>
id: skolm06
description: Talentelever på musikskoler efter kommune, kunstart og tid
columns: komk, kunstart, tid (time), indhold (unit Antal)
tid range: 2022 to 2025
</table>
<table>
id: skolm07
description: Arrangementer på musikskoler efter kommune, arrangementstype, nøgletal og tid
columns: komk, arrangementtype, bnogle, tid (time), indhold (unit Antal)
tid range: 2022 to 2025
</table>
<table>
id: skolm08
description: Korte projekter på musikskoler efter kommune, kunstart, nøgletal og tid
columns: komk, kunstart, bnogle, tid (time), indhold (unit Antal)
tid range: 2022 to 2025
</table>
<table>
id: skolm09
description: Musikskolers samarbejde med dagtilbud efter kommune, kunstart, aldersgruppe, nøgletal og tid
columns: komk, kunstart, agebygroup, bnogle, tid (time), indhold (unit Antal)
tid range: 2022 to 2025
</table>
<table>
id: skolm10
description: Musikskolers samarbejde med folkeskoler efter kommune, kunstart, klassetrin, undervisningskategori, nøgletal og tid
columns: komk, kunstart, klasse, undkat, bnogle, tid (time), indhold (unit Antal)
tid range: 2022 to 2025
</table>
<table>
id: skolm11
description: Musikskolers samarbejde med ungdomsuddannelser og ungdomsskoler efter kommune, kunstart, nøgletal og tid
columns: komk, kunstart, bnogle, tid (time), indhold (unit Antal)
tid range: 2022 to 2025
</table>
<table>
id: skolm12
description: Musikskolers øvrige samarbejde efter kommune, kunstart, formål, nøgletal og tid
columns: komk, kunstart, formal, bnogle, tid (time), indhold (unit Antal)
tid range: 2022 to 2025
</table>
<table>
id: ligeki3a
description: Ligestillingsindikator for elever på musikskoler efter indikator, kommune, alder og tid
columns: indikator, komk, alder1, tid (time), indhold (unit -)
tid range: 2021 to 2025
</table>
</fact tables>

notes:
- For student counts by municipality/age/gender: use skolm02b (unique students, from 2021) or skolm02a (subject enrollments — counts a student enrolled in 3 subjects 3 times). For national/kommunegruppe totals only and a rate per 1,000 inhabitants: use laby41.
- For school characteristics (season length, ownership type, pricing, discounts): use skolm01. aktp is a measurement selector — always filter to one aktp value; each code is a different metric.
- For MGK (pre-conservatory talent track) students: use skolm03. Note alderk mixes age and gender in one column — cannot sum across values.
- For staff: skolm04a=FTE (årsværk) by municipality+function+subject area, skolm04b=headcount by education (no regional breakdown), skolm04c=headcount by work region (5 regioner).
- For school finances (lederløn, lærerløn, tilskud, elevbetaling): use skolm05. Goes back to 2012 — longest series in this subject. oeknogl is a measurement selector; never sum across it.
- For talent students (talentelever) by art form: use skolm06 (from 2022).
- For outreach/collaboration activities (from 2022): skolm07=concerts and events, skolm08=short projects, skolm09=collaboration with dagtilbud (nurseries/kindergartens), skolm10=folkeskole collaboration (most granular: by grade and teaching type), skolm11=youth education collaboration, skolm12=other collaboration by purpose. All these tables have bnogle as a measurement selector — always filter to one bnogle value (e.g. 3070=Deltagende elever) to avoid overcounting.
- For gender equality indicators: use ligeki3a. indhold is a percentage or pp-difference — never sum across indikator values.
- Common pitfall: komk='0' appears in all municipality tables as the national total but is not in dim.kommunegrupper or dim.nuts. Use LEFT JOIN or exclude with WHERE f.komk != '0' depending on whether you want national totals.
- Map: All komk tables (skolm01, skolm02a, skolm02b, skolm04a, skolm05–12, ligeki3a) support choropleth maps via /geo/kommuner.parquet — merge on komk=dim_kode. skolm04c supports /geo/regioner.parquet via arbreg=dim_kode.