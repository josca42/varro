<fact tables>
<table>
id: ror11
description: Transport i rørledninger efter produkt, enhed og tid
columns: produkt, enhed, tid (time), indhold (unit -)
tid range: 1982-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Only one table (ror11): annual pipeline transport 1982–2024 for naturgas and råolie.
- Always filter enhed to a single unit (75=1000 ton or 76=Mio. tonkm) — every row is duplicated across units.
- produkt=180 is the grand total; 190=Naturgas i alt and 210=Råolie inkl. vand are the two components. Use these three for breakdowns. produkt=200 (Naturgas til udlandet, transit volumes) and 220 (Råolie ekskl. vand) are supplementary views — do not sum all 5 codes.