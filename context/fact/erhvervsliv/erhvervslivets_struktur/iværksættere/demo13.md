table: fact.demo13
description: Erhvervsdemografi efter branche (DB07 19-grp), enhed og tid
measure: indhold (unit -)
columns:
- branchedb0721: join dim.db on branchedb0721=kode::text [approx]
- maengde4: values [AFU=Fuldtidsansatte (antal), OPH=Ophørte firmaer (antal), OMS=Omsætning (mio kr.) , NYE=Nye firmaer (antal)]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- branchedb0721 uses EU NACE section letter codes (A–T, X) — 0% match with dim.db which uses numeric codes. Do not attempt a dim.db join. Use ColumnValues("demo13", "branchedb0721") to get labels: A=Landbrug/skovbrug/fiskeri, C=Industri, F=Bygge og anlæg, G=Handel, etc. T=Erhverv i alt (national total), X=Uoplyst aktivitet.
- maengde4 is a measurement selector — each branche+tid repeats 4 times. Filter to one: AFU=fuldtidsansatte, NYE=nye firmaer, OPH=ophørte firmaer, OMS=omsætning (mio kr.). These are not additive across maengde4 values.
- Broadest branch grouping in this subject (21 sections) — use when you need a clean sector overview. For finer detail use demo11 (127 groups) or demo14/demo19 for regional breakdown.