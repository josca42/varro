table: fact.ligeii5
description: Ligestillingsindikator for offentligt forsørgede efter indikator, alder, ydelsestype, herkomst og tid
measure: indhold (unit -)
columns:
- indikator: values [M1=Mænd (pr. 100.000), K1=Kvinder (pr. 100.000), F1=Forskel mellem mænd og kvinder (point, pr. 100.000)]
- alder: values [TOT=Alder i alt, 1629=16-29 år, 3049=30-49 år, 5099=50 år og derover]
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere, TOTLE=Nettoledige, TOTVO=Vejledning og opkvalificering, TOTSB=Støttet beskæftigelse, TOTAN=Barselsdagpenge mv., TOTTB=Tilbagetrækning, TOTYD=Øvrige ydelsesmodtagere]
- herkomst: values [0=I alt, 10=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- Rate table (pr. 100.000 persons), NOT counts. indhold values should never be summed across rows — each value is an independent rate.
- indikator has 3 values: M1=mænd (rate per 100.000), K1=kvinder (rate per 100.000), F1=forskel (M1 minus K1, can be negative). Always filter to one indikator value. F1 is a derived difference, not a rate.
- herkomst uses the same inline numeric coding as ligeib5 (not dim.herkomst): 0=I alt, 10=Dansk oprindelse, 21=Indvandrere i alt, 24/25=vestlige/ikke-vestlige indvandrere, 31=Efterkommere i alt, 34/35=vestlige/ikke-vestlige efterkommere. Hierarchical aggregates — don't sum across levels.
- For raw counts (Antal) rather than rates, use ligeib5.
- Annual data to 2024-01-01.
