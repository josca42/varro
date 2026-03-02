table: fact.msr1o
description: Detaljeret materialestrømsregnskab, oversigt (Detaljeniveau 1) efter materialetype, kategori og tid
measure: indhold (unit Ton)
columns:
- mater: values [A0=Materialer i alt, A1=Naturressourcer, biomasse (afgrøder, planter, træ, fisk, vildt), A3=Naturressourcer, mineraler (sand, grus, ler mv.), A4=Naturressourcer, fossil energi, CA=Produkter fra landbrug, skovbrug og fiskeri ... WA4=Affald til forbrænding, WA5=Øvrige residualer, udledt til miljø og kloaksystem mv. (balance), WU1=Udledning til luft, energirelaterede, WU2=Udledning til luft, procesrelaterede, ZB=Balance]
- dyrkat: values [ATASUM=Tilgang i alt, ATBSUM=Produktion i brancher i alt, TA1090=Indvinding af naturressourcer, TA0700=Import, TA0150=Residualer fra privat og offentligt forbrug, TA0500=Afhændelser, nedgang i lagre og skrot fra kapitalapparat mv., AAASUM=Anvendelse i alt, AABSUM=Forbrug i produktionen i alt, AA9090=Residualer til miljø, AA6000=Eksport, AA3150=Privat og offentligt forbrug, AA5000=Investeringer og lagerforøgelser mv.]
- tid: date range 2018-01-01 to 2020-01-01
notes:
- dyrkat contains BOTH tilgang (inflow) and anvendelse (outflow) categories: ATASUM=Tilgang i alt, AAASUM=Anvendelse i alt. This is an overview table — do not sum ATASUM + AAASUM, pick one side. Use msr*t for tilgang only, msr*a for anvendelse only.
- mater is hierarchical — filter to a consistent level. A0=total, A1/A3/A4/CA.../WA*/WU*/ZB = main flow categories. Summing all mater codes double-counts.
- Very limited time range: 2018–2020 only (3 years).
