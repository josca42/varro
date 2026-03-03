table: fact.ifor41
description: Ulighedsmål målt på ækvivaleret disponibel indkomst efter ulighedsmål, kommune og tid
measure: indhold (unit -)
columns:
- ullig: values [70=Gini-koefficient, 71=Maksimal udjævningsprocent, 72=S80/20(Baseret på gennemsnit i deciler), 73=P90/10 (Baseret på decilgrænser)]
- kommunedk: join dim.nuts on kommunedk=kode [approx]; levels [3]
- tid: date range 1987-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- ullig is an inequality measure selector: each code is a fundamentally different statistic — Gini-koefficient (70), Maksimal udjævningsprocent (71), S80/20 based on decil averages (72), P90/10 based on decil limits (73). Never sum or average across ullig values — always filter to one measure per query.
- kommunedk code 0 = Danmark i alt (not in dim.nuts). All other codes join dim.nuts at niveau=3 (kommuner).
- Gini-koefficient (70) is the most commonly cited inequality measure. Values typically range 0.25–0.35 for Danish kommuner.
- This is the only table in the subject with pre-calculated inequality indices (Gini, S80/20, P90/10). Use it instead of computing inequality manually from decil data.
- Sample query (Gini by kommune, 2023): SELECT d.titel, f.indhold FROM fact.ifor41 f JOIN dim.nuts d ON f.kommunedk = d.kode::int WHERE f.ullig = '70' AND f.tid = '2023-01-01' AND f.kommunedk != 0 ORDER BY f.indhold DESC;
- Map: /geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
