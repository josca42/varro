table: fact.aed16
description: Frit boligvalg og gennemsnitlig ventetid til plejehjem og plejeboliger for personer på 67 år og derover efter enhed, område og tid
measure: indhold (unit -)
columns:
- maengde4: values [0=Personer på venteliste i alt, 110=Personer visiteret til den generelle venteliste, 120=Personer der vælger frit valg, 130=Andel af personer i alt, der vælger frit valg, 140=Gennemsnitlig ventetid i dage til plejebolig for personer på generel venteliste, som har fået tilbudt bolig i året]
- omrade: join dim.nuts on omrade=kode; levels [3]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- maengde4 contains 5 entirely different metrics in the same column: counts (0, 110, 120), a percentage (130), and days (140). Never sum or aggregate across maengde4 — each value requires a separate query. Always filter to one maengde4 value.
- indhold unit is "-" because the unit differs by maengde4 value: Antal for 0/110/120, Pct. for 130, Dage for 140.
- omrade joins dim.nuts niveau 3 only (98 kommuner). omrade=0 is the national total (not in dim).
- To get waiting time in days: filter maengde4='140'. To get the share choosing free choice: filter maengde4='130'.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
