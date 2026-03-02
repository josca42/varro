<fact tables>
<table>
id: fra020
description: Fravær efter sektor, køn, fraværsårsag, arbejdsfunktion, fraværsindikator og tid
columns: sektor, kon, fravaer, arbf, fravaer1, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra021a
description: Fravær efter sektor, køn, fraværsårsag, uddannelse, fraværsindikator og tid
columns: sektor, kon, fravaer, uddannelse, fravaer1, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: fra022
description: Fravær efter sektor, køn, fraværsårsag, branche, fraværsindikator og tid
columns: sektor, kon, fravaer, erhverv, fravaer1, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra023
description: Fravær efter sektor, køn, fraværsårsag, område, fraværsindikator og tid
columns: sektor, kon, fravaer, omrade, fravaer1, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra024
description: Fravær efter sektor, køn, fraværsårsag, alder, fraværsindikator og tid
columns: sektor, kon, fravaer, alder, fravaer1, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra025
description: Fravær på statslige arbejdspladser efter område, køn, fraværsårsag, branche (DB07), fraværsindikator og tid
columns: omrade, kon, fravaer, branche07, fravaer1, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra026
description: Fravær på statslige arbejdspladser efter område, køn, fraværsårsag, arbejdsfunktion, fraværsindikator og tid
columns: omrade, kon, fravaer, arbfunk, fravaer1, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra027
description: Fravær på kommunale arbejdspladser efter område, køn, fraværsårsag, arbejdsfunktion, fraværsindikator og tid
columns: omrade, kon, fravaer, arbfunk, fravaer1, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra028
description: Fravær på regionale arbejdspladser efter område, køn, fraværsårsag, arbejdsfunktion, fraværsindikator og tid
columns: omrade, kon, fravaer, arbfunk, fravaer1, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra029
description: Fravær på arbejdspladser i virksomheder og organisationer efter branche (DB07), arbejdsfunktion, køn, størrelsesgruppe, fraværsindikator, fraværsårsag og tid
columns: branche07, arbfunk, kon, strgrupipr, fravaer1, fravaer, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra030
description: Fravær på arbejdspladser i virksomheder og organisationer efter arbejdsfunktion, køn, fraværsindikator, fraværsårsag og tid
columns: arbfunk, kon, fravaer1, fravaer, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: fra031
description: Fravær i forbindelse med egen sygdom efter sektor, køn, fraværsindikator, periodelængde og tid
columns: sektor, kon, fravaer1, periodelg, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: ligehb11
description: Anmeldte arbejdsulykker efter branche, køn og tid
columns: branche, kon, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: ligefi8
description: Ligestillingsindikator for fraværsdagsværk ved barns sygdom (gennemsnitlig) efter indikator, sektor, indkomst og tid
columns: indikator, sektor, indkom, tid (time), indhold (unit Antal)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: ligefi9
description: Ligestillingsindikator for fraværsdagsværk ved barns sygdom (gennemsnitlig) efter indikator, sektor, branche og tid
columns: indikator, sektor, branche, tid (time), indhold (unit Antal)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: ligehi8
description: Ligestillingsindikator for fraværsdagsværk ved egen sygdom (gennemsnitlig) efter indikator, sektor, arbejdsfunktion, alder og tid
columns: indikator, sektor, arbfunk, alder, tid (time), indhold (unit Antal)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: ligehi9
description: Ligestillingsindikator for fraværsdagsværk ved egen sygdom (gennemsnitlig) efter indikator, sektor, arbejdsfunktion, familietype og tid
columns: indikator, sektor, arbfunk, famtyp, tid (time), indhold (unit Antal)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: ligehi11
description: Ligestillingsindikator for anmeldte arbejdsulykker efter indikator, branche og tid
columns: indikator, branche, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
</fact tables>
notes:
- **fravaer1 is a measurement-type selector present in all fra0XX tables.** It repeats every dimension combination 8 times (fraværsprocent, fraværsdagsværk pr. ansat, fraværsperioder pr. ansat, kalenderdage pr. periode, fuldtidsansatte, helårsansatte, fraværsperioder antal, fraværsdagsværk antal). Always filter fravaer1 to one value or results will be meaningless aggregates.
- **fra020-fra024 and fra029-fra031 cover all sectors** (use sektor to filter). fra025/fra026 = statslige workplaces only, fra027 = kommunale only, fra028 = regionale only.
- **Which table to use by breakdown dimension:**
  - By arbejdsfunktion (job function): fra020 (all sectors, disco niveau 1-2), fra026 (stat, niveau 4), fra027 (kommuner, niveau 4), fra028 (regioner, niveau 4), fra030 (virksomheder, niveau 4), fra029 (virksomheder, niveau 1-2 + branche)
  - By branche/erhverv: fra022 (all sectors, letter+numeric codes), fra025 (stat, 11 special codes), fra029 (virksomheder, DB07 letters)
  - By region: fra023 (all sectors, 5 regioner), fra025/fra026/fra028 (niveau 1 regions), fra027 (kommuner)
  - By uddannelse: fra021a (all sectors, H10-H90 coding, from 2015)
  - By alder: fra024 (all sectors, 10 age groups)
  - By periodelænde (sickness spell duration): fra031 (own sickness only)
- **ligehb11** = raw count of reported work accidents by branche (letter codes, DB07) + kon, through 2024.
- **ligehi11** = accident rate (per mio. arbejdstimer) by branche + indikator (men/women/difference). Use for gender comparison of accident risk.
- **ligefi8/ligefi9** = gender gap in child-sickness absence: ligefi8 by income bracket, ligefi9 by branche (10 industry groups). Both show average fraværsdagsværk for men/women/difference.
- **ligehi8/ligehi9** = gender gap in own-sickness absence: ligehi8 by job function + age, ligehi9 by job function + family type.
- All ligeXX tables use indikator as a gender-comparison selector (LAV1/LAV2/LAV3 or M111/K111/F111). Always filter to one indikator value.
- fra021a starts in 2015; all other fra0XX and ligeXX tables start in 2013 (ligehb11 from 2015 through 2024).
- Map: fra023, fra025, fra026, fra028 support regional choropleth (niveau 1, 5 regioner) via context/geo/regioner.parquet — merge on omrade=dim_kode. fra027 supports kommune-level choropleth (niveau 3) via context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade='0' in all cases.
