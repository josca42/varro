table: fact.statusv2
description: 25-45 årige efter status for videregående uddannelse, alder, forældres højest fuldførte uddannelse og tid
measure: indhold (unit Antal)
columns:
- statusvid: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- alder1: values [IALT=Alder i alt, 25=25 år, 26=26 år, 27=27 år, 28=28 år ... 41=41 år, 42=42 år, 43=43 år, 44=44 år, 45=45 år]
- forudd1: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser, H90=H90 Uoplyst mv.]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- Column names differ from other statusv tables: statusvid (not uddstat), alder1 (not alder), forudd1 (parent education). Don't assume column names carry over from statusv1/3/4.
- forudd1 total is 'TOT' (not '0' or 'AA_TOTAL'). Filter forudd1='TOT' and alder1='IALT' and statusvid='AA_TOTAL' to get the grand total.
- forudd1 covers full ISCED hierarchy H10–H90: H10=Grundskole, H20=Gymnasiale, H30=Erhvervsfaglige, H35=Adgangsgivende forløb (very few: ~600 in 2024), H40–H80=videregående, H90=Uoplyst mv. (~19.5% of population have unknown parent education).
- Useful for intergenerational mobility analysis: cross-tabulate statusvid with forudd1 to see how parent education predicts child's higher education completion.