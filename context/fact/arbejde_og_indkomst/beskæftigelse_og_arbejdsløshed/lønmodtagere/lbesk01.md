table: fact.lbesk01
description: Lønmodtagere efter branche (DB07 10- og 19-grp) og tid
measure: indhold (unit Antal)
columns:
- branchedb071038: join dim.db_10 on branchedb071038=kode::text [approx]; levels [1]
- tid: date range 2008-01-01 to 2025-08-01
dim docs: /dim/db_10.md

notes:
- branchedb071038 mixes two grouping schemes in one column: numeric 1–11 (10-gruppe) and letter codes A–S + X (19-gruppe NACE afsnit). TOT = alle brancher. Never aggregate across both — filter to one scheme.
- For 10-gruppe: WHERE branchedb071038 ~ '^[0-9]+$'. Join: JOIN dim.db_10 d ON f.branchedb071038 = d.kode::text AND d.niveau = 1. Gives 11 groups (1=Landbrug, 2=Industri, ..., 10=Kultur, 11=Uoplyst).
- For 19-gruppe: WHERE branchedb071038 ~ '^[A-Z]' AND branchedb071038 != 'TOT'. Letter codes are NOT in any dim table — treat as inline. Use ColumnValues("lbesk01", "branchedb071038") to see labels (A=Landbrug, B=Råstofindvinding, C=Industri, D=Energiforsyning, E=Vandforsyning, F=Bygge, G=Handel, H=Transport, I=Hoteller, J=Information, K=Finansiering, L=Ejendom, M=Videnservice, N=Operationel service, O=Off. admin, P=Undervisning, Q=Sundhed, R=Kultur, S=Andre service, X=Uoplyst).
- No tal column — single measure type. lbesk01 = ukorrigeret; lbesk03 = sæsonkorrigeret (same structure, but lbesk03 doc wrongly says dim.db — correct dim is db_10).