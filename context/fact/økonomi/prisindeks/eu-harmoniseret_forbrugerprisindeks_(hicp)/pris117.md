table: fact.pris117
description: EU-harmoniseret forbrugerprisindeks (HICP) efter varegruppe, enhed og tid
measure: indhold (unit -)
columns:
- varegr: join dim.ecoicop on varegr=kode::text [approx]
- enhed: values [100=Indeks, 200=Ændring i forhold til måneden før (pct.), 300=Ændring i forhold til samme måned året før (pct.)]
- tid: date range 1996-01-01 to 2025-09-01
dim docs: /dim/ecoicop.md

notes:
- varegr uses 6-digit ECOICOP codes (e.g. '010000', '011000', '100000'), NOT the short kode used in dim.ecoicop. Simple equality join fails entirely. The 6-digit code encodes: first 2 chars = division number (zero-padded), chars 3-6 = group/class/subclass/sub-subclass digits (trailing zeros = not specified).
- Special aggregate code: 'HICP' = overall HICP total index (not in dim.ecoicop).
- The hierarchy niveau is inferred from trailing zeros: 4 trailing zeros = niveau 1, 3 = niveau 2, 2 = niveau 3, 1 = niveau 4, 0 = niveau 5. 10 out of 378 codes are HICP-specific sub-categories not present in dim.ecoicop (e.g. '061230', '082300').
- Correct join expression (decode varegr to dim.ecoicop kode):
  ```sql
  WITH decoded AS (
    SELECT *,
      CASE
        WHEN varegr = 'HICP' THEN 0
        WHEN substr(varegr,3,4)='0000' THEN 1
        WHEN substr(varegr,4,3)='000'  THEN 2
        WHEN substr(varegr,5,2)='00'   THEN 3
        WHEN substr(varegr,6,1)='0'    THEN 4
        ELSE 5
      END AS varegr_niveau,
      CASE
        WHEN varegr = 'HICP' THEN NULL
        WHEN substr(varegr,3,4)='0000' THEN left(varegr,2)::int
        WHEN substr(varegr,4,3)='000'  THEN (left(varegr,2)||substr(varegr,3,1))::int
        WHEN substr(varegr,5,2)='00'   THEN (left(varegr,2)||substr(varegr,3,2))::int
        WHEN substr(varegr,6,1)='0'    THEN (left(varegr,2)||substr(varegr,3,3))::int
        ELSE                                (left(varegr,2)||substr(varegr,3,4))::int
      END AS ecoicop_kode
    FROM fact.pris117
  )
  SELECT d.titel, f.indhold
  FROM decoded f
  JOIN dim.ecoicop d ON f.ecoicop_kode = d.kode AND d.niveau = f.varegr_niveau
  WHERE f.enhed = '300' AND f.varegr_niveau = 1  -- year-on-year, division level
  ```
- enhed is a measurement selector — every varegr+tid combination has 3 rows (100=index, 200=mom%, 300=yoy%). Always filter to one enhed value. Failing to filter triples all counts.
- To browse categories: ColumnValues("pris117", "varegr") returns all 378 codes but the raw 6-digit format is not human-readable. Use the decode logic above and join dim.ecoicop to get titles.