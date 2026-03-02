table: fact.pl1
description: Bedrifter efter enhed, præcisionsteknologi og tid
measure: indhold (unit -)
columns:
- enhed: values [ANTAL=Bedrifter (antal), AREAL=Samlet dyrket areal (ha)]
- praetek: values [100=Alle bedrifter med dyrket areal, 110=Bedrifter med præcisionsteknologi, 120=Bedrifter uden præcisionsteknologi, 130=Fotos fra satelitter eller droner, 140=Traktor eller mejetærsker med RTK-GPS, 150=Software til planlægning af og dokumentation af varieret kvælstofbehov, 160=Sektionsstyring i alt, 162=Sektionsstyring til spredning af planteværn (2024- ), 164=Sektionsstyring til spredning af handelsgødning (2024- ), 170=Afgrødesensorer på traktorer eller maskiner, 172=Selvkørende maskiner eller anden robotteknologi]
- tid: date range 2018-01-01 to 2025-01-01

notes:
- enhed is a measure-type selector: ANTAL (farm count) or AREAL (ha). Always filter to one.
- praetek has two tiers: top-level summary (100=Alle, 110=Med præcisionsteknologi, 120=Uden præcisionsteknologi) and specific technology types (130-172). The specific types are NOT mutually exclusive — a single farm can have multiple technologies (RTK-GPS AND section control AND sensors). Summing 130-172 overcounts. Use codes 100/110/120 for summary counts; treat 130-172 as independent binary questions ("how many farms use X?").
- Codes 162 and 164 (specific sektionsstyring types) were introduced in 2024 surveys — only present from 2024 onwards.
- National only, no regional breakdown.