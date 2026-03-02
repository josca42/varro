table: fact.doda1
description: Døde efter dødsårsag, alder, køn og tid
measure: indhold (unit Antal)
columns:
- arsag: values [TOT=I ALT, A01=A-01 Infektiøse inkl. parasitære sygdomme, A02=A-02 Kræft, A03=A-03 Andre svulster (anden neoplasi), A04=A-04 Sygdomme i blod (-dannende) organer, sygdomme, som inddrager immunsystem ... A22=A-22 Hændelser med uvis omstændighed, A23=A-23 Legale interventioner inkl. krigshandlinger (politi, militær, krigstilstand), A23X=A-23x Covid-19 - Corona, A24=A-24 Dødsfald uden medicinske oplysninger, UOPL=Årsag ikke oplyst]
- alder: values [TOT=Alder i alt, 0=0 år, 1-4=1-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-=85 år og derover]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- tid: date range 2007-01-01 to 2022-01-01

notes:
- kon uses numeric codes: 1=Mænd, 2=Kvinder, TOT=I alt — different from dod/fod207 which use M/K.
- alder is grouped (not individual years): 0, 1-4, 5-9, ..., 80-84, 85-. Use 'TOT' for all ages.
- arsag codes: A01–A24 are the 24 standard cause-of-death groups. TOT = sum(A01–A24) + UOPL. A23X (Covid-19) is an extra code already embedded within the standard A01–A24 total — it is NOT additive on top of TOT.
- To avoid overcounting: filter kon to one value and alder to one value when querying a specific cause. All three have total rows.
- Use ColumnValues("doda1", "arsag") to see the full list of 26 arsag codes with labels.