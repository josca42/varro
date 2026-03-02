table: fact.ligefi5
description: Ligestillingsindikator for arbejdstimer for beskæftigede lønmodtagere (gennemsnitlig) efter indikator, alder, familietype og tid
measure: indhold (unit Antal)
columns:
- indikator: values [LA1T=Mænd (timer), LA2T=Kvinder (timer), LA3T=Forskel mellem mænd og kvinder (timer)]
- alder: values [TOT=Alder i alt, -16=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-66=65-66 år, 67-=67 år og derover]
- famtyp: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, F3=Familier med hjemmeboende børn, yngste barn mellem 0-5 år, F4=Familier med hjemmeboende børn, yngste barn 6 år og derover, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, E2=Enlige med hjemmeboende børn, i alt, E4=Enlige med hjemmeboende børn, yngste barn mellem 0-5 år, E3=Enlige med hjemmeboende børn, yngste barn 6 år og derover, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, P2=Par med hjemmeboende børn, i alt, P4=Par med hjemmeboende børn, yngste barn mellem 0-5 år, P3=Par med hjemmeboende børn, yngste barn 6 år og derover, U9=Uoplyst familietype]
- tid: date range 2008-01-01 to 2023-01-01
notes:
- indhold measures average working hours, NOT a count of persons. LA1T=Mænd (timer), LA2T=Kvinder (timer), LA3T=Forskel (timer). Never sum across indikator values.
- Use this table to compare average working hours between men and women by family type and age — e.g. how many fewer hours do women with young children work compared to men.
- famtyp has nested hierarchy — filter to TOT or a single non-overlapping level.
