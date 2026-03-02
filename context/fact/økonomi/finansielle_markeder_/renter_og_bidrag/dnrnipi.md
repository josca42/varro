table: fact.dnrnipi
description: Nye indenlandske indlån i pengeinstitutter efter instrument, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid) og tid
measure: indhold (unit -)
columns:
- instrnat: values [PL00NYEINDLAAN=Tidsindskud og repoindlån ekskl. puljer i alt, PL4PNYEINDLAAN= - Tidsindskud ekskl. puljer, PL6PNYEINDLAAN= - Repoindlån ekskl. puljer]
- data: values [EFFR=Effektiv rentesats (pct.), FORO=Forretningsomfang (mio. kr.)]
- indsek: values [1100=1100: Ikke-finansielle selskaber, 1400=1400: Husholdninger, 1410=- 1410: Husholdninger - personligt ejede virksomheder, 1430=- 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: values [Z01=Alle valutaer, DKK=- heraf DKK, EUR=- heraf EUR]
- lobetid1: values [ALLE=Alle løbetider, M1A=Op til og med 1 år, 3M=- Op til og med 3 mdr., 1A=- Over 3 mdr. og op til og med 1 år, S1A=Over 1 år, 2A=- Over 1 år og op til og med 2 år, S2A=- Over 2 år]
- tid: date range 2003-01-01 to 2025-09-01
notes:
- data is a measurement selector: EFFR=effective rate (pct), FORO=new deposit volume (mio. kr.). Always filter to one.
- instrnat codes here have a "NYEINDLAAN" suffix (e.g. PL00NYEINDLAAN, PL4PNYEINDLAAN, PL6PNYEINDLAAN) — unlike the MFI counterpart dnrnim which uses plain codes (PL00, PL4P, PL6P). PL00NYEINDLAAN is the total.
- indsek has no total row. Values: 1100, 1400, 1410, 1430, 1500. Avoid summing 1400 with its sub-sectors 1410/1430.
- lobetid1 has nested aggregates: ALLE=total, M1A includes 3M and 1A; S1A includes 2A and S2A.
- valuta: Z01=all currencies, DKK and EUR are subsets. Don't sum across them.
- This is pengeinstitutter new deposits. For MFI-sector total new deposits, see dnrnim.
