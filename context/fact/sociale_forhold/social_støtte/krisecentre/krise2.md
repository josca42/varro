table: fact.krise2
description: Ophold og beboere på krisecentre efter herkomst, varighed, beboerstatus og tid
measure: indhold (unit Antal)
columns:
- herkams: values [T=I alt, 7=Personer med dansk oprindelse, 8=Indvandrere og efterkommere, 0=Uoplyst herkomst]
- kmdr: values [TOT=I alt, 000001=1 døgn, 002005=2-5 døgn, 006030=6-30 døgn, 031119=31-119 døgn, 120365=120-364 døgn, 365000=Hele året, 999999=Uoplyst]
- bebostat: values [1=Ophold, 2=Ophold med børn, 3=Kvinder, 35=Mænd (2024-), 38=Uoplyst køn (voksne) (2024-), 4=Børn]
- tid: date range 2017-01-01 to 2024-01-01

notes:
- herkams=T is the national total; herkams=7 (dansk oprindelse), herkams=8 (indvandrere og efterkommere), and herkams=0 (uoplyst) are mutually exclusive and sum to T. Always exclude herkams='T' when aggregating across origin groups.
- bebostat is a measurement selector — same semantics as krise1: 1=Ophold (stays), 2=Ophold med børn, 3=Kvinder, 4=Børn, 35=Mænd (2024 only), 38=Uoplyst køn (2024 only). Never sum across bebostat values.
- kmdr=TOT is the aggregate across duration bands; the 6 individual bands sum to TOT. Filter to a single kmdr value or use TOT.
- No regional breakdown in this table; use krise1 for regional data.