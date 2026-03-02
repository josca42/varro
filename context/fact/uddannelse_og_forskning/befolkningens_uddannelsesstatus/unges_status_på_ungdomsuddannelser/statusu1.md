table: fact.statusu1
description: 18-25 åriges ungdomsuddannelser efter uddannelsesstatus, uddannelse, alder, køn, herkomst og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- uddannelse: values [TOT=I alt, H00=Ingen ungdomsuddannelse, H20=H20 Gymnasiale uddannelser, H29=H29 Erhvervsfaglige grundforløb, H30=H30 Erhvervsfaglige uddannelser, H99=Andre højere uddannelser]
- alder: values [IALT=Alder i alt, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25=25 år]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- herkomst: join dim.herkomst on herkomst=kode [approx: Fact uses 0,10,20,30 while dimension uses 1,2,3. Values appear to be fact_value/10=dimension_value]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/herkomst.md

notes:
- herkomst does NOT join directly to dim.herkomst. Fact codes are 0,10,20,30 while dim uses 1,2,3. The mapping is: fact_value / 10 = dim kode (e.g. herkomst=10 → kode=1 "Dansk oprindelse"). herkomst=0 is the "I alt" total, not in the dim. Since there are only 3 categories the dim is rarely needed — filter using the inline codes directly: herkomst IN (10,20,30) for all origins, or e.g. herkomst=20 for indvandrere only.
- 5 dimension columns (uddstat, uddannelse, alder, kon, herkomst) all include total rows. To count people by a single dimension without overcounting, filter all others to their totals: uddstat='AA_TOTAL', uddannelse='TOT', alder='IALT', kon='TOT', herkomst=0.
- uddstat values: AA_TOTAL (all statuses), FULDFOERT (completed), IGANG (ongoing), AFBRUDT (dropped out), INGENREG (no registered education). For a question about completion rates, use FULDFOERT and divide by AA_TOTAL.
- This is the only statusu table with kon and herkomst breakdowns. Use it for gender or origin comparisons.