table: fact.dodb1
description: Døde efter dødsårsag, køn og tid
measure: indhold (unit Antal)
columns:
- arsag: values [TOT=ÅRSAGER I ALT, A01=A-01 INFEKTIØSE INKL. PARASITÆRE SYGDOMME I ALT, B001=B-001 Tuberkulose, B002=B-002 Infektion med meningokokker, B003=B-003 AIDS (HIV-sygdom) ... A23X=A-23X COVID-19 - CORONA I ALT, B107X=B-107x Covid-19 - Corona, A24=A-24 DØDSFALD UDEN MEDICINSKE OPLYSNINGER I ALT, B108=B-108 Dødsfald uden medicinske oplysninger, UOPL=ÅRSAG IKKE OPLYST]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- tid: date range 2007-01-01 to 2022-01-01

notes:
- CRITICAL: arsag contains BOTH A-level (24 aggregate groups) AND B-level (100+ specific diseases) codes in the same column. Summing all arsag values will massively double-count because each A-code equals the sum of its B-subcodes. Always filter to one level: either LIKE 'A%' for aggregate groups or LIKE 'B%' for specific diseases.
- Use dodb1 (B-level) when you need fine-grained disease breakdowns; use doda1 for the same data with alder dimension.
- kon uses numeric codes: 1=Mænd, 2=Kvinder, TOT=I alt — same as doda1.
- No alder dimension — for cause-of-death with age breakdown use doda1 instead.
- TOT arsag = sum(A01–A24) + UOPL.