table: fact.obesk1
description: Offentligt fuldtidsbeskæftigede lønmodtagere efter formålsopdeling (COFOG) og tid
measure: indhold (unit Antal)
columns:
- cofog: join dim.cofog on cofog=kode::text; levels [1]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/cofog.md
notes:
- SCOPE: Only public sector full-time equivalent employees (offentligt fuldtidsbeskæftigede). Covers Stat + Regioner + Kommuner only — NOT offentlige virksomheder or private.
- No tal column — single measure.
- cofog joins dim.cofog correctly (83% match). Unmatched: TOT1=total and 99=Uoplyst/Andre — filter these out in JOIN. Join at niveau 1 (10 COFOG categories, codes 1–10): JOIN dim.cofog d ON f.cofog = d.kode::text AND d.niveau = 1.
- COFOG categories: 1=Generelle tjenester, 2=Forsvar, 3=Orden og sikkerhed, 4=Økonomi, 5=Miljø, 6=Boliger, 7=Sundhed, 8=Fritid og kultur, 9=Undervisning, 10=Social beskyttelse.
- obesk1 = ukorrigeret; obesk4 = sæsonkorrigeret (identical structure).
