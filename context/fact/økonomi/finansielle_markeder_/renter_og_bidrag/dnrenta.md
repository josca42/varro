table: fact.dnrenta
description: Rentesatser og aktieindeks (årsobservationer) efter instrument, land, opgørelsesmetode og tid
measure: indhold (unit Pct.)
columns:
- instrument: values [ODKNAA=Nationalbankens rente - Diskonto (1987-), OFONAA=Nationalbankens rente - Folioindskud (1987), OIRNAA=Nationalbankens rente - Udlån (1992-), OIBNAA=Nationalbankens rente - Indskudsbeviser (1992-), MTNTNX=Pengemarkedsrente - Tomorrow/next (1997-) ... CRO30Y=Obligationsrente - Realkreditobligationer (Annuitetslån), løbetid 30 år (1987-2011), CERNAA=Obligationsrente - Alle stats- og realkreditobligationer (1987-2011), CMRNAA=Obligationsrente - Mindsterenten (1985-2010 ), CKANAA=OMXC-aktieindekset (tidl.KAX) (31.dec.1995=100) (1996-2011), CKXNAA=OMXC20-aktieindekset (tidl.KFX) (3.juli 1989=100) (1994-2011)]
- land: values [DK=DK: Danmark]
- opgoer: values [A=Årsgennemsnit, E=Årsultimo]
- tid: date range 1985-01-01 to 2024-01-01
notes:
- opgoer is a measurement selector: A=annual average, E=year-end value. Always filter to one.
- Most equity index and obligationsrente series end around 2011-2012 (see instrument labels). The table runs to 2024 but many instruments will have no data after 2012.
- land is only DK.
