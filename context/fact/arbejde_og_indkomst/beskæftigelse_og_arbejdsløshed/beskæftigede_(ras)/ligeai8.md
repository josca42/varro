table: fact.ligeai8
description: Ligestillingsindikator for beskæftigede lønmodtagere efter indikator, arbejdstidens omfang, herkomst, familietype, alder og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- arbomfang: values [H=Heltid, D=Deltid]
- herkomst: join dim.herkomst on herkomst=kode [approx]
- famtyp: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, F3=Familier med hjemmeboende børn, yngste barn mellem 0-5 år, F4=Familier med hjemmeboende børn, yngste barn 6 år og derover, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, E2=Enlige med hjemmeboende børn, i alt, E4=Enlige med hjemmeboende børn, yngste barn mellem 0-5 år, E3=Enlige med hjemmeboende børn, yngste barn 6 år og derover, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, P2=Par med hjemmeboende børn, i alt, P4=Par med hjemmeboende børn, yngste barn mellem 0-5 år, P3=Par med hjemmeboende børn, yngste barn 6 år og derover, U9=Uoplyst familietype]
- alder: values [TOT=Alder i alt, -16=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-66=65-66 år, 67-=67 år og derover]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/herkomst.md
notes:
- indhold is a gender indicator, NOT a count. LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel (procentpoint). Never sum across indikator values.
- herkomst does NOT join dim.herkomst — inline codes: TOT=I alt, 1=Dansk oprindelse, 24=Indvandrere fra vestlige, 25=Indvandrere fra ikke-vestlige, 34=Efterkommere fra vestlige, 35=Efterkommere fra ikke-vestlige. Use ColumnValues("ligeai8", "herkomst").
- arbomfang has only H and D — no total.
- famtyp has nested hierarchy — filter to TOT or a single level.
