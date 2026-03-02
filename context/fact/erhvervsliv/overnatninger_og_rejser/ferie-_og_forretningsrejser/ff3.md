table: fact.ff3
description: Antal rejser efter formål med rejse, transportmiddel, varighed, destination og tid
measure: indhold (unit Antal)
columns:
- seg: values [6=Ferierejser, 8=Forretningsrejser]
- transmid: values [118=Bil, 125=Tog, 130=Skib, 135=Fly, 145=Bus, 150=Sejlbåd, 155=Cykel, 160=Andre transportmidler]
- kmdr: values [1=Mindre end fire overnatninger, 2=Mindst fire overnatninger]
- destina: values [IALT=Danmark og udlandet i alt, DAN=Danmark, UDLAN=Verden udenfor Danmark]
- tid: date range 2017-01-01 to 2024-01-01

notes:
- indhold is absolute trip count (Antal). This is the only count table in this subject; ff1, ff2, ff4 are all percentages.
- seg must always be filtered: seg=6 (ferierejser) and seg=8 (forretningsrejser) are independent populations. Summing them gives total trips across both types, which is valid only if intentional.
- seg=8 (forretningsrejser) is only available from 2019. seg=6 (ferierejser) goes back to 2017. Filtering without checking this will silently drop years.
- destina=IALT is the aggregate of DAN+UDLAN. Never sum IALT with DAN or UDLAN — that double-counts. Filter to IALT for totals, or use DAN/UDLAN for breakdowns.
- IALT ≠ DAN+UDLAN exactly due to rounding (small discrepancies of ~100 trips out of millions are normal).
- transmid: the doc lists 8 transport modes but only 6 appear in the data (150=Sejlbåd and 155=Cykel are absent — folded into 160=Andre transportmidler). Don't filter for 150 or 155.
- A complete count for one year: SELECT seg, transmid, SUM(indhold) FROM fact.ff3 WHERE destina='IALT' AND tid='2024-01-01' GROUP BY seg, transmid.