<fact tables>
<table>
id: forsk21
description: Forskningsbiblioteker med særlige forpligtelser efter bibliotek, aktivitet og tid
columns: bib2, aktivi, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: forsk22
description: Økonomi på forskningsbiblioteker med særlige forpligtelser efter bibliotek, aktivitet og tid
columns: bib2, aktivi, tid (time), indhold (unit 1.000 kr.)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: forsk23
description: Udlån på forskningsbiblioteker med særlige forpligtelser efter bibliotek, opgørelse, modtagertype og tid
columns: bib2, opgoer1, modtag, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: forsk24
description: Bestand af fysiske materialer på forskningsbiblioteker med særlige forpligtelser efter bibliotek, materialetype og tid
columns: bib2, mater, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: forsk6
description: Interurbanindlån på forskningsbiblioteker med særlige forpligtelser efter bibliotek, kilde og tid
columns: bib2, kild, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: sbs2
description: Sammenlignende forskningsbiblioteksstatistik efter bibliotek, nøgletal og tid
columns: bib2, bnogle, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: forsk5c
description: Bestand og brug af elektroniske ressourcer på forskningsbiblioteker med særlige forpligtelser efter bibliotek, opgørelse, elektronisk materialetype, placering og tid
columns: bib2, opgoer1, matypelek, placering, tid (time), indhold (unit Antal)
tid range: 2014-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All tables cover 2009–2024 annually, except forsk5c which only starts in 2014.
- The forsk series (forsk21/22/23/24/6/5c) covers "forskningsbiblioteker med særlige forpligtelser" (libraries with special obligations, bib2=82xxx, total=82010). sbs2 covers all research libraries (bib2=80xxx, total=80010) — broader scope, different bib2 coding.
- Table by topic: forsk21=general activities (hours, area, visitors, staff), forsk22=economy (1.000 kr.), forsk23=loans by recipient type, forsk24=physical materials stock, forsk6=interurban loans received (indlån), forsk5c=electronic resources (stock and usage).
- sbs2 is the comparative KPI table with 25 summary metrics across all research libraries — useful for cross-library benchmarking but units are mixed (counts and 1.000 kr. within the same table).
- All tables have bib2 aggregate totals (82010 or 80010). All aktivi/bnogle/mater/kild columns contain independent metrics — never sum across them unless specifically aggregating raw counts with no aggregate present (e.g. modtag in forsk23, mater in forsk24).
- forsk6.kild=19169 is a pre-computed total — do not add it to the component codes 19170–19173.
- forsk22 warning: wage code 13125 (udbetalt til beskæftigelsesordninger) may be a sub-item of 13120 (løn) — verify before summing.