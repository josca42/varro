table: fact.statusv6
description: 25-45 årige efter uddannelsesstatus, alder, ungdomsuddannelses karakter og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- alder: values [IALT=Alder i alt, 25=25 år, 26=26 år, 27=27 år, 28=28 år ... 41=41 år, 42=42 år, 43=43 år, 44=44 år, 45=45 år]
- grundkar: values [0=I alt, 21=2-4,99, 22=5-8,99, 23=9 eller mere, 99=Uoplyst]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- grundkar total is '0'. Filter grundkar='0' and alder='IALT' and uddstat='AA_TOTAL' for grand total.
- grundkar grades (Danish 7-point scale bands): 21=2–4.99 (low), 22=5–8.99 (mid), 23=9 eller mere (high). These are bands, not the grade itself.
- grundkar=99 (Uoplyst) is very large: ~54% overall (863k of 1.6M in 2024). Breakdown by uddstat: INGENREG has 87% uoplyst (people with no higher education rarely have a grade registered), FULDFOERT has ~35% uoplyst, IGANG ~20%. Exclude 99 when comparing grade distributions across education statuses.
- Most useful filtered to FULDFOERT or IGANG where grade data is more complete. Comparing grade distributions across uddstat reveals selection effects.