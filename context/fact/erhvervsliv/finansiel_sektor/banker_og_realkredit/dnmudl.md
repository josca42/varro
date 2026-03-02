table: fact.dnmudl
description: Penge- og realkreditinstitutters udlån til husholdninger og ikke-finansielle virksomheder - lang tidsserie efter datatype, rapporterende institut, sektor, land, valuta og tid
measure: indhold (unit Mio. kr.)
columns:
- data: values [ULTIMONOM=Ultimobalance - nominel værdi (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- rapinst: values [PI=Pengeinstitutter, RI=Realkreditinstitutter]
- sektornat: values [1114=X114: Ikke-finansielle selskaber og husholdninger i alt, 1100=- X100: Ikke-finansielle selskaber, 1400=- X400: Husholdninger, 1410=-  - X410: Husholdninger - personligt ejede virksomheder, 1430=-  - X430: Husholdninger - lønmodtagere, pensionister mv.]
- land: values [A1=Hele verden, DK=DK, X0=Udland i alt]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- Long time series from 2003 covering only husholdninger and ikke-finansielle selskaber (not full sector breakdown).
- data: only 2 values — ULTIMONOM=end-of-period nominal stock (mio. kr.) and KI=index (201501=100). This is nominal value only (no market value). Filter to data='ULTIMONOM' for amounts.
- rapinst: PI=pengeinstitutter, RI=realkreditinstitutter. These are separate views of lending — don't sum if you want combined (use dnmud instead for combined MFI loans).
- sektornat hierarchy: 1114=total (ikke-finansielle selskaber + husholdninger); 1100 and 1400 are sub-sectors; 1410/1430 are sub-categories of husholdninger. Pick one level.
- land: A1=hele verden, DK=Denmark, X0=udland. Only 3 values. For domestic lending: land='DK'.
- valuta: Z01 and X00 are aggregate codes not in dim.valuta_iso. Only 3 valuta values (Z01, DKK, X00 based on audit). Use valuta='Z01' for total.
- For domestic pengeinstitut lending to households: rapinst='PI', data='ULTIMONOM', sektornat='1400', land='DK', valuta='Z01'.