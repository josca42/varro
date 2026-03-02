table: fact.cfabnp
description: FoU udgifter i pct. af BNP efter pct af BNP og tid
measure: indhold (unit Pct. af bnp)
columns:
- pctbnp: values [0=I alt, 101=Erhvervslivet, 102=Den offentlige sektor]
- tid: date range 1997-01-01 to 2023-01-01
notes:
- pctbnp='0' = I alt (total R&D as % of BNP). pctbnp='101' = erhvervslivet share, pctbnp='102' = offentlig sektor share. These are independent rates, not sub-components — '101'+'102' ≠ '0' (they may not sum to total due to overlaps or rounding).
- indhold is already a percentage of BNP — never sum across pctbnp codes.
- Longest time series for R&D intensity: starts 1997. Useful for tracking Denmark's R&D-to-GDP ratio trend.
