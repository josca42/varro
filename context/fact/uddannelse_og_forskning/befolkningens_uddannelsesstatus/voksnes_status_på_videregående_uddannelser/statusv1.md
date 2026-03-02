table: fact.statusv1
description: 25-45 åriges videregående uddannelse efter uddannelsesstatus, uddannelse, alder, køn, herkomst og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- uddannelse: values [TOT=I alt, H00=Ingen ungdomsuddannelse, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- alder: values [IALT=Alder i alt, 25=25 år, 26=26 år, 27=27 år, 28=28 år ... 41=41 år, 42=42 år, 43=43 år, 44=44 år, 45=45 år]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- ietype: values [0=I alt, 10=Personer med dansk oprindelse, 20=Indvandrere, 30=Efterkommere]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- 5 dimension columns. To get a single count, filter all non-target dims to their totals: uddstat='AA_TOTAL', uddannelse='TOT', alder='IALT', kon='TOT', ietype='0'. Forgetting any one inflates the result.
- uddstat and uddannelse interact: H00 (ingen ungdomsuddannelse) only appears when uddstat='INGENREG'. H40–H80 only appear with FULDFOERT, IGANG, or AFBRUDT. For a specific uddstat (e.g. FULDFOERT) the education breakdown H40/H50/H60/H70/H80 sums exactly to the TOT row — they are mutually exclusive.
- ietype is herkomst (ethnic origin): 0=I alt, 10=dansk oprindelse, 20=Indvandrere, 30=Efterkommere. Filter ietype='0' unless breaking down by herkomst.
- This is the richest table in the subject — only one with both uddannelse and kon/ietype breakdowns. Use it for gender or herkomst cross-tabulations.