table: fact.ligeab8
description: Beskæftigede lønmodtagere efter arbejdstidens omfang, herkomst, familietype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- arbomfang: values [TOT1=I alt, H=Heltid, D=Deltid]
- herkomst: join dim.herkomst on herkomst=kode [approx]
- famtyp: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, E2=Enlige med hjemmeboende børn, i alt, E4=Enlige med hjemmeboende børn, yngste barn mellem 0-5 år, E3=Enlige med hjemmeboende børn, yngste barn 6 år og derover, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, P2=Par med hjemmeboende børn, i alt, P4=Par med hjemmeboende børn, yngste barn mellem 0-5 år, P3=Par med hjemmeboende børn, yngste barn 6 år og derover, U9=Uoplyst familietype]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, -16=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-66=65-66 år, 67-=67 år og derover]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/herkomst.md
notes:
- Same structure as ligeab7 but uses herkomst (origin) instead of sektor.
- herkomst does NOT join dim.herkomst — use inline codes: TOT=I alt, 1=Dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande. Use ColumnValues("ligeab8", "herkomst").
- arbomfang has TOT1=I alt (note: TOT1 not TOT), H=Heltid, D=Deltid.
- famtyp has nested hierarchy — see ligeab7 notes. Filter to TOT to avoid double-counting.
- kon has TOT, M, K.
