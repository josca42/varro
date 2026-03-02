table: fact.dncfe
description: Klimarelaterede indikatorer for den finansielle sektors porteføljer efter investor, investering, udstedersektor, udstedelsesland, udledningskategori, værdier og tid
measure: indhold (unit -)
columns:
- investor: values [MFI=- S.122 Penge- og realkreditinstitutter, IF=- S.124 Investeringsfonde, IFG=- - S.124 Investeringsfonde ekskl. S.128+S.129 Forsikrings- og pensionssektorens investeringer, FP=- S.128+S.129 Forsikrings- og pensionssektoren, FPG=- - S.128+S.129 Forsikrings- og pensionssektoren, hvor ejerandele i S.124 Investeringsfonde er gennemlyst]
- invest1: values [100=Alle investeringer i børsnoterede virksomheder, 110=- Aktier, 120=- Virksomhedsobligationer]
- udstedsektor: values [10=Alle sektorer, 11=- Heraf S.11 Ikke-finansielle selskaber som udsteder]
- udstland2: values [Z0=Alle lande, Z9=- Heraf S.2 Udland som udsteder]
- udlkat: values [100=- Scope 1- og 2-udledninger, 110=- - Scope 1-udledninger, 120=- - Scope 2-udledninger, 200=- Scope 3-udledninger]
- vaerdi1: values [FE=Absolutte finansierede udledninger (tusinde ton CO2e, årsniveau), CI=Udledningsintensitet (ton CO2e pr. mio. kr. omsætning), WACI=Vægtet gennemsnitlig udledningsintensitet (ton CO2e pr. mio. kr. omsætning), CF=CO2e-aftryk (ton CO2e pr. mio. kr. investeret), COV=Dækningsgrad (pct.)]
- tid: date range 2018-01-01 to 2025-04-01

notes:
- vaerdi1 is the primary measurement selector with 5 incompatible metrics: FE (tusinde ton CO2e), CI (ton CO2e/mio.kr.omsætning), WACI (ton CO2e/mio.kr.omsætning, value-weighted), CF (ton CO2e/mio.kr.investeret), COV (pct. dækningsgrad). Never sum or average across vaerdi1 values — always filter to one.
- All other columns also function as selectors with aggregate "total" rows: invest1=100 includes 110+120; udstedsektor=10 includes 11; udstland2=Z0 includes Z9. Filter to one level per column.
- udlkat has hierarchy: 100=scope1+2 includes 110 (scope1) and 120 (scope2). 200=scope3 is independent. Don't sum 100+110+120.
- IFG and FPG investors are "look-through" variants of IF and FP — they consolidate investeringsfonde back into the underlying investor sectors. Do not add IFG to IF or FPG to FP.
- For a simple "what is the financed emissions of bank sector": investor='MFI', invest1=100, udstedsektor=10, udstland2='Z0', udlkat=100, vaerdi1='FE'.