table: fact.dnrentm
description: Rentesatser og aktieindeks (månedsobservationer) efter instrument, land, opgørelsesmetode og tid
measure: indhold (unit -)
columns:
- instrument: values [ODKNAA=Nationalbankens rente - Diskonto (Aug 1987-), OFONAA=Nationalbankens rente - Folioindskud (Aug 1987-), OIRNAA=Nationalbankens rente - Udlån (Apr. 1992-), OIBNAA=Nationalbankens rente - Indskudsbeviser (Apr. 1992-), MTNTNX=Pengemarkedsrente - Tomorrow/next (Jan. 1997-okt. 2015) ... CRO30Y=Obligationsrente - Realkreditobligationer (Annuitetslån), løbetid 30 år (Jan. 1987-nov. 2012), CERNAA=Obligationsrente - Alle stats- og realkreditobligationer (Jan. 1987-nov. 2012), CMRNAA=Obligationsrente - Mindsterenten (Okt. 1985-jun. 2011), CKANAA=OMXC-aktieindekset (tidl.KAX) (31.dec.1995=100) (Jan 1996-nov. 2012 ), CKXNAA=OMXC20-aktieindekset (tidl.KFX) (3.juli 1989=100) (Jan 1994-nov. 2012 )]
- land: values [DK=DK: Danmark]
- opgoer: values [A=Månedsgennemsnit, E=Månedsultimo]
- tid: date range 1985-10-01 to 2025-09-01
notes:
- opgoer is a measurement selector: A=monthly average, E=month-end value. Always filter to one — they represent different aggregation methods for the same instrument series.
- Many instrument series end in 2012 when DST stopped publishing certain rates (CERNAA, CRO30Y, CKANAA, CKXNAA etc.). Filter by instrument start/end dates in labels if your time range extends beyond active periods.
- land is only DK. Monthly data from 1985 but individual instruments start at different dates per their label.
