table: fact.obesk2
description: Offentligt fuldtidsbeskæftigede lønmodtagere efter sektor og tid
measure: indhold (unit Antal)
columns:
- sektor: join dim.esr_sekt on sektor::text=kode
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/esr_sekt.md
notes:
- SCOPE: Only public sector full-time equivalent employees. No tal column — single measure.
- WARNING: dim.esr_sekt join is broken (0% match). sektor uses 4-digit numeric codes: use ColumnValues("obesk2", "sektor") for labels. Values likely match the lbesk public sector breakdown (stat/regioner/kommuner pattern). Treat as inline.
- obesk2 = ukorrigeret; obesk3 = sæsonkorrigeret (identical structure).
- sektor values confirmed: 1032=Offentlig forvaltning og service, 1015=Stat, 1020=Regioner, 1025=Kommuner, 1030=Sociale kasser og fonde (no total row).
