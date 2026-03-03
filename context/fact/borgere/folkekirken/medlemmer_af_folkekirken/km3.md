table: fact.km3
description: Levendefødte og døde efter sogn, bevægelse og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- bevaegelsev: values [B02=Levendefødte, B03=Døde]
- tid: date range 2007-01-01 to 2025-04-01

notes:
- Simple vital statistics by sogns. bevaegelsev has only 2 mutually exclusive values: B02=Levendefødte (births), B03=Døde (deaths). Always filter to one for a single metric.
- Quarterly data (tid: Jan, Apr, Jul, Oct). Each row = count of births or deaths in that sogns during that quarter. Sum across quarters for annual totals.
- No fkmed column — this covers all residents (members and non-members). This is total births/deaths in sogns area regardless of church membership.
- Natural increase = births - deaths; compute as SUM(CASE WHEN bevaegelsev='B02' THEN indhold ELSE -indhold END) by sogns/period.
- Map: /geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
