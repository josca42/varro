table: fact.lbesk32
description: Lønmodtagere efter enhed, branche (DB07 19-grp), sektor og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- branchedb0738: join dim.db on branchedb0738=kode::text
- sektor: join dim.esr_sekt on sektor::text=kode
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/db.md, /dim/esr_sekt.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- WARNING: dim.db join for branchedb0738 is broken (0% match). branchedb0738 uses letter codes only (A–S, X, TOT) — NOT in dim.db (which uses numeric codes). Treat branchedb0738 as inline. Use ColumnValues("lbesk32", "branchedb0738") for labels: A=Landbrug, B=Råstofindvinding, C=Industri, D=Energiforsyning, E=Vandforsyning, F=Bygge, G=Handel, H=Transport, I=Hoteller, J=Information, K=Finansiering, L=Ejendom, M=Videnservice, N=Operationel service, O=Off. admin, P=Undervisning, Q=Sundhed, R=Kultur, S=Andre service, X=Uoplyst, TOT=I alt.
- WARNING: dim.esr_sekt join for sektor is broken (0% match). sektor uses 4-digit numeric codes — treat as inline. Values: 1000=total, 1015=Stat, 1020=Regioner, 1025=Kommuner, 1030=Sociale kasser og fonde, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit, 1050=Uoplyst.
- To get branch totals across all sectors, filter sektor='1000'. To get sector totals across all branches, filter branchedb0738='TOT'.
