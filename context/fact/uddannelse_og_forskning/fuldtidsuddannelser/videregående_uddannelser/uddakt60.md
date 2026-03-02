table: fact.uddakt60
description: Uddannelsesaktivitet på bacheloruddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [H60=H60 Bacheloruddannelser, BACH, H6020=H6020 Pædagogisk, BACH, H602030=H602030 Pædagogik, BACH, H6025=H6025 Humanistisk og teologisk, BACH, H602510=H602510 Humanistisk uden nærmere angivelse, BACH ... H609030=H609030 Folkesundhedsvidenskab, BACH, H609035=H609035 It og sundhedsvidenskab, BACH, H609050=H609050 Medicin, BACH, H609055=H609055 Odontologi, BACH, H609095=H609095 Sundhedsvidenskab i øvrigt, BACH]
- alder: values [TOT=Alder i alt, -13=Under 14 år, 14=14 år, 15=15 år, 16=16 år ... 28=28 år, 29=29 år, 30-34=30-34 år, 35-39=35-39 år, 40-=40 år-]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — every row combination is repeated 3 times (B, F, T). Always filter to one value: fstatus='B' for enrolled students on Oct 1, fstatus='F' for completions, fstatus='T' for new intake. Omitting this filter triples all counts.
- uddannelse has 3 hierarchy levels distinguished by code length: len=3 is the top total (H60 = all BACH), len=5 is sub-category (9 groups), len=7 is specific program (95 programs). Filter to a single level to avoid double-counting. Use LENGTH(uddannelse)=7 for program breakdown or H60 for the overall total.
- herkomst and herkomst1 are cross-tabulated: each herkomst value appears paired with all herkomst1 values and vice versa. To analyze by herkomst (dansk oprindelse/indvandrere/efterkommere), filter herkomst1='TOT'. To analyze by herkomst1 (national region), filter herkomst='TOT'. For overall totals, filter both to TOT.
- kon='10' is the gender total (not 'TOT'). Female=K, Male=M.
- Minimum filter for a clean total: fstatus='B', uddannelse='H60', alder='TOT', herkomst='TOT', herkomst1='TOT', kon='10'.