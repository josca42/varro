table: fact.km3
description: Levendefødte og døde efter sogn, bevægelse og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- bevaegelsev: values [B02=Levendefødte, B03=Døde]
- tid: date range 2007-01-01 to 2025-04-01
notes:
- Most granular geographic breakdown: individual sogne (~2300+ codes). No dim table join — use the inline code=label values.
- Codes '0' (Uden placerbar adresse) and '9999' (Uden fast bopæl) represent ~7 births per year that cannot be placed geographically. Include them for a complete national total; exclude for a spatial analysis. In 2024: excluding gave 13,810 vs 13,817 including.
- bevaegelsev: same as bev3a — filter to B02 for births, B03 for deaths.
- To aggregate to municipality level, strip the last digits from the 4-digit Sogn code (they embed the municipality code prefix) or join via an external parish→municipality crosswalk.
- Map: context/geo/sogne.parquet — merge on sogn=dim_kode. Exclude sogn IN (0, 9999).
