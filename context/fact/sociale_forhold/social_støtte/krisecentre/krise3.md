table: fact.krise3
description: Ophold og beboere på krisecentre efter alder, varighed, beboerstatus og tid
measure: indhold (unit Antal)
columns:
- alder1: values [IALT=Alder i alt, 1824=18-24 år, 2529=25-29 år, 3039=30-39 år, 4049=40-49 år, 50OV=50 år og derover, 9999=Uoplyst alder]
- kmdr: values [TOT=I alt, 000001=1 døgn, 002005=2-5 døgn, 006030=6-30 døgn, 031119=31-119 døgn, 120365=120-364 døgn, 365000=Hele året, 999999=Uoplyst]
- bebostat: values [1=Ophold, 2=Ophold med børn, 3=Kvinder, 35=Mænd (2024-), 38=Uoplyst køn (voksne) (2024-), 4=Børn]
- tid: date range 2017-01-01 to 2024-01-01

notes:
- alder1=IALT is the total across all age groups. The 6 age bands (1824, 2529, 3039, 4049, 50OV, 9999) are mutually exclusive and sum to IALT. Always exclude alder1='IALT' when aggregating across age groups.
- Age bands cover adults only (18+); bebostat=4 (Børn) also has values per age band, which are the ages of accompanying children.
- bebostat is a measurement selector — same semantics as krise1/krise2: 1=Ophold, 2=Ophold med børn, 3=Kvinder, 4=Børn, 35=Mænd (2024 only), 38=Uoplyst køn (2024 only). Never sum across bebostat values.
- kmdr=TOT is the aggregate; individual duration bands sum to TOT.
- No regional or origin breakdown in this table; use krise1 for region or krise2 for herkomst.