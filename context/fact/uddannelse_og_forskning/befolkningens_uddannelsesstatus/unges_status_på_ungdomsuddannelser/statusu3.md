table: fact.statusu3
description: 18-25 årige efter uddannelsesstatus, alder, forældres indkomstniveau og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- alder: values [IALT=Alder i alt, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25=25 år]
- forind: values [0=I alt, 100=Under 300.000 Kr., 101=300 - 399.000 Kr., 102=400 - 499.000 Kr., 103=500 - 599.000 Kr., 104=600 - 699.000 Kr., 105=700 - 799.000 Kr., 106=800 - 899.000 Kr., 107=Over 900.000 Kr., 999=Uoplyst]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- No dimension joins — all columns have inline values. forind=0 is "I alt" (total), forind=999 is "Uoplyst". The 7 income bands (100–107) cover <300k to >900k DKK in 100k increments.
- 3 dimension columns (uddstat, alder, forind). To isolate a specific income group: filter uddstat='AA_TOTAL', alder='IALT', then group by forind (exclude 0 and 999 as needed).
- No uddannelse column — this table shows education status by income bracket only (not broken down by type of education). For type-of-education breakdown use statusu2.
- Note: forind refers to parental income, not the young person's own income.