table: fact.statusv5
description: 25-45 årige efter uddannelsesstatus, uddannelse, grundskolens beliggenhed og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- uddannelse: values [TOT=I alt, H00=Ingen ungdomsuddannelse, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- grundbel: values [0=Hele landet, 101=København, 147=Frederiksberg, 155=Dragør, 185=Tårnby ... 840=Rebild, 787=Thisted, 820=Vesthimmerlands, 851=Aalborg, 98=Kommune ukendt]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- grundbel is the municipality where the person attended primary school (grundskole), not their current residence. Codes are post-2007 reform kommunekoder (101–860, all 98 municipalities present).
- grundbel='0' is the national total. grundbel='98' is "Kommune ukendt" (~19.5% of population, ~312k of 1.6M in 2024). The 98 municipality codes plus '98' (unknown) sum exactly to '0'.
- Two dimensions with totals: uddstat='AA_TOTAL' and uddannelse='TOT'. Filter both to get a single count per municipality.
- Use ColumnValues("statusv5", "grundbel") to get the municipality code-to-name mapping (all 98 communes listed inline). No dim table join needed.
- Useful for geographic analysis of higher education completion by childhood municipality — where you grew up predicts your education outcome.
- Map: /geo/kommuner.parquet — merge on grundbel=dim_kode. Exclude grundbel IN (0, 98).