table: fact.msr3o
description: Detaljeret materialestrømsregnskab, oversigt (Detaljeniveau 3) efter materialetype, kategori og tid
measure: indhold (unit Ton)
columns:
- mater: values [A0=Materialer i alt, A110=Naturressourcer, primære afgrøder, A120=Naturressourcer, græs, grønfoder og halm mv., A129=Naturressourcer, anden biomasse, inkl. haveaffald, A130=Naturressourcer, træ, brænde og skovflis ... WA594=Øvrige residualer, human fødevareomsætning og udledning til kloak mv. (balance), WA596=Øvrige residualer, spredning af materialer i miljøet mv. (balance), WU1=Udledning til luft, energirelaterede, WU2=Udledning til luft, procesrelaterede, ZB=Balance]
- dyrkat: values [ATASUM=Tilgang i alt, ATBSUM=Produktion i brancher i alt, TA1090=Indvinding af naturressourcer, TA0700=Import, TA0150=Residualer fra privat og offentligt forbrug, TA0510=Afhændelser og skrot fra kapitalapparat mv., TA0520=Nedgang i lagre, AAASUM=Anvendelse i alt, AABSUM=Forbrug i produktionen i alt, AA9090=Residualer til miljø, AA6000=Eksport, AA3150=Privat og offentligt forbrug, AA5100=Investeringer, AA5200=Forøgelse af lagre mv.]
- tid: date range 2018-01-01 to 2020-01-01
notes:
- dyrkat contains BOTH tilgang (inflow) and anvendelse (outflow) categories: ATASUM=Tilgang i alt, AAASUM=Anvendelse i alt. This is an overview table — do not sum ATASUM + AAASUM, pick one side. Use msr*t for tilgang only, msr*a for anvendelse only.
- mater is hierarchical — filter to a consistent level. A0=total, A1/A3/A4/CA.../WA*/WU*/ZB = main flow categories. Summing all mater codes double-counts.
- Very limited time range: 2018–2020 only (3 years).
