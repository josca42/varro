table: fact.pris111
description: Forbrugerprisindeks efter varegruppe, enhed og tid
measure: indhold (unit -)
columns:
- varegr: join dim.ecoicop_dst on varegr=kode [approx]; levels [4, 5]
- enhed: values [100=Indeks, 200=Ændring i forhold til måneden før (pct.), 300=Ændring i forhold til samme måned året før (pct.)]
- tid: date range 2001-01-01 to 2025-09-01
dim docs: /dim/ecoicop_dst.md

notes:
- **enhed is a measurement selector** — every varegr×tid combination appears 3×, once per enhed (100=Indeks, 200=månedlig ændring pct., 300=årsændring pct.). Always filter to one enhed or results will be tripled.
- varegr=0 is the overall CPI total. Filter it out when iterating over categories.
- The varegr→dim.ecoicop_dst join requires stripping trailing zeros AND a niveau filter. Direct join on varegr=kode fails (only 1% match). The correct join:
  ```sql
  WITH tz AS (
    SELECT varegr,
      CASE WHEN varegr % 10000 = 0 THEN 4 WHEN varegr % 1000 = 0 THEN 3
           WHEN varegr % 100  = 0 THEN 2 WHEN varegr % 10   = 0 THEN 1 ELSE 0 END AS tz
    FROM fact.pris111
  )
  JOIN dim.ecoicop_dst d ON d.kode = (varegr / POWER(10, tz)::int)
    AND d.niveau = (5 - tz)
  ```
- 5-digit varegr (< 100000) covers ECOICOP main groups 1–9; 6-digit varegr (≥ 100000) covers main groups 10 (UDDANNELSE), 11 (RESTAURANTER), 12 (ANDRE VARER). The 6-digit codes are needed because groups 10–12 have 2-digit prefixes.
- 95% of codes (365/384) match dim.ecoicop_dst. Unmatched codes (131xxx, 132xxx, 141xxx, 151xxx and a handful of 5-digit ones) are DST-specific ECOICOP extensions — use LEFT JOIN and accept NULLs for titel.
- ColumnValues("pris111", "varegr") returns all 385 codes with labels like "01.1.1 Brød og kornprodukter". Use fuzzy_match_str to find a specific category without knowing the code.
- Table contains all ECOICOP hierarchy levels (niveau 1–5) simultaneously — do not SUM across varegr without filtering to a single niveau, as parent and child rows are both present.