<fact tables>
<table>
id: silc10
description: Økonomisk sårbare efter afsavnsmål, baggrundsoplysninger, enhed og tid
columns: afsavn, bagopl, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc100
description: Grunde til uopfyldt behov for læge og tandlæge efter spørgsmål, svarmulighed, enhed og tid
columns: sporg, svar, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc1a
description: Økonomisk sårbare: Andel personer efter afsavnsmål, køn og alder og tid
columns: afsavn, koal, tid (time), indhold (unit Pct.)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: silc20
description: Husstandenes økonomiske afsavn efter afsavnsmål, baggrundsoplysninger, enhed og tid
columns: afsavn, bagopl, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc30
description: Befolkningens økonomiske afsavn efter afsavnsmål, baggrundsoplysninger, enhed og tid
columns: afsavn, bagopl, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc40
description: Slår pengene til efter baggrundsoplysninger, svarmulighed, enhed og tid
columns: bagopl, svar, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc50
description: Generel livstilfredshed efter baggrundsoplysninger, enhed og tid
columns: bagopl, enhed, tid (time), indhold (unit Gns.)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc52
description: Tillid til fremmede efter baggrundsoplysninger, enhed og tid
columns: bagopl, enhed, tid (time), indhold (unit Gns.)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc60
description: Helbredsproblemer efter spørgsmål, baggrundsoplysninger, enhed og tid
columns: sporg, bagopl, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc70
description: Økonomisk byrde af forbrugslån efter baggrundsoplysninger, svarmulighed, enhed og tid
columns: bagopl, svar, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc80
description: Ændring i husstandsindkomst efter spørgsmål, baggrundsoplysninger, svarmulighed, enhed og tid
columns: sporg, bagopl, svar, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc90
description: Ugentlige timer i dagtilbud (0-12 år) efter baggrundsoplysninger, enhed og tid
columns: bagopl, enhed, tid (time), indhold (unit Timer)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: silc1b
description: Boligbyrde: Andel personer efter køn, alder, i hvor høj grad husstanden synes boligudgiften er en byrde og tid
columns: koen, alder, svaerhed1, tid (time), indhold (unit Pct.)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: silc2b
description: Boligbyrde: Andel personer efter socioøkonomisk status, køn, i hvor høj grad husstanden synes boligudgiften er en byrde og tid
columns: socio, koen, svaerhed1, tid (time), indhold (unit Pct.)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: silc3b
description: Boligbyrde: Andel personer efter husstandstype, alder, i hvor høj grad husstanden synes boligudgiften er en byrde og tid
columns: hustyp, alder, svaerhed1, tid (time), indhold (unit Pct.)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: silc4b
description: Boligbyrde: Andel personer efter indkomstgruppe, køn, i hvor høj grad husstanden synes boligudgiften er en byrde og tid
columns: indkomgrp, kon, svaerhed1, tid (time), indhold (unit Pct.)
tid range: 2004-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- Nearly all tables (silc10/20/30/40/60/70/80/100) have an enhed column that acts as a measurement selector — every row combination appears 3 times (percent, count-in-thousands, standard error). Always filter enhed. The std error rows (STD/STDG) are rarely needed unless reporting uncertainty.

- Economic vulnerability / material deprivation has three complementary tables:
  - silc1a (2011–2024, Pct. only): best for trend analysis by gender/broad age; no enhed, no overcounting risk.
  - silc10 (2021–2024): richer demographic breakdown (38 bagopl values across 9 categories) plus enhed selector.
  - silc20 (2021–2024, household level): household deprivations with 11 items (furniture, heating, rent arrears, etc.). Use for household-level questions. bagopl limited to region/income/housing/urbanization.
  - silc30 (2021–2024, personal): 6 personal deprivation items (clothing, shoes, social activities, etc.) at person level.
  In silc20 and silc30 the afsavn items are independent yes/no indicators — not a composite. silc10's A0 is the composite (≥3 of 5).

- Financial difficulty / income:
  - silc40: How well households make ends meet (6-point scale from "very hard" to "very easy"). svar values are mutually exclusive and sum to 100% — good for distributional analysis.
  - silc80: Experienced and expected income changes (HI010/HI040). Use sporg to choose past vs future horizon.
  - silc70: Burden of consumer loan repayments. UDF10=no repayments is a real category.

- Wellbeing:
  - silc50: Life satisfaction (mean score 0–10 by bagopl). Filter enhed='GNS'.
  - silc52: Trust in strangers (mean score 0–10 by bagopl). Same structure as silc50.

- Health:
  - silc60: Three health indicators (poor health / chronic illness / limited by health). Filter sporg to one question, enhed to one unit.
  - silc100: Unmet healthcare needs (doctor vs dentist). GR8=no unmet need dominates (~88%); GR1=cost, GR2=waiting list.

- Childcare:
  - silc90: Average weekly hours in dagtilbud for 0–12-year-olds, by household region/income/housing. Filter enhed='GNS'. Coverage 2021–2024.

- Housing cost burden (longest series, 2004–2024):
  - silc1b: by gender + age (7 bands).
  - silc2b: by socioeconomic status + gender.
  - silc3b: by household type + broad age (3 bands).
  - silc4b: by income quintile + gender. Note: uses column name kon (not koen like silc1b/silc2b).
  In all four: svaerhed1=100 is a dummy (indhold always=100). Use svaerhed1 IN (115,120,125) for the real distribution. Values sum to 100%.

- bagopl groups are NOT additive across categories — they represent separate demographic cuts of the same population. Always pick one bagopl value; never sum across categories.
