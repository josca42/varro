table: fact.konk5
description: Erklærede konkurser efter levetid og tid
measure: indhold (unit Antal)
columns:
- levtid: values [000=Konkurser i alt, LEV1=0-2 år, LEV2=3-5 år, LEV3=6-10 år, LEV4=Over 10 år]
- tid: date range 2009-01-01 to 2025-09-01

notes:
- levtid='000' is the national total. Filter it out when summing across lifetime categories (LEV1–LEV4 sum to total).
- Levetid refers to the age of the bankrupt company at the time of bankruptcy, not case duration. LEV1=0-2 years old, LEV4=over 10 years old.