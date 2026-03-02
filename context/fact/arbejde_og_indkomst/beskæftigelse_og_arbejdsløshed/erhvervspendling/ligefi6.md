table: fact.ligefi6
description: Ligestillingsindikator for pendlingsafstand (gennemsnitlig) for beskæftigede personer efter indikator, familietype, alder og tid
measure: indhold (unit Antal)
columns:
- indikator: values [LA1K=Mænd (km), LA2K=Kvinder (km), LA3K=Forskel mellem mænd og kvinder (km)]
- famtyp: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, F3=Familier med hjemmeboende børn, yngste barn mellem 0-5 år, F4=Familier med hjemmeboende børn, yngste barn 6 år og derover, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, E2=Enlige med hjemmeboende børn, i alt, E4=Enlige med hjemmeboende børn, yngste barn mellem 0-5 år, E3=Enlige med hjemmeboende børn, yngste barn 6 år og derover, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, P2=Par med hjemmeboende børn, i alt, P4=Par med hjemmeboende børn, yngste barn mellem 0-5 år, P3=Par med hjemmeboende børn, yngste barn 6 år og derover, U9=Uoplyst familietype]
- alder: values [TOT=Alder i alt, -16=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-66=65-66 år, 67-=67 år og derover]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- indhold is average commuting distance in km despite the 'unit Antal' label. Values are around 18–26 km — these are km not counts.
- indikator encodes both the gender and the measure: LA1K=average for men (km), LA2K=average for women (km), LA3K=difference (men minus women, km). There is no separate gender column. Never sum across indicators — they are independent averages, not additive categories.
- To get average commute for men overall: WHERE indikator='LA1K' AND famtyp='TOT' AND alder='TOT'.
- famtyp has the same overlapping cross-cuts as ligefb6 (E/P vs F split). Use {TOT}, {E1, P1, U9}, or {F1, F2, U9} for non-overlapping totals. Note ligefi6 uses F3/F4 instead of E3/E4 for the børn-age subcategories.
- alder=TOT is the age aggregate. Filter alder='TOT' unless drilling into age groups.