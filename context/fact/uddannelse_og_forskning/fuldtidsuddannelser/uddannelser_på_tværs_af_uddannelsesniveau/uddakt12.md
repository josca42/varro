table: fact.uddakt12
description: Uddannelsesaktivitet efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [TOT=I alt, H10=H10 Grundskole, H1010=H1010 Grundskole til og med 6. klasse, H1020=H1020 Grundskole 7.-9. klasse, H1030=H1030 Grundskole 10. klasse ... H8035=H8035 Naturvidenskab, Ph.d., H8039=H8039 Samfundsvidenskab, Ph.d., H8059=H8059 Teknisk videnskab, Ph.d., H8080=H8080 Jordbrug, natur og miljø, Ph.d., H8090=H8090 Sundhedsvidenskab, Ph.d.]
- alder: values [TOT=Alder i alt, -5=-5 år, 6=6 år, 7=7 år, 8=8 år ... 36=36 år, 37=37 år, 38=38 år, 39=39 år, 40-=40 år-]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- No geographic breakdown — national only. Use uddakt10 or uddakt11 for regional analysis.
- herkomst and herkomst1 are cross-classified, not independent. herkomst = origin type (5=Dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst). herkomst1 = country group (1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst). Danish-origin students (herkomst=5) always have herkomst1=1. To get independent breakdowns use herkomst1='TOT' when filtering herkomst, and vice versa. National totals: herkomst='TOT' AND herkomst1='TOT'.
- fstatus is a measurement selector — always filter to exactly one value: B=enrolled Oct 1, F=completed, T=new entrants.
- uddannelse is hierarchical (same as uddakt10): TOT → H10…H80 → sub-codes. Don't mix levels when aggregating.