table: fact.uddakt70
description: Uddannelsesaktivitet på lange videregående uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [H70=H70 Lange videregående uddannelser, LVU, H7020=H7020 Pædagogisk, LVU, H702030=H702030 Pædagogik, LVU, H7025=H7025 Humanistisk og teologisk, LVU, H702510=H702510 Humanistisk uden nærmere angivelse, LVU ... H709050=H709050 Medicin, LVU, H709055=H709055 Odontologi, LVU, H709095=H709095 Sundhedsvidenskab i øvrigt, LVU, H7095=H7095 Politi og forsvar mv., LVU, H709525=H709525 Officer i forsvaret, LVU]
- alder: values [TOT=Alder i alt, -13=Under 14 år, 14=14 år, 15=15 år, 16=16 år ... 28=28 år, 29=29 år, 30-34=30-34 år, 35-39=35-39 år, 40-=40 år-]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — every row combination is repeated 3 times (B, F, T). Always filter to one value: fstatus='B' for enrolled students on Oct 1, fstatus='F' for completions, fstatus='T' for new intake. Omitting this filter triples all counts.
- uddannelse has 3 hierarchy levels distinguished by code length: len=3 is the top total (H70 = all LVU), len=5 is sub-category (10 groups), len=7 is specific program (100 programs). Filter to a single level to avoid double-counting. Use LENGTH(uddannelse)=7 for program breakdown or H70 for the overall total.
- herkomst and herkomst1 are cross-tabulated: each herkomst value appears paired with all herkomst1 values and vice versa. To analyze by herkomst (dansk oprindelse/indvandrere/efterkommere), filter herkomst1='TOT'. To analyze by herkomst1 (national region), filter herkomst='TOT'. For overall totals, filter both to TOT.
- kon='10' is the gender total (not 'TOT'). Female=K, Male=M.
- Minimum filter for a clean total: fstatus='B', uddannelse='H70', alder='TOT', herkomst='TOT', herkomst1='TOT', kon='10'.