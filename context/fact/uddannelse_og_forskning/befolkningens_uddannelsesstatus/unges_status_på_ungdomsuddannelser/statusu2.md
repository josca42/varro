table: fact.statusu2
description: 18-25 årige efter uddannelsesstatus, uddannelse, alder, forældres højest fuldførte uddannelse og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- uddannelse: values [TOT=I alt, H00=Ingen ungdomsuddannelse, H20=H20 Gymnasiale uddannelser, H29=H29 Erhvervsfaglige grundforløb, H30=H30 Erhvervsfaglige uddannelser, H99=Andre højere uddannelser]
- alder: values [IALT=Alder i alt, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25=25 år]
- forudd1: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser, H90=H90 Uoplyst mv.]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- No dimension joins — all columns have inline values. forudd1 codes follow the standard Danish education classification (H10=grundskole through H80=ph.d.). TOT=I alt is the total.
- 4 dimension columns (uddstat, uddannelse, alder, forudd1) all include total rows. For a simple count by parent education, filter: uddstat='AA_TOTAL', uddannelse='TOT', alder='IALT', then group by forudd1.
- Use this table when the question is about how parental education level affects youth education status. For parental income, use statusu3; for parental employment, use statusu4.