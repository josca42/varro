table: fact.uddakt40
description: Uddannelsesaktivitet på korte videregående uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [H40=H40 Korte videregående uddannelser, KVU, H4020=H4020 Pædagogisk, KVU, H402015=H402015 Pædagog, KVU, H4024=H4024 Medier og kommunikation, KVU, H402415=H402415 Multimediedesign, KVU ... H408940=H408940 Tandplejer og klinisk tandteknik, KVU, H408945=H408945 Andre sundhedsfaglige uddannelser, KVU, H4095=H4095 Politi og forsvar mv., KVU, H409510=H409510 Politi og forsvar uden nærmere angivelse, KVU, H409515=H409515 Fængselsvæsnet, KVU]
- alder: values [TOT=Alder i alt, -13=Under 14 år, 14=14 år, 15=15 år, 16=16 år ... 28=28 år, 29=29 år, 30-34=30-34 år, 35-39=35-39 år, 40-=40 år-]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — every row combination is repeated 3 times (B, F, T). Always filter to one value: fstatus='B' for enrolled students on Oct 1, fstatus='F' for completions, fstatus='T' for new intake. Omitting this filter triples all counts.
- uddannelse has 3 hierarchy levels distinguished by code length: len=3 is the top total (H40 = all KVU), len=5 is sub-category (10 groups e.g. H4024, H4038), len=7 is specific program (28 programs e.g. H402415). Filter to a single level with LENGTH(uddannelse)=7 for program breakdown, or use the len=3 code H40 for the overall total. Mixing levels causes double-counting.
- herkomst and herkomst1 are cross-tabulated: each herkomst value appears paired with all herkomst1 values and vice versa. To analyze by herkomst (dansk oprindelse/indvandrere/efterkommere), filter herkomst1='TOT'. To analyze by herkomst1 (national region: Danmark/Vestlige/Ikke-vestlige), filter herkomst='TOT'. For overall totals, filter both to TOT.
- kon='10' is the gender total (not 'TOT'). Female=K, Male=M.
- Minimum filter for a clean total: fstatus='B', uddannelse='H40', alder='TOT', herkomst='TOT', herkomst1='TOT', kon='10'.