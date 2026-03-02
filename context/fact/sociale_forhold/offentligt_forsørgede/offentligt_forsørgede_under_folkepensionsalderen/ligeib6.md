table: fact.ligeib6
description: Offentligt forsørgede efter køn, alder, ydelsestype, familietype og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 1629=16-29 år, 3049=30-49 år, 5099=50 år og derover]
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere, TOTLE=Nettoledige, TOTVO=Vejledning og opkvalificering, TOTSB=Støttet beskæftigelse, TOTAN=Barselsdagpenge mv., TOTTB=Tilbagetrækning, TOTYD=Øvrige ydelsesmodtagere]
- famtyp: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn, U9=Uoplyst familietype]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- famtyp has two overlapping hierarchy axes: (a) E1/P1 splits by enlig/par; (b) F1/F2 splits by with/without children. These axes overlap (EUHB appears in both F2 and E1, etc.). Leaf codes are: EUHB, EMHB, PUHB, PMHB, U9. Never mix hierarchy axes in a sum.
- Hierarchy: TOT = E1 + P1 + U9 = F1 + F2 + U9. Within E1: EUHB + EMHB. Within P1: PUHB + PMHB. Within F1: EMHB + PMHB. Within F2: EUHB + PUHB.
- ydelsestype: broad group codes (TOT, TOTUSU, SU, TOTLE, TOTVO, TOTSB, TOTAN, TOTTB, TOTYD).
- alder: only 3 broad groups (16-29, 30-49, 50+) plus TOT.
- Annual data to 2024-01-01.
