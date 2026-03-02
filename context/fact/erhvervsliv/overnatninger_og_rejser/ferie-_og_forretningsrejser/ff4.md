table: fact.ff4
description: Ferierejser efter formål med rejse, overnatningsform, varighed, destination og tid
measure: indhold (unit Pct.)
columns:
- seg: values [6=Ferierejser, 8=Forretningsrejser]
- overnatf: values [110=Hoteller og Feriecentre i alt, 140=Camping, 150=Vandrerhjem, 175=Lejet feriehus, 180=Eget feriehus, 185=Familie og venner, 190=Skib og lystbåd, 200=Andre overnatningsformer]
- kmdr: values [1=Mindre end fire overnatninger, 2=Mindst fire overnatninger]
- destina: values [IALT=Danmark og udlandet i alt, DAN=Danmark, UDLAN=Verden udenfor Danmark]
- tid: date range 2017-01-01 to 2024-01-01

notes:
- indhold is percentage share of trips by accommodation type (overnatf). Values sum to ~100 across overnatf for a fixed seg+kmdr+destina+tid. Never sum across overnatf — they're shares.
- seg must always be filtered: seg=6 (ferierejser) covers 2017-2024; seg=8 (forretningsrejser) only covers 2019-2024. Mixing both in a sum gives a meaningless blend of two populations.
- destina=IALT is the aggregate of DAN+UDLAN. Never sum IALT with DAN or UDLAN. Filter to one destina value for any given query.
- overnatf=190 (Skib og lystbåd) for forretningsrejser (seg=8) has only 5 time points instead of 6 — it's missing from some years entirely.
- For business travel (seg=8), hoteller (overnatf=110) dominates strongly (75-90%). For ferierejser (seg=6), the split is more even across accommodation types.
- kmdr splits short vs long trips — filter to one to avoid double-counting.