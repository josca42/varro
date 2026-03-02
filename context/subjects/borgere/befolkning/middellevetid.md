<fact tables>
<table>
id: hisb7
description: Middellevetid for 0-årige efter køn og tid
columns: kon, tid (time), indhold (unit År)
tid range: 1840 to 2025
</table>
<table>
id: hisbr
description: Middellevetid for 0-årige efter område, køn og tid
columns: omrade, kon, tid (time), indhold (unit År)
tid range: 2000 to 2025
</table>
<table>
id: laby21
description: Middellevetid for 0-årige efter kommunegruppe, køn og tid
columns: komgrp, kon, tid (time), indhold (unit År)
tid range: 2006 to 2025
</table>
<table>
id: hisb77
description: Middellevetid for 0-årige efter område, køn og tid
columns: omrade, kon, tid (time), indhold (unit År)
tid range: 2000 to 2025
</table>
<table>
id: hisbk
description: Middellevetid for 0-årige efter område, køn og tid
columns: omrade, kon, tid (time), indhold (unit År)
tid range: 2000 to 2025
</table>
<table>
id: hisb8
description: Dødelighedstavle (2-års tavler) efter alder, køn, dødelighedstavle og tid
columns: alder, kon, tavle, tid (time), indhold (unit -)
tid range: 1981 to 2025
</table>
<table>
id: hisb9
description: Dødelighedstavle (5-års tavler) efter alder, køn, dødelighedstavle og tid
columns: alder, kon, tavle, tid (time), indhold (unit -)
tid range: 1901 to 2025
</table>
<table>
id: ligehi1
description: Ligestillingsindikator for middellevetid for 0-årige efter indikator og tid
columns: indikator, tid (time), indhold (unit -)
tid range: 1901 to 2025
</table>
<table>
id: ligehi2
description: Ligestillingsindikator for middelrestlevetid for 50-årige efter indikator, familietype og tid
columns: indikator, famtyp, tid (time), indhold (unit -)
tid range: 1996 to 2025
</table>
<table>
id: ligehi4
description: Ligestillingsindikator for middelrestlevetid for 30-årige efter indikator, højest fuldførte uddannelse og tid
columns: indikator, hfudd, tid (time), indhold (unit -)
tid range: 2012 to 2025
</table>
</fact tables>

notes:
- For life expectancy at birth (simple national series): hisb7 goes back to 1840 (M/K only, annual, no rolling periods). ligehi1 goes back to 1901 with a pre-computed gender gap (F2), but uses 2-year rolling periods.
- For life expectancy at birth by geography: three tables at different granularities, all 2000+:
  - hisbr: 5 regioner (dim.nuts niveau=1)
  - hisb77: 11 landsdele (dim.nuts niveau=2)
  - hisbk: ~94 kommuner (dim.nuts niveau=3)
  All three have omrade=0 as a national aggregate not in dim.nuts; all have kon TOT/M/K (filter to one).
- For life expectancy at birth by kommunegruppe: laby21 (2006+), 5 grupper (Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner).
- For full mortality tables (survival curves, age-specific death rates, remaining life expectancy at any age):
  - hisb8: 2-year rolling periods, 1981–2025
  - hisb9: 5-year rolling periods, 1901–2025
  Both have tavle as a measurement-type selector (1=Overlevende, 2=Dødshyppighed, 3=Middellevetid) — always filter tavle to one value.
- For remaining life expectancy broken down by social characteristics:
  - ligehi2: at age 50 by family type (enlige vs par), 1996+, 5-year rolling periods
  - ligehi4: at age 30 by education level, 2012+, 5-year rolling periods
- All tables with kon include either M/K only (hisb7, hisb8, hisb9) or TOT/M/K (all others). Always filter kon to avoid overcounting when TOT is present.
- Map: hisbr (regioner), hisb77 (landsdele), hisbk (kommuner) all support choropleth maps via context/geo/regioner.parquet, context/geo/landsdele.parquet, and context/geo/kommuner.parquet respectively — merge on omrade=dim_kode, exclude omrade=0.