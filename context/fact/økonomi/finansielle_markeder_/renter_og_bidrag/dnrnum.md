table: fact.dnrnum
description: Nye indenlandske udlån ekskl. kassekreditter o.l. fra MFI-sektoren ekskl. Nationalbanken efter formål, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid), rentefiksering, lånstørrelse og tid
measure: indhold (unit -)
columns:
- formal: values [ALLE=Alle formål, B=Boligformål for udlån til husholdninger, EXB=Ej boligformål for udlån til husholdninger, F=- Forbrugerkredit for udlån til husholdninger, A=- Andet formål for udlån til husholdninger]
- data: values [EFFR=Effektiv rentesats (pct.), FORO=Forretningsomfang (mio. kr.), AAOP=Årlige omkostninger i procent - ÅOP (pct.)]
- indsek: values [1100=1100: Ikke-finansielle selskaber, 1400=1400: Husholdninger, 1410=- 1410: Husholdninger - personligt ejede virksomheder, 1430=- 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: values [Z01=Alle valutaer, DKK=- heraf DKK, EUR=- heraf EUR]
- lobetid1: values [ALLE=Alle løbetider, M1A=Op til og med 1 år, S1A=Over 1 år]
- rentfix1: values [ALLE=Alle rentefikseringsperioder, M1A=- Op til og med 1 år, 1A5A=- Over 1 år og op til og med 5 år, 10A=- Over 5 år og op til og med 10 år, S10A=- Over 10 år]
- laanstr: values [ALLE=Alle lånstørrelser, M75M=- Op til og med 7,5 mio. kr. for udlån til ikke-finansielle selskaber, 2M=-  - Op til og med 2 mio. kr. for udlån til ikke-finansielle selskaber, 75M=-  - Over 2 mio. kr. og op til og med 7,5 mio. kr. for udlån til ikke-finansielle selskaber, S75M=- Over 7,5 mio. kr. for udlån til ikke-finansielle selskaber]
- tid: date range 2003-01-01 to 2025-09-01
notes:
- data is a measurement selector: EFFR=effective rate (pct), FORO=new loan volume (mio. kr.), AAOP=annual percentage rate/ÅOP (pct). Always filter to one — they have incompatible units.
- indsek does NOT include a total (1000). Values: 1100=ikke-finansielle selskaber, 1400=husholdninger, 1410/1430=sub-sectors of husholdninger, 1500=nonprofitinstitutioner. To get all sectors combined, sum 1100+1400+1500 (or filter to non-overlapping codes only — avoid double-counting 1400 and its sub-sectors 1410/1430).
- valuta: Z01=all currencies, DKK and EUR are subsets. Don't sum across them.
- lobetid1, rentfix1, formal, laanstr all have ALLE as total aggregates. Filter all to ALLE for a simple aggregate, or pick one breakdown at a time.
- laanstr buckets are defined for 1100 (non-financial firms) only — codes like M75M, 2M, 75M, S75M are not meaningful for household loans (1400).
- This is new loans (nye udlån) from MFI-sector. For outstanding balances, see dnruum.
