table: fact.skat
description: Skatter og afgifter efter type og tid
measure: indhold (unit 1.000 kr.)
columns:
- type: values [TOTAL=Skatter og afgifter i alt, 1=1. Indkomstskatter i alt, 1.1=1.1. Personlige indkomstskatter, 1.1.01=1.1.1. Statslig indkomstskat, 1.1.02=1.1.2. Amtskommunal indkomstskat ... 6.3=6.3. Indbetalinger til Garantiformuen og Afviklingsfonden, 6.3.01=6.3.1. Indbetalinger til Garantiformuen, 6.3.02=6.3.2. Indbetalinger til Afviklingsfonden, 6.4=6.4. Indbetalinger til Landsbyggefonden, 6.4.01=6.4.1. Indbetalinger til Landsbyggefonden]
- tid: date range 1947-01-01 to 2024-01-01

notes:
- type is a 3-level hierarchy: TOTAL (grand total), 1–6 (top-level groups), X.Y (subgroups), X.Y.ZZ (individual items). Filter to exactly one level to avoid double-counting. TOTAL = 1+2+3+4+5+6 (verified).
- To get totals by top-level group: WHERE type IN ('1','2','3','4','5','6'). For individual line items only: WHERE type ~ '^[0-9]+\.[0-9]+\.[0-9]+'. Use ColumnValues("skat","type") to browse the full label list.
- 214 distinct type codes total. Group meanings: 1=Indkomstskatter, 2=Produktions-/importskatter, 3=Løbende indkomst-/formueskatter, 4=Obligatoriske sociale bidrag, 5=Afgifter (many subtypes), 6=Andre skatter.