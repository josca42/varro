table: fact.smdbv003
description: Stofmisbrugsbehandling efter nøgletal, køn, alder og tid
measure: indhold (unit Antal)
columns:
- aktp: values [KTKFORL=Kontaktforløb, BEHFORL=Behandlingsforløb, PERSBEH=Personer i behandling]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder1: values [TOT=Alder i alt, 0017=Under 18 år, 1899=18 år og derover]
- tid: date range 2015-01-01 to 2024-01-01

notes:
- No regional dimension — this is the national breakdown by gender and age. For regional data use smdbv002.
- aktp has 3 distinct metrics (KTKFORL, BEHFORL, PERSBEH). Always filter to one aktp — do not sum across all three.
- kon and alder1 both have total rows: kon='TOT' and alder1='TOT'. Filter both to their total when you only want one dimension's breakdown. alder1 has only 3 values: TOT, 0017 (under 18), 1899 (18+) — no finer age breakdown in this table.
- To get national total for a metric: WHERE aktp='PERSBEH' AND kon='TOT' AND alder1='TOT'.