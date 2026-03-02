table: fact.dnbsiko
description: Indenlandske kreditoverførsler i kroner efter type, initiering, datatype og tid
measure: indhold (unit -)
columns:
- kredit: values [IALT=1. Indenlandske kreditoverførsler i danske kroner i alt, SINTRA=1.1. Interne overførsler, SINTER=1.2. Straksoverførsler, DINTER=1.3. Intradag-overførsler, KONINTER=1.4. Standardoverførsler, IBNINTER=1.5. Indbetalingskort]
- init: values [IALT=Total, MANU=Manuelt behandlede kreditoverførsler, ELEK=Elektronisk behandlede kreditoverførsler]
- datat: values [A=Antal (1.000 stk.), V=Værdi (mio. kr.)]
- tid: date range 2016-01-01 to 2025-04-01

notes:
- datat is a measurement selector: A=Antal (1.000 stk.) vs V=Værdi (mio. kr.). Always filter to one — every combination repeats for A and V.
- kredit is hierarchical: IALT=total (parent of SINTRA, SINTER, DINTER, KONINTER, IBNINTER). Never sum IALT with its children. The five subtypes are: SINTRA=interne overførsler, SINTER=straksoverførsler, DINTER=intradag, KONINTER=standardoverførsler, IBNINTER=indbetalingskort.
- init: IALT=total (MANU + ELEK). Never sum across init values. In practice the vast majority are ELEK; MANU is a small residual.
- This table is domestic-only (indenlandske) DKK transfers. For cross-border DKK or other currencies, use dnbsvko.
- Simplest aggregate query: SELECT tid, indhold FROM fact.dnbsiko WHERE kredit='IALT' AND init='IALT' AND datat='A' ORDER BY tid;