table: fact.dnrnuri
description: Nye indenlandske udlån fra realkreditinstitutter efter datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid), oprindelig rentefiksering, lånstørrelse og tid
measure: indhold (unit -)
columns:
- data: values [AL51EFFR=Effektiv rentesats inkl. bidrag (pct.) (kun nominallån), AL51BIDS=Bidragssats (pct.) (kun nominallån), AL50FORO=Forretningsomfang (mio. kr.), AL50AAOP=Årlige omkostninger i procent - ÅOP (pct.)]
- indsek: values [1100=1100: Ikke-finansielle selskaber, 1400=1400: Husholdninger, 1410=- 1410: Husholdninger - personligt ejede virksomheder, 1430=- 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: values [Z01=Alle valutaer, DKK=- heraf DKK, EUR=- heraf EUR]
- lobetid1: values [ALLE=Alle løbetider]
- rentfix: values [ALLE=Alle rentefikseringsperioder, M1A=- Op til og med 1 år, 1M3M=-  - Variabel og op til og med 3 mdr., 6M=-  - Over 3 mdr. og op til og med 6 mdr., 1A=-  - Over 6 mdr. og op til og med 1 år, 1A5A=- Over 1 år og op til og med 5 år, 2A=-  - Over 1 år og op til og med 2 år, 3A=-  - Over 2 år og op til og med 3 år, 5A=-  - Over 3 år og op til og med 5 år, 10A=- Over 5 år og op til og med 10 år, S10A=- Over 10 år]
- laanstr: values [ALLE=Alle lånstørrelser, M75M=- Op til og med 7,5 mio. kr. for udlån til ikke-finansielle selskaber, 2M=-  - Op til og med 2 mio. kr. for udlån til ikke-finansielle selskaber, 75M=-  - Over 2 mio. kr. og op til og med 7,5 mio. kr. for udlån til ikke-finansielle selskaber, S75M=- Over 7,5 mio. kr. for udlån til ikke-finansielle selskaber]
- tid: date range 2003-01-01 to 2025-09-01
notes:
- data is a measurement selector: AL51EFFR=effective rate incl. bidrag (pct, nominallån only), AL51BIDS=bidragssats (pct, nominallån only), AL50FORO=new loan volume (mio. kr.), AL50AAOP=ÅOP (pct). Always filter to one.
- indsek has no total row. Values: 1100=non-financial firms, 1400=husholdninger, 1410/1430=sub-sectors of 1400, 1500=nonprofitinstitutioner. Avoid double-counting 1400 with its sub-sectors.
- rentfix has granular fixation period categories (1M3M, 6M, 1A, 2A, 3A, 5A, 10A, S10A) plus aggregate ranges (M1A, 1A5A, 10A, S10A at higher level). ALLE=all periods. Be careful not to mix nested sub-totals with leaf values.
- lobetid1 only has ALLE here — no maturity breakdown for realkreditlån in this table.
- valuta: Z01=all currencies, DKK and EUR are subsets. Don't sum across them.
- laanstr codes are defined for non-financial firms (1100) only; not meaningful for husholdninger.
- This is realkreditinstitutter new loans. For pengeinstitutter new loans, see dnrnupi.
