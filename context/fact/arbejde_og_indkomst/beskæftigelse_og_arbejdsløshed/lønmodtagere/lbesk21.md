table: fact.lbesk21
description: Lønmodtagere efter enhed, sektor og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- sektor: join dim.esr_sekt on sektor::text=kode
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/esr_sekt.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- WARNING: dim.esr_sekt join is broken (0% match). sektor uses 4-digit numeric codes (DST internal sector taxonomy), NOT the letter codes in dim.esr_sekt (OFF/VIR/UOP/INT). Treat sektor as inline.
- sektor values: 1000=Sektorer i alt, 1015=Stat, 1020=Regioner, 1025=Kommuner, 1030=Sociale kasser og fonde, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit-organisationer, 1050=Uoplyst. Use ColumnValues("lbesk21", "sektor").
- lbesk21 = ukorrigeret; lbesk23 = sæsonkorrigeret (identical structure).
