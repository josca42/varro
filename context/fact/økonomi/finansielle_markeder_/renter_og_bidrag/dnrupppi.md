table: fact.dnrupppi
description: Pengeinstitutternes udestående indenlandske forretninger fordelt på 10 pct. percentiler efter instrument, indenlandsk sektor og tid
measure: indhold (unit Pct.)
columns:
- instrnat: values [AL00EFFRP90N=Effektiv rentesats (pct.) på udlån i alt, DKK (øvre decil), AL00EFFRP10N=Effektiv rentesats (pct.) på udlån i alt, DKK (nedre decil), PL00EFFRP90ALLE=Effektiv rentesats (pct.) på indlån i alt, DKK (øvre decil), PL00EFFRP10ALLE=Effektiv rentesats (pct.) på indlån i alt, DKK (nedre decil)]
- indsek: values [1100=1100: Ikke-finansielle selskaber, 1400=1400: Husholdninger, 1410=- 1410: Husholdninger - personligt ejede virksomheder, 1430=- 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=1500: Nonprofitinstitutioner rettet mod husholdninger]
- tid: date range 2003-01-01 to 2025-09-01
notes:
- instrnat encodes the metric, direction, and percentile all in one code — these are four independent statistics, not categories that can be summed: AL00EFFRP90N=upper decile (90th pct) on loans, AL00EFFRP10N=lower decile (10th pct) on loans, PL00EFFRP90ALLE=upper decile on deposits, PL00EFFRP10ALLE=lower decile on deposits.
- indsek has no total row. Values: 1100, 1400, 1410, 1430, 1500. Avoid summing 1400 with 1410/1430.
- No valuta column — this is DKK only (implied by the instrument code suffix).
- Use this table to show interest rate dispersion (spread between upper and lower decile) rather than level. A simple query: filter instrnat IN ('AL00EFFRP90N','AL00EFFRP10N') and compute the spread.
