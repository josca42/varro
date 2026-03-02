<fact tables>
<table>
id: bol101
description: Boliger efter område, beboertype, anvendelse, udlejningsforhold, ejerforhold, opførelsesår og tid
columns: omrade, bebo, anvendelse, udlforh, ejer, opforelsesar, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: bol102
description: Boliger efter område, beboertype, anvendelse, opførelsesår, opvarmning, toiletforhold, badeforhold, køkkenforhold og tid
columns: amt, bebo, anvendelse, opforelsesar, opvarmning, toilet, bad, koekken, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: bol103
description: Boliger efter område, beboertype, anvendelse, antal værelser, boligstørrelse i kvm., husstandsstørrelse og tid
columns: amt, bebo, anvendelse, antvaer, boligstor, husstor, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: bol104
description: Boliger efter område, beboertype, anvendelse, udlejningsforhold, husstandstype, antal børn og tid
columns: amt, bebo, anvendelse, udlforh, hustyp, antborn, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: bol105
description: Boliger efter område, beboertype, anvendelse, opvarmning, toiletforhold, badeforhold, husstandstype, antal børn og tid
columns: amt, bebo, anvendelse, opvarmning, toilet, bad, hustyp, antborn, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: bol106
description: Boliger efter område, enhed, anvendelse og tid
columns: omrade, enhed, anvendelse, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: bolrd
description: Beboede boliger efter udlejningsforhold og tid
columns: udlforh, tid (time), indhold (unit Antal)
tid range: 1930-01-01 to 2025-01-01
</table>
<table>
id: laby45a
description: Andel af familier med sommerhus efter kommunegruppe og tid
columns: komgrp, tid (time), indhold (unit Pct.)
tid range: 2022-01-01 to 2022-01-01
</table>
</fact tables>

notes:
- bol101–bol105 all cover the full boligbestand (occupied + unoccupied + holiday homes) from 2010–2025 at region/landsdel/kommune level (dim.nuts, kode=0=Hele landet). None have aggregate total codes for their categorical dimensions — you always need to filter or SUM explicitly.
- bol101 is the most comprehensive: region × bebo × anvendelse × udlforh × ejer × opforelsesar. Use it when you need ownership type (ejer) or tenancy (udlforh) combined with geography and building type.
- bol102 adds facility quality (opvarmning, toilet, bad, koekken) and construction period. amt joins dim.nuts even though the doc lists inline values. Use for housing quality questions.
- bol103 adds size and occupancy info (antvaer, boligstor, husstor). Use for questions about number of rooms, floor area, or household size per dwelling.
- bol104 adds household composition (hustyp, antborn) with udlforh. Use for family structure × tenancy questions.
- bol105 combines facility info (opvarmning, toilet, bad) with household composition (hustyp, antborn). Use when crossing housing conditions against family type.
- bol106 is the only table with average measures (m² per dwelling, m² per person, persons per dwelling). enhed is a measurement selector — always filter to one enhed value to avoid tripling counts. Has a 'TOT' code for anvendelse. Use for spatial comparison of dwelling sizes or occupancy density.
- bolrd is the only table with pre-2010 data (back to 1930). National level only, owner vs. renter. Use for long-term historical trend analysis.
- laby45a is a single-year (2022) percentage table by kommunegruppe. Very narrow use case: share of families with a holiday home.
- opforelsesar in all tables uses period ranges for pre-2005 (e.g. '1950-1959') and individual years from 2005+. No total code exists — sum all values to aggregate across construction periods.
- Map: bol101–bol106 all support choropleth maps at kommune (niveau 3), landsdel (niveau 2), and region (niveau 1) level via dim.nuts. Use context/geo/kommuner.parquet, landsdele.parquet, or regioner.parquet. bolrd and laby45a have no geographic breakdown.