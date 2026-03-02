table: fact.ror11
description: Transport i rørledninger efter produkt, enhed og tid
measure: indhold (unit -)
columns:
- produkt: values [180=Rørtransport i alt, 190=Naturgas i alt, 200=Naturgas til udlandet, 210=Råolie inkl. vand, 220=Råolie ekskl. vand]
- enhed: values [75=1000 ton, 76=Mio. tonkm]
- tid: date range 1982-01-01 to 2024-01-01

notes:
- enhed is a measurement selector — every produkt/tid row appears twice, once for enhed=75 (1000 ton) and once for enhed=76 (Mio. tonkm). Always filter to one unit: WHERE enhed=75 or WHERE enhed=76.
- produkt codes are NOT all additive. produkt=180 (Rørtransport i alt) = 190 + 210 exactly. produkt=200 (Naturgas til udlandet) and produkt=220 (Råolie ekskl. vand) are supplementary views NOT included in 180 — summing all 5 produkt codes double-counts. To get total pipeline transport use produkt=180; to break it into gas vs oil use 190 and 210.
- produkt=200 (Naturgas til udlandet) can exceed 190 (Naturgas i alt) because it measures transit volumes through Danish pipelines to foreign countries — a different scope than domestic gas transport.
- Small table (10 produkt×enhed combinations, ~43 years). No dimension joins needed.