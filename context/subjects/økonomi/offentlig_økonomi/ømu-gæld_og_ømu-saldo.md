<fact tables>
<table>
id: edp1
description: Offentligt underskud og gæld i EU-landene efter land, funktion, enhed og tid
columns: land, funktion, enhed, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: edp5
description: Danmarks kvartalsvise ØMU-gæld efter funktion og tid
columns: funktion, tid (time), indhold (unit Mia. kr.)
tid range: 2000-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- For EU cross-country comparison (GAELD or SALDO, annual 2000–2024): use edp1. It covers all 27 EU member states plus EU-27 aggregate (B6) and an EU total (I9), with values in EUR, PCT of GDP, and DKK (DK only).
- For the quarterly Danish ØMU-debt time series (most up to date, through Q1 2025): use edp5. It is Denmark-only, single-measure, Mia. kr.
- edp1 requires filtering both enhed (EUR/DKK/PCT) and funktion (SALDO/GAELD) on every query — forgetting either silently inflates sums. edp5 needs no such filtering.
- The unit scales differ: edp1 Danish debt is in Mio. kr., edp5 is in Mia. kr. Don't compare raw values across tables without adjusting for this.