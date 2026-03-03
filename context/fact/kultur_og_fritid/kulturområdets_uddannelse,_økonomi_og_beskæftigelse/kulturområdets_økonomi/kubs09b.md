table: fact.kubs09b
description: Kulturministeriets udbetalinger særligt målrettet forskning efter område, kulturemne, finansieringsart, statsinstitution, enhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode::text [approx]; levels [2, 3]
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 9=Fornøjelses- og temaparker, 10=Idræt, 11=Spil og lotteri ... 30=Reklame, 31=Statslig administration, 32=Udstyr, 33=Anden/tværgående kultur, 34=Folkeoplysning og folkehøjskoler]
- finansart: values [0=I alt, 40=Anlæg, 41=Distribution, 43=Drift, 39=Personlig, 42=Projekt]
- statsinstituition: values [SL=Statsinstitutioner landsdækkende, SB=Statsinstitutioner efter beliggenhed]
- enhed: values [KUDB=Udbetalinger (1.000 kr.), KKPI=Udbetaling pr. indbygger (kr.)]
- tid: date range 2017-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- Same structure as kubs02b but scoped to forskning-targeted disbursements. See kubs02b notes for `enhed` selector, `statsinstituition` selector, and `omrade` int-cast join guidance.
- `omrade='00'` is national aggregate (not in dim). Use `f.omrade::int = d.kode` for join.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade::int=dim_kode. Exclude omrade='00'.