table: fact.kubs02b
description: Kulturministeriets udbetalinger efter område, kulturemne, finansieringsart, statsinstitution, enhed og tid
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
- `enhed` is a measurement selector: KUDB=total 1.000 kr., KKPI=kr. per inhabitant. Always filter to one value — mixing them in a sum is meaningless.
- `statsinstituition` is also a selector: SL=national institutions (counted as national total, not tied to a location), SB=institutions by physical location. These are two different views of the data; filter to one.
- `omrade` joins dim.nuts but requires a cast to int: `f.omrade::int = d.kode`. The documented text join fails for region codes (081–085) and landsdel codes (01–11) because of leading zeros. `omrade='00'` is the national aggregate (not in dim).
- `omrade` has hierarchy levels 2 (landsdele, codes 01–11) and 3 (kommuner, codes 101+). Regions (niveau 1, 081–085) are also present — join via int cast. Filter `d.niveau` to pick your geographic granularity.
- `finansart=0` is I alt. Filter kulturemne=0 for all topics.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade::int=dim_kode. Exclude omrade='00'.