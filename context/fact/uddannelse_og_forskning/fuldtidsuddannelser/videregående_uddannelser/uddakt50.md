table: fact.uddakt50
description: Uddannelsesaktivitet på mellemlange videregående  uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [H50=H50 Mellemlange videregående uddannelser, MVU, H5020=H5020 Pædagogisk, MVU, H502015=H502015 Pædagog, MVU, H502020=H502020 Folkeskolelærer, MVU, H502025=H502025 Andre pædagogiske uddannelser, MVU ... H508940=H508940 Tandplejer og klinisk tandteknik, MVU, H508945=H508945 Andre sundhedsfaglige uddannelser, MVU, H5095=H5095 Politi og forsvar mv., MVU, H509520=H509520 Politi, MVU, H509525=H509525 Officer i forsvaret, MVU]
- alder: values [TOT=Alder i alt, -13=Under 14 år, 14=14 år, 15=15 år, 16=16 år ... 28=28 år, 29=29 år, 30-34=30-34 år, 35-39=35-39 år, 40-=40 år-]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — every row combination is repeated 3 times (B, F, T). Always filter to one value: fstatus='B' for enrolled students on Oct 1, fstatus='F' for completions, fstatus='T' for new intake. Omitting this filter triples all counts.
- uddannelse has 3 hierarchy levels distinguished by code length: len=3 is the top total (H50 = all MVU), len=5 is sub-category (13 groups), len=7 is specific program (49 programs). Filter to a single level to avoid double-counting. Use LENGTH(uddannelse)=7 for program breakdown or H50 for the overall total.
- herkomst and herkomst1 are cross-tabulated: each herkomst value appears paired with all herkomst1 values and vice versa. To analyze by herkomst (dansk oprindelse/indvandrere/efterkommere), filter herkomst1='TOT'. To analyze by herkomst1 (national region), filter herkomst='TOT'. For overall totals, filter both to TOT.
- kon='10' is the gender total (not 'TOT'). Female=K, Male=M.
- Minimum filter for a clean total: fstatus='B', uddannelse='H50', alder='TOT', herkomst='TOT', herkomst1='TOT', kon='10'.