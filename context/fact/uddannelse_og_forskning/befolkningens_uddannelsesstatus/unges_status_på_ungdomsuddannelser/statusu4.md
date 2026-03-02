table: fact.statusu4
description: 18-25 årige efter uddannelsesstatus, alder, forældres beskæftigelsesstatus og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- alder: values [IALT=Alder i alt, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25=25 år]
- forbesk: values [TOT=I alt, BEGGE=Begge forældre beskæftiget, EN=En forælder beskæftiget, INGEN=Ingen forælder beskæftiget, UOPLYST=Uoplyst]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- No dimension joins — all columns have inline values. forbesk=TOT is the total. 4 employment categories: BEGGE (both parents employed), EN (one parent employed), INGEN (no parent employed), UOPLYST (unknown).
- 3 dimension columns (uddstat, alder, forbesk). To get counts by parental employment status: filter uddstat='AA_TOTAL', alder='IALT', then group by forbesk (optionally exclude UOPLYST).
- No uddannelse column — shows education status by parental employment only. For type-of-education detail use statusu2.