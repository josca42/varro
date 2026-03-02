table: fact.dnrentd
description: Rentesatser og aktieindeks (dagsobservationer) efter instrument, land, opgørelsesmetode og tid
measure: indhold (unit Pct.)
columns:
- instrument: values [ODKNAA=Nationalbankens rente - Diskonto (Aug. 1987-), OFONAA=Nationalbankens rente - Folioindskud (Aug 1987- ), OIRNAA=Nationalbankens rente - Udlån (Apr. 1992-), OIBNAA=Nationalbankens rente - Indskudsbeviser (Apr. 1992-), DESNAA=DESTR Referencerente, DEONAA=DESTR Omsætning , DEKNAA=DESTR Koncentrationsmål, DEMNAA=DESTR Beregningsmetode, PDRNAA=Referencerente - preDESTR, rentesats (marts 2017-marts 2022), PDONAA=Referencerente - preDESTR , omsætning (marts 2017-marts 2022)]
- land: values [DK=DK: Danmark]
- opgoer: values [E=Daglige renter (procent), A=Gennemsnit (procent), T=Omsætning (mio. kroner)]
- tid: date range 1983-05-10 to 2025-10-30
notes:
- opgoer is a measurement selector: E=daily rates (pct), A=daily average (pct), T=turnover (mio. kr.). Always filter to one value — mixing them silently combines incompatible units.
- instrument codes carry their own time ranges in the label. Many instruments start in 1987 or later despite the table going back to 1983. Expect NULLs or missing rows before an instrument's start date, not zeros.
- DESTR instruments (DESNAA, DEONAA, DEKNAA, DEMNAA) are active from 2022 onwards; PDRNAA/PDONAA cover 2017-2022 as the pre-DESTR reference rate predecessor.
- land is only DK — no filter needed but it is present in the schema.
