table: fact.lbesk02
description: Lønmodtagere efter sektor og tid
measure: indhold (unit Antal)
columns:
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1046=Virksomheder og organisationer, 1050=Uoplyst]
- tid: date range 2008-01-01 to 2025-08-01
notes:
- Simple two-way sector split. sektor uses 4-digit numeric codes — fully inline, do NOT join dim.esr_sekt (0% match). Values: 1000=total, 1032=Offentlig forvaltning og service, 1046=Virksomheder og organisationer, 1050=Uoplyst.
- No tal column — single measure (antal lønmodtagere). lbesk02 = ukorrigeret; lbesk04 = sæsonkorrigeret (identical structure).
- For a more granular sector breakdown (stat/regioner/kommuner/sociale kasser), use lbesk21 or lbesk23.
