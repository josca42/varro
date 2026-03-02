table: fact.statusv3
description: 25-45 årige efter uddannelsesstatus, alder, forældres indkomstniveau og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- alder: values [IALT=Alder i alt, 25=25 år, 26=26 år, 27=27 år, 28=28 år ... 41=41 år, 42=42 år, 43=43 år, 44=44 år, 45=45 år]
- forind: values [0=I alt, 100=Under 300.000 Kr., 101=300 - 399.000 Kr., 102=400 - 499.000 Kr., 103=500 - 599.000 Kr., 104=600 - 699.000 Kr., 105=700 - 799.000 Kr., 106=800 - 899.000 Kr., 107=Over 900.000 Kr., 999=Uoplyst]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- forind total code is '0' (numeric string), not 'TOT' or 'AA_TOTAL'. Filter forind='0' for national total.
- Income bands are forind 100–107 in ~100k DKK increments: 100=under 300k, 101=300–399k, 102=400–499k, 103=500–599k, 104=600–699k, 105=700–799k, 106=800–899k, 107=over 900k. Bands are mutually exclusive and sum exactly to forind='0'.
- forind=999 (Uoplyst) covers ~20% of the population (324k of 1.6M in 2024). Include or exclude explicitly depending on analysis intent.
- Use for socioeconomic analysis of education outcomes — e.g. compare FULDFOERT rates across parent income bands.