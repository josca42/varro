table: fact.und2
description: Børn der er modtaget underretninger om efter administrationskommune, underretninger, alder, køn og tid
measure: indhold (unit Antal)
columns:
- admkom: join dim.nuts on admkom=kode [approx]; levels [3]
- underret: values [0=I alt, 1=1 underretning, 2=2 underretninger, 3=3 underretninger, 4=4 underretninger, 5=5 underretninger, 6=6 underretninger eller flere]
- alder1: values [00=I alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 16=16 år, 17=17 år, 18=18 år, U0=Ufødt, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn, U=Uoplyst køn, ufødt]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Counts CHILDREN by how many notifications were received about them (1, 2, 3, 4, 5, 6+). Use this to answer "how many children had 3 or more underretninger".
- underret: 0=I alt (total children with any notification), 1-5=exact counts, 6=six or more. These are mutually exclusive — a child is in exactly one group. Summing 1+2+3+4+5+6 = total (same as code 0).
- admkom joins dim.nuts at niveau 3 (kommuner). Code 0 = national total, code 998 = unknown municipality.
- Same alder1 and kon encoding as und1 (total='00', ufødt='U0').
- For total children with any notification by kommune: WHERE underret='0' AND alder1='00' AND kon='0'.
- Map: /geo/kommuner.parquet — merge on admkom=dim_kode. Exclude admkom=0 and admkom=998.