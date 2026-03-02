table: fact.dnbsmis
description: Kortmisbrug efter type, kategori, land, datatype og tid
measure: indhold (unit -)
columns:
- kortype: values [KORT=1. Danske betalingskort, DANK=1.1. Dankort og Co-brandede Dankort, INTDEBK=1.2. Internationale debetkort, INTKREK=1.3. Internationale kreditkort, UDLKORT=2. Udenlandske betalingskort, UDLINTDEBK=2.1. Udenlandske debetkort, UDLINTKREK=2.2. Udenlandske kreditkort]
- misbrug2: values [MIS=1 Misbrug, i alt, MISTS=1.1 Misbrug med tabte eller stjålne kort, MISKHTS=1.1.1 Heraf kontanthævninger, MISFHTS=1.1.2 Heraf i fysiske forretninger (betjent ekspedition), MISFHKTTS=1.1.2.1 Heraf kontaktløse transaktioner, MISF=1.2 Misbrug med falske kort, MISKHF=1.2.1 Heraf kontanthævninger, MISFHF=1.2.2 Heraf i fysiske forretninger (betjent ekspedition), MISIHF=1.3 Misbrug i e-handel]
- nation: values [TOT=I alt, DK=Danmark, UDL=Udland (kun danske kort)]
- data: values [A=Antal, V=Værdi (1.000 kr.), AO=Andel af det samlede antal transaktioner (promille), VO=Andel af den samlede værdi af transaktioner (promille)]
- tid: date range 2016-01-01 to 2025-07-01

notes:
- `data` is a 4-way measurement selector — always filter to exactly one value: A=antal (count), V=værdi (1.000 kr.), AO=andel af antal (promille share of transaction count), VO=andel af værdi (promille share of transaction value). Summing across data values is meaningless.
- misbrug2 is a multi-level hierarchy. MIS=total fraud is the aggregate. Next level: MISTS (lost/stolen), MISF (counterfeit), MISIHF (e-commerce). Sub-levels (MISKHTS, MISFHTS, MISFHF, MISKHF, MISFHKTTS) are finer breakdowns. Never sum MIS together with its children — double-counting. Filter to one level.
- MISFHKTTS (contactless within physical store fraud) has fewer rows than other codes — not reported for all periods/dimensions.
- kortype has two top-level groups: KORT (Danish cards) and UDLKORT (foreign cards), unlike transaction tables that only cover Danish cards. Filter kortype='KORT' for Danish card fraud only.
- nation: TOT=I alt, DK=Denmark, UDL=Abroad (only for Danish cards per description). UDL has significantly fewer rows than DK or TOT — many misbrug2 subtypes are only reported for DK geography.
- Typical query: WHERE data='A' AND nation='TOT' AND misbrug2='MIS' for total fraud counts by card type over time.