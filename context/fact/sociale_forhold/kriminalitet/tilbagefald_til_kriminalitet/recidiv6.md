table: fact.recidiv6
description: Personer efter køn, alder, uddannelse, varighed til tilbagefald og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder1: values [0=I alt, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- uddannelse: values [TOT=I alt, 10=Grundskole, 20=Gymnasial uddannelse, 35=Erhvervsuddannelse, 40=Videregående uddannelse, 00=Uoplyst uddannelse]
- vartilbage: values [0=I alt, 0=Ingen tilbagefald, 6=I løbet af 6 måneder, 712=Efter 6 måneder og indenfor 1 år, 1324=Efter 1 år og indenfor 2 år]
- tid: date range 2008 to 2024
notes:
- tid is rolling 3-year follow-up windows (starts 2008, one year later than recidiv1-5). Do not sum across overlapping tid values.
- uddannelse has 6 codes (TOT, 10, 20, 35, 40, 00). 00=Uoplyst uddannelse (unknown) is a real category, not an aggregate. TOT=I alt.
- vartilbage=0 means I alt (includes non-recidivists). ColumnValues shows id=0 twice — only one code 0 in data. To select only recidivists: WHERE vartilbage != 0.
- 4 dimension columns all have total rows (TOT/0). Clean total: kon='TOT', alder1=0, uddannelse='TOT', vartilbage=0, single tid.
