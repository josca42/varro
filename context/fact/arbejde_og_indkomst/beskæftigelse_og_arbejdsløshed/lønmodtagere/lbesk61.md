table: fact.lbesk61
description: Lønmodtagere efter enhed, branche (DB07 19-grp), sektor, køn, alder og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- branchedb0738: join dim.db on branchedb0738=kode::text
- sektor: join dim.esr_sekt on sektor::text=kode
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- alder: values [TOT=Alder i alt, U15=Under 15 år, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6574=65-74 år, 75OV=75 år og derover, UDK=Uoplyst alder, uden bopæl i Danmark]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/db.md, /dim/esr_sekt.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- WARNING: dim.db join for branchedb0738 is broken (0% match). branchedb0738 uses letter codes only (A–S, X, TOT) — NOT in dim.db. Treat as inline. Use ColumnValues("lbesk61", "branchedb0738") for labels.
- WARNING: dim.esr_sekt join for sektor is broken (0% match). sektor values here: 1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit-organisationer, 1050=Uoplyst. Treat as inline.
- Note: sektor here has 6 values (aggregated public sector as 1032), different from lbesk21/lbesk23 which split offentlig into stat/regioner/kommuner/sociale kasser.
- Most detailed table combining branche + sektor + kon + alder. Filter all dimensions to avoid overcounting.
- Data ends 2025-01. For more recent data, use tables without alder breakdown.
