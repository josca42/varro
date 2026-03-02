table: fact.ligeib5
description: Offentligt forsørgede efter køn, alder, ydelsestype, herkomst og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 1629=16-29 år, 3049=30-49 år, 5099=50 år og derover]
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere, TOTLE=Nettoledige, TOTVO=Vejledning og opkvalificering, TOTSB=Støttet beskæftigelse, TOTAN=Barselsdagpenge mv., TOTTB=Tilbagetrækning, TOTYD=Øvrige ydelsesmodtagere]
- herkomst: join dim.herkomst on herkomst=kode [approx]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/herkomst.md
notes:
- herkomst does NOT join dim.herkomst. The column uses a different numeric coding scheme than the dim table (which uses kode 1,2,3,9). Use herkomst values directly: 0=I alt, 10=Dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande.
- herkomst has hierarchical aggregate codes — 0=I alt, 21=Indvandrere i alt (covers 24+25), 31=Efterkommere i alt (covers 34+35). Never sum across all values.
- ydelsestype has broad group codes (TOT, TOTUSU, SU, TOTLE, TOTVO, TOTSB, TOTAN, TOTTB, TOTYD) — fewer levels than auk01. No individual benefit codes.
- alder: only 3 broad groups (16-29, 30-49, 50+) plus TOT. For finer age bands use auk01.
- Annual data to 2024-01-01. For origin breakdowns with regional detail use auk04/auh04.
