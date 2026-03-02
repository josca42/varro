table: fact.statusv4
description: 25-45 årige efter uddannelsesstatus, alder, forældres beskæftigelsesstatus og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- alder: values [IALT=Alder i alt, 25=25 år, 26=26 år, 27=27 år, 28=28 år ... 41=41 år, 42=42 år, 43=43 år, 44=44 år, 45=45 år]
- forbesk: values [TOT=I alt, BEGGE=Begge forældre beskæftiget, EN=En forælder beskæftiget, INGEN=Ingen forælder beskæftiget, UOPLYST=Uoplyst]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- forbesk total is 'TOT'. Filter forbesk='TOT' and alder='IALT' and uddstat='AA_TOTAL' for grand total.
- forbesk values are mutually exclusive and sum to TOT: BEGGE (both parents employed, ~55%), EN (one parent, ~19%), INGEN (none, ~7%), UOPLYST (unknown, ~20%).
- Simplest table in the subject — 3 substantive forbesk categories plus UOPLYST. Clean for comparative analysis of employment background vs education status.