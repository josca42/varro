table: fact.orgout11
description: International outsourcing efter firma, branche (DB07 10-grp), funktioner og tid
measure: indhold (unit Antal)
columns:
- firma: values [TOT=Firmaer i alt (Antal), SINT=Firmaer med outsourcing (Antal)]
- branchedb0710: values [TOT=TOT Erhverv i alt, 2=2 Industri, råstofindvinding og forsyningsvirksomhed, 3=3 Bygge og anlæg, 4=4 Handel og transport mv., 5=5 Information og kommunikation, 6=6 Finansiering og forsikring, 7=7 Ejendomshandel og udlejning, 8=8 Erhvervsservice]
- funktioner: values [CTOT=Funktioner i alt, CBF=Kernefunktioner, SBF=Hjælpefunktioner]
- tid: date range 2009 to 2024

notes:
- tid is int4range (survey waves, not annual). The 4 periods are [2009,2012), [2014,2017), [2018,2021), [2021,2024). Filter with: WHERE tid = '[2021,2024)'::int4range
- firma: TOT=all firms in scope, SINT=only firms with international outsourcing. Most outsourcing questions want SINT. Don't mix or sum them.
- funktioner: CTOT is NOT the sum of CBF+SBF. A firm outsourcing both core and support is counted once in CTOT but appears in both CBF and SBF. Use CTOT for total outsourcing firm count; filter to CBF or SBF when analyzing by function type.
- branchedb0710: sectors 2–8 do sum to TOT. Either filter to TOT for a national total, or exclude TOT when grouping by sector.