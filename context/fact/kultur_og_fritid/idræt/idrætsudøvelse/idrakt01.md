table: fact.idrakt01
description: Idrætsorganisationernes medlemmer efter område, aktivitet, køn, alder og tid
measure: indhold (unit Antal)
columns:
- blstkom: join dim.nuts on blstkom=kode [approx: 0 and 99 not in nuts (likely all/unknown)]; levels [2, 3]
- aktivitet: values [A1=Alle idrætsaktiviteter, A3=Atletik, A2=Amerikansk fodbold, A4=Automobilsport (4 hjul), A5=Badminton ... A69=Triathlon, A70=Vandski/Wakeboard, A71=Volleyball, A72=Vægtløftning, A82=Øvrige Idrætslige aktiviteter]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder1: values [TOT=Alder i alt, 0012=0-12 år, 1318=13-18 år, 1924=19-24 år, 2559=25-59 år, 6099=60 år og derover]
- tid: date range 2014-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- blstkom joins dim.nuts. Code 0 = national total (hele landet), 99 = uoplyst — neither exists in dim.nuts so LEFT JOIN will return NULL titel for these. The fact table uses niveau 2 (11 landsdele) and niveau 3 (98 kommuner). Filter `WHERE d.niveau = 2` or `= 3` to pick a single level and avoid double-counting regions.
- aktivitet A1 = "Alle idrætsaktiviteter" (aggregate). Never sum A1 together with the individual sports (A2–A82) — pick one or the other.
- This table has 5 dimension columns (blstkom, aktivitet, kon, alder1, tid). To get a national member count by sport, filter: blstkom='0', kon=10 (i alt), alder1='TOT'. Forgetting any total row will inflate sums.
- kon 10 = i alt, 1 = mænd, 2 = kvinder. alder1 TOT = i alt.
- Use ColumnValues("nuts", "titel", for_table="idrakt01") to see which regions are in this fact table (104 codes including the unmatched 0 and 99).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on blstkom=dim_kode. Exclude blstkom IN (0, 99).