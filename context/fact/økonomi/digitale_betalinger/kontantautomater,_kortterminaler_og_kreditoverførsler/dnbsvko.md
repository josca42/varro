table: fact.dnbsvko
description: Kreditoverførsler i valuta efter type, retning, geografisk dækning, datatype og tid
measure: indhold (unit Antal)
columns:
- kortype: values [IALT=1. Total, DKK=1.1. Kreditoverførsler i kroner (kun grænseoverskridende), SCT=1.2. SEPA kreditoverførsler, QEURO=1.3. Andre overførsler i euro, ekskl. Target2-overførsler, QVALUTA=1.4. Overførsler i andre valutaer]
- ret: values [DEBITOR=Afsendt, KREDITOR=Modtaget]
- geodaek: values [TOT=Total, DK=Indenlandsk, UDL=Grænseoverskridende]
- data: values [A=Antal (1.000 stk.), V=Værdi (mio. kr.)]
- tid: date range 2016-01-01 to 2025-07-01

notes:
- data is a measurement selector: A=Antal (1.000 stk.) vs V=Værdi (mio. kr.). Always filter to one — every combination of kortype/ret/geodaek repeats for both A and V.
- kortype is hierarchical: IALT=total (parent of DKK, SCT, QEURO, QVALUTA). Never sum IALT with its children.
- geodaek: TOT=total, DK=domestic, UDL=cross-border. TOT=DK+UDL, so never sum across geodaek values.
- DKK (kreditoverførsler i kroner) only exists for geodaek=TOT and geodaek=UDL — there is no DKK/DK row. Domestic DKK transfers are covered by a separate table: dnbsiko.
- ret has no totals row: DEBITOR=afsendt, KREDITOR=modtaget are independent perspectives. Don't sum them unless the question specifically asks for combined flow volume.
- Minimal overcounting filter for a simple total: WHERE kortype='IALT' AND geodaek='TOT' AND ret='DEBITOR' AND data='A'.