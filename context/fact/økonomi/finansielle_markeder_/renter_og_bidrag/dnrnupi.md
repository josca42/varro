table: fact.dnrnupi
description: Nye indenlandske udlån ekskl. kassekreditter o.l. fra pengeinstitutter efter formål, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid), oprindelig rentefiksering, lånstørrelse og repoforretninger og tid
measure: indhold (unit -)
columns:
- formal: values [ALLE=Alle formål, B=Boligformål for udlån til husholdninger, EXB=Ej boligformål for udlån til husholdninger, F=- Forbrugerkredit for udlån til husholdninger, A=- Andet formål for udlån til husholdninger]
- data: values [EFFR=Effektiv rentesats (pct.), FORO=Forretningsomfang (mio. kr.), AAOP=Årlige omkostninger i procent - ÅOP (pct.)]
- indsek: values [1100=1100: Ikke-finansielle selskaber, 1400=1400: Husholdninger, 1410=- 1410: Husholdninger - personligt ejede virksomheder, 1430=- 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: values [Z01=Alle valutaer, DKK=- heraf DKK, EUR=- heraf EUR]
- lobetid1: values [ALLE=Alle løbetider, M1A=Op til og med 1 år, S1A=Over 1 år]
- rentfix: values [ALLE=Alle rentefikseringsperioder, M1A=- Op til og med 1 år, S1A=- Over 1 år]
- laanstrrepo: values [ALLEAL00=Alle lånstørrelser for udlån til alle sektorer, ALLEAL00EXAL40=- Heraf ekskl. repoforretninger for udlån til ikke-finansielle selskaber, M75MAL00=- Op til og med 7,5 mio. kr. for udlån til ikke-finansielle selskaber, 2MAL00=-  - Op til og med 2 mio. kr. for udlån til ikke-finansielle selskaber, 75MAL00=-  - Over 2 mio. kr. og op til og med 7,5 mio. kr. for udlån til ikke-finansielle selskaber, M75MAL00EXAL40= -  - heraf ekskl. repoforretninger for udlån til ikke-finansielle selskaber, S75MAL00=- Over 7,5 mio. kr. for udlån til ikke-finansielle selskaber, S75MAL00EXAL40=-  - heraf ekskl. repoforretninger for udlån til ikke-finansielle selskaber]
- tid: date range 2003-01-01 to 2025-09-01
notes:
- data is a measurement selector: EFFR=effective rate (pct), FORO=new loan volume (mio. kr.), AAOP=ÅOP (pct). Always filter to one.
- indsek has no total row (1000 absent). Top-level: 1100=non-financial firms, 1400=husholdninger, 1500=nonprofitinstitutioner. 1410 and 1430 are sub-sectors of 1400 — don't sum 1400 with 1410/1430.
- laanstrrepo encodes both loan size AND whether repos are excluded: ALLEAL00=all sizes, ALLEAL00EXAL40=excl. repoforretninger. Codes like M75MAL00, S75MAL00 are for non-financial firms only. Filter to ALLEAL00 for simplest aggregate.
- rentfix: ALLE=all fixation periods, M1A=up to 1 year, S1A=over 1 year. These two sub-totals cover the full range without overlap.
- valuta: Z01=all currencies, DKK and EUR are subsets. Don't sum across them.
- This is pengeinstitutter new loans only. For MFI-sector new loans, see dnrnum.
