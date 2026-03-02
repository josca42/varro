table: fact.ligeab7
description: Beskæftigede lønmodtagere efter arbejdstidens omfang, sektor, familietype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- arbomfang: values [TOT1=I alt, H=Heltid, D=Deltid]
- sektor: join dim.esr_sekt on sektor::text=kode [approx]
- famtyp: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, E2=Enlige med hjemmeboende børn, i alt, E4=Enlige med hjemmeboende børn, yngste barn mellem 0-5 år, E3=Enlige med hjemmeboende børn, yngste barn 6 år og derover, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, P2=Par med hjemmeboende børn, i alt, P4=Par med hjemmeboende børn, yngste barn mellem 0-5 år, P3=Par med hjemmeboende børn, yngste barn 6 år og derover, U9=Uoplyst familietype]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, -16=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-66=65-66 år, 67-=67 år og derover]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/esr_sekt.md
notes:
- sektor has a total code: 1000=Sektorer i alt (unlike ras305/307 which lack a total). Also 1015=Stat, 1020=Regioner, 1025=Kommuner, 1030=Sociale kasser og fonde, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit-organisationer, 1050=Uoplyst.
- sektor does NOT join dim.esr_sekt — use inline values.
- arbomfang has TOT1=I alt (note: TOT1 not TOT), H=Heltid, D=Deltid.
- famtyp has a nested hierarchy: TOT (all), then E1=Enlige i alt (contains EUHB and E2), P1=Par i alt (contains PUHB and P2), F1/F2 (families with/without children). Filter to TOT to avoid double-counting across family type levels.
- alder has TOT plus age groups.
- kon has TOT, M, K.
