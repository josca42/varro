table: fact.ligeii6
description: Ligestillingsindikator for offentligt forsørgede efter indikator, alder, ydelsestype, familietype og tid
measure: indhold (unit Pr. 100.000 personer)
columns:
- indikator: values [M1=Mænd (pr. 100.000), K1=Kvinder (pr. 100.000), F1=Forskel mellem mænd og kvinder (point, pr. 100.000)]
- alder: values [TOT=Alder i alt, 1629=16-29 år, 3049=30-49 år, 5099=50 år og derover]
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere, TOTLE=Nettoledige, TOTVO=Vejledning og opkvalificering, TOTSB=Støttet beskæftigelse, TOTAN=Barselsdagpenge mv., TOTTB=Tilbagetrækning, TOTYD=Øvrige ydelsesmodtagere]
- famtyp: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- Rate table (Pr. 100.000 personer), NOT counts. Never sum indhold across rows.
- indikator: M1=mænd rate, K1=kvinder rate, F1=forskel (M1−K1, can be negative). Always filter to one indikator.
- famtyp has two overlapping hierarchy axes (same as ligeib6): E1/P1 (enlig/par) and F1/F2 (with/without children). Leaf codes: EUHB, EMHB, PUHB, PMHB. No U9 in this table.
- For raw counts by family type, use ligeib6.
- Annual data to 2024-01-01.
