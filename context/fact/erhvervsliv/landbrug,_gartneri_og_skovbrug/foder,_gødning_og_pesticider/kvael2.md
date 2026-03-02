table: fact.kvael2
description: Den samlede handelsgødningsforsyning/Indhold af rene næringsstoffer efter stoftype, måleenhed og tid
measure: indhold (unit -)
columns:
- stoftype: values [FOS=Fosfor, Phosphorus (P), KALIUM=Kalium Potassium (K), KVÆL=Kvælstof, Nitrogen (N)]
- maleenhed: values [MIOKG=Mio. kg, KGPRHA=Kg pr. ha]
- tid: date range 1983 to 2024

notes:
- maleenhed is a measurement selector: MIOKG=Mio. kg (absolute supply) vs KGPRHA=Kg pr. ha (per-hectare rate). Every stoftype×tid combination appears twice. Filter to exactly one — MIOKG for totals, KGPRHA for intensity.
- stoftype has exactly 3 nutrients: KVÆL=Nitrogen (N), FOS=Phosphorus (P), KALIUM=Potassium (K). No total row — these represent distinct nutrient types and summing them is not meaningful.
- tid is int4range. Filter with `WHERE tid @> 2023` for a specific year.
- Simple table: 3 nutrients × 2 units × ~40 years. No sub-categories.