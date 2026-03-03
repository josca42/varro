<fact tables>
<table>
id: idrfin01
description: Kommunale udgifter (1000 kr.) til idræt efter område, funktion, dranst og tid
columns: omrade, funktion, dranst, tid (time), indhold (unit 1.000 kr.)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: idrfin02
description: Kommunale udgifter (Kr.) pr. indbygger til idræt efter område, funktion, dranst og tid
columns: amt, funktion, dranst, tid (time), indhold (unit Kr. pr. indb.)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: idroeko1
description: Idrætsbranchernes økonomiske nøgletal efter branche (DB07), nøgletal og tid
columns: branche07, aktp, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: idrudd01
description: Elevtal på fuldtids idrætsuddannelser efter køn, uddannelsestype, status og tid
columns: konams, uddtype, fstatus, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrbes01
description: Idrætsbeskæftigelse efter branche (DB07), køn, alder, nøgletal og tid
columns: branche07, kon, alder, bnogle, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrbes02
description: Idrætsbeskæftigelse efter branche (DB07), funktion, nøgletal og tid
columns: branche07, funktion, bnogle, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrbes03
description: Idrætsbeskæftigelse efter branche (DB07), uddannelsesniveau, nøgletal og tid
columns: branche07, uddniv, bnogle, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrfu11
description: Idrætsforbrug for en gennemsnitshusstand efter forbrugsgruppe og tid
columns: konsumgrp, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrfu12
description: Idrætsforbrug efter forbrugsgruppe, socioøkonomisk status og tid
columns: konsumgrp, socio, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrfu13
description: Idrætsforbrug efter forbrugsgruppe, husstand og tid
columns: konsumgrp, husstand, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrfu14
description: Idrætsforbrug efter forbrugsgruppe, samlet indkomst og tid
columns: konsumgrp, samind, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrfu15
description: Idrætsforbrug efter forbrugsgruppe, boligform og tid
columns: konsumgrp, bolform, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrfu16
description: Idrætsforbrug efter forbrugsgruppe, region og tid
columns: konsumgrp, cl_region, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: idrfu17
description: Idrætsforbrug efter forbrugsgruppe, alder og tid
columns: konsumgrp, alder1, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
</fact tables>
notes:
- Municipal sports spending: idrfin01 has total expenditure (1.000 kr.) by kommune/landsdel; idrfin02 has the same data as per-capita (Kr. pr. indb.). Both cover 2011-2024, both join dim.nuts (niveau 2=landsdele, niveau 3=kommuner). Code 0 in omrade/amt = national total (not in dim.nuts).
- Sports industry economics: idroeko1 covers 4 sports branches (sportsanlæg, sportsklubber, fitnesscentre, andre) with 6 economic indicators (omsætning, eksport, import, lønsum, jobs, årsværk). Always filter aktp to one indicator — units differ across values.
- Sports employment (idrbes01/02/03): all three cover the same 4 branches + total (TOTR) for 2015-2023. All three require filtering bnogle to either AARSV or GENST. Choose based on breakdown needed: idrbes01 by gender/age, idrbes02 by job function, idrbes03 by education level.
- Sports education: idrudd01 covers student counts on full-time sports education programs by gender, type, and status. fstatus values (0000/START/SLUT) are not additive — always filter to one.
- Household sports consumption (idrfu11-17): idrfu11 has the detailed subcategory breakdown (IDRFU1-4: tøj/sko, udstyr, spil, medlemskab). idrfu12-17 each slice the same top-level data (konsumgrp: 213/214/1000/SPORT) by a different demographic axis (socioøkonomisk status, husstandstype, indkomst, boligform, region, alder). Do not sum across konsumgrp — units are incompatible. All these tables include 2001=Gennemsnitshusstand as a reference category.
- Common pitfall for branche07 tables (idroeko1, idrbes01-03): branche07='TOTR' is the aggregate total and is not in dim.db. Use it for national sports totals without a JOIN; join dim.db for individual branch breakdowns.
- Map: idrfin01 (total spend) and idrfin02 (per-capita spend) support choropleth maps via /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2).
