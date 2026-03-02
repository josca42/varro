table: fact.brn12
description: Børns (0-17-årige) familier efter antal børn, børnefamilietype, familietype og tid
measure: indhold (unit Antal)
columns:
- antborn: values [0=0 børn, 1=1 barn, 2=2 børn, 3=3 børn, 4=4 børn, 5=5 børn, 6=6 børn, 7-=7 eller flere børn]
- brnfam: values [112212=Enlig mor med børn og samværsbørn, 112222=Enlig mor med børn, 122212=Enlig mor med samværsbørn, 212221=Enlig far med børn og samværsbørn, 212222=Enlig far med børn ... 322121=Par med fars særbørn samt fars samværsbørn, 322122=Par med fars særbørn, 322211=Par med mors og fars samværsbørn, 322212=Par med mors samværsbørn, 322221=Par med fars samværsbørn]
- famtyp: values [1=Ægtepar med forskelligt køn, 6=Ægtepar med samme køn, 2=Registreret partnerskab, 3=Samlevende par, 4=Samboende par, 5=Enlig]
- tid: date range 2008-01-01 to 2025-01-01
notes:
- No geography dimension — national totals only.
- brnfam contains 37 distinct 6-digit codes encoding a complex family composition (whose children are present: mors egne/særbørn/samværsbørn, fars egne/særbørn/samværsbørn, fælles børn). Use ColumnValues("brn12", "brnfam") to see all codes with labels.
- famtyp describes the adult couple type (ægtepar/samlevende/enlig) independently of brnfam. antborn is the number of children in the family.
- This table counts families (not children). A family with 3 børn appears once with antborn=3, not three times.
