table: fact.skolm04a
description: Ansattes årsværk på musikskolerne efter kommune, arbejdsfunktion, fagområde og tid
measure: indhold (unit -)
columns:
- komk: join dim.kommunegrupper on komk=kode; levels [2]
- arbfunk: values [TOT=Ansatte i alt, 10490=Ledelse og administration, 10500=Fastansat underviser]
- fagomr: values [TOTA=Fagområder i alt, 10490=Ledelse og administration, 1001=Musik, 1002=Visuel kunst, 1003=Håndværk og design, 1004=Scenekunst, 1005=Dans, 1006=Film og animation, 1007=Skrivekunst, 1008=Medier, 1009=Øvrige]
- tid: date range 2021 to 2025
dim docs: /dim/kommunegrupper.md

notes:
- indhold is årsværk (FTE), not a headcount of individuals. Use skolm04b for individual employee counts.
- komk joins dim.kommunegrupper at niveau 2. komk='0' is the national total, not in the dim.
- arbfunk and fagomr both have total rows (TOT/TOTA). Filter both to avoid overcounting. Code 10490 appears in both columns (Ledelse og administration) — when arbfunk='10490', use fagomr='TOTA' to get the total for that function; fagomr breakdown is only meaningful when arbfunk='10500' (Fastansat underviser).
- Map: context/geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.