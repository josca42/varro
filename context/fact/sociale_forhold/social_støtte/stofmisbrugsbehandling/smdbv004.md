table: fact.smdbv004
description: Stofmisbrugsbehandling efter område, behandlingsgaranti og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- ventetidgaranti: values [NYBEH=Nystartede behandlingsforløb (antal), OK=Overholdt (antal), EJOK=Ikke overholdt (antal), OKPCT=Overholdt (pct.), EJOKPCT=Ikke overholdt (pct.)]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. niveau 1 = 5 regioner, niveau 3 = 98 kommuner. omrade = '0' is national total (not in dim). Filter to one niveau to avoid double-counting.
- ventetidgaranti MIXES counts and percentages in the same column — never sum all values. The 5 values split into: counts (NYBEH=total new treatments, OK=met guarantee, EJOK=not met) and percentages (OKPCT, EJOKPCT). Treat these as separate measures; pick one group depending on the question.
- OK + EJOK should equal NYBEH (guarantee applies to all new treatments). OKPCT + EJOKPCT ≈ 100.
- indhold unit is '-' (mixed) — confirm you understand whether you're reading counts or percentages before interpreting values. National avg 2024: OKPCT≈89%, EJOKPCT≈11%.
- Sample query — guarantee compliance rate by region (2024): SELECT d.titel, f.indhold FROM fact.smdbv004 f JOIN dim.nuts d ON f.omrade = d.kode WHERE d.niveau = 1 AND f.ventetidgaranti = 'OKPCT' AND f.tid = '2024-01-01'
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.