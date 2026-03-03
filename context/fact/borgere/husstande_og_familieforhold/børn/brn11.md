table: fact.brn11
description: Børn med familieskift efter område, familieskift, familietype sidste år, familietype i år, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- famskift: values [JA_SKIFT=Har skiftet familie, EJ_SKIFT=Har ikke skiftet familie]
- famtypsaa: values [0=Udeboende, 1=Begge forældre, 2=Enlig mor, 3=Mor og partner, 4=Enlig far, 5=Far og partner]
- famtypaa: values [0=Udeboende, 1=Begge forældre, 2=Enlig mor, 3=Mor og partner, 4=Enlig far, 5=Far og partner]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år, 5=5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år, 15=15 år, 16=16 år, 17=17 år]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/nuts.md
notes:
- omrade has three groups: '0' (national total, not in dim.nuts — use omrade='0' directly), niveau 1 (5 regioner), niveau 3 (99 kommuner). Filter to one niveau when joining dim.nuts.
- famskift: use famskift='JA_SKIFT' to isolate children who changed family structure during the year; famskift='EJ_SKIFT' is the large majority who did not change.
- famtypsaa = family type at start of year (sidste år), famtypaa = family type at end of year (i år). Cross-tabulate these to see transition flows, e.g. how many went from "Begge forældre" (1) to "Enlig mor" (2).
- famtype 0="Udeboende" in both before/after columns covers children moving in or out of institutional care.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
