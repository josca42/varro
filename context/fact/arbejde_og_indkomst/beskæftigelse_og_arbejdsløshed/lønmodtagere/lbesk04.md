table: fact.lbesk04
description: Lønmodtagere (sæsonkorrigeret) efter sektor og tid
measure: indhold (unit Antal)
columns:
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1046=Virksomheder og organisationer, 1050=Uoplyst]
- tid: date range 2008-01-01 to 2025-08-01
notes:
- Sæsonkorrigeret version of lbesk02. Same sektor coding: 1000=total, 1032=Offentlig, 1046=Virksomheder og org., 1050=Uoplyst. Fully inline — do NOT join dim.esr_sekt (0% match).
- No tal column — single measure. Use for time-series trend analysis where seasonality distorts comparisons.
