table: fact.dnfpvale
description: Forsikrings- og pensionssektorens valutaeksponering og -afdækning efter værdier, valuta og tid
measure: indhold (unit Mia. kr.)
columns:
- vaerdi1: values [VALEKS=1. Valutaeksponering i alt, HEDGED=1.1. Afdækket valutaeksponering, DKK=1.1.1. Afdækket til kroner, EUR=1.1.2. Afdækket til euro, USD=1.1.3. Afdækket til dollar, OVR=1.1.4. Afdækket til øvrige valutaer, NONHEDGE=1.2. Uafdækket valutaeksponering]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- tid: date range 2015-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- No virktypnb column — this table covers the entire insurance and pension sector only (no breakdown by company type).
- vaerdi1 is hierarchical: VALEKS (1. total exposure) > HEDGED (1.1 hedged) > DKK (1.1.1), EUR (1.1.2), USD (1.1.3), OVR (1.1.4); VALEKS > NONHEDGE (1.2 unhedged). Never sum all vaerdi1 rows. For total exposure use VALEKS; to split hedged vs unhedged, use HEDGED and NONHEDGE (they sum to VALEKS). DKK/EUR/USD/OVR are children of HEDGED only.
- valuta joins dim.valuta_iso but two codes are custom aggregates: Z01=Alle valutaer ekskl. DKK (all currencies except DKK, the total), Z05=Øvrige valutaer (other currencies). The individual matched currencies are EUR and USD. Use ColumnValues("dnfpvale", "valuta") to see all 4 codes.
- Use valuta='Z01' for total exposure figures. The table shows how much of the sector's foreign currency exposure is hedged and into which target currency (DKK, EUR, USD, or other).