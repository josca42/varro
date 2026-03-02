table: fact.fond14
description: Bevilligede fondsmidler til sundhedsformål efter fondstype, hovedområder og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- homr: values [3010=SUNDHEDSFREMME OG FOREBYGGELSE, 3011=Ulykkesforebyggelse, 3012=Organiseret idræt, 3013=Motion og fritid, 3015=BEHANDLING, 3020=REHABILITERING]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- homr has a TWO-LEVEL HIERARCHY. The uppercase codes (3010=SUNDHEDSFREMME OG FOREBYGGELSE, 3015=BEHANDLING, 3020=REHABILITERING) are aggregate parent categories. The lowercase codes (3011=Ulykkesforebyggelse, 3012=Organiseret idræt, 3013=Motion og fritid) are sub-categories of 3010 only.
- NEVER sum all 6 homr codes — this double-counts. Verified: sum of 3010+3015+3020 ≈ fond01 sundhedsformål total; sum of all 6 = 13% higher due to double-counting 3011+3012+3013 which are already included in 3010.
- For a top-level breakdown: use WHERE homr IN (3010, 3015, 3020).
- For a detailed sub-area breakdown of sundhedsfremme: use WHERE homr IN (3011, 3012, 3013) — but be aware these are sub-components of 3010 and do not cover all of 3010.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.