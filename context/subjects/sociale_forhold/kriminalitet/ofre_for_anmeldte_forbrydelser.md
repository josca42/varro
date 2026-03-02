<fact tables>
<table>
id: straf5
description: Ofre for anmeldte forbrydelser efter overtrædelsens art, alder, køn og tid
columns: overtraed, alder, koen, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: ligepb1
description: Ofre for personfarlig kriminalitet efter overtrædelsens art, alder, køn og tid
columns: overtraed, alder, koen, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: ligepi1
description: Ligestillingsindikator for ofre for personfarlig kriminalitet efter overtrædelsens art, alder, indikator og tid
columns: overtraed, alder, indikator, tid (time), indhold (unit Pr. 100.000 personer)
tid range: 2001-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For raw victim counts with full crime-type detail (196 codes, all crime types): use straf5. For personal crime only with a simpler hierarchy (22 LS codes): use ligepb1. For gender-adjusted victimization rates (per 100,000): use ligepi1.
- straf5 and ligepb1/ligepi1 use different coding schemes for crime type: straf5 uses numeric S-suffix codes (1S, 11S, 12S…), ligepb1/ligepi1 use LS-prefix codes (LS1, LS11…). They cannot be joined or compared directly via the code column.
- All three tables cover the same time range (2001–2024, annual) and share the same age bands, but koen codes differ: straf5 uses 1/2/9/TOT while ligepb1 uses M/K/TOT.
- Critical pitfall for all tables: overtraed contains codes at multiple hierarchy levels. Summing across all distinct overtraed values massively overcounts. Always pick one level (e.g. total only, or category level, or leaf level) and filter accordingly.
- All tables have total rows for alder (TOT) and koen (TOT/I alt). Always filter non-target dimensions to their total to avoid overcounting.