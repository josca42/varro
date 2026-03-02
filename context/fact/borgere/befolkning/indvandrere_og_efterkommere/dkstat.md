table: fact.dkstat
description: Personer, der har fået dansk statsborgerskab efter køn, alder, tidligere statsborgerskab og tid
measure: indhold (unit Antal)
columns:
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 96=96 år, 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover]
- tidstat: join dim.lande_psd on tidstat=kode; levels [3]
- tid: date range 1979-01-01 to 2024-01-01
dim docs: /dim/lande_psd.md

notes:
- No total rows for kon (1/2 only) or alder (individual years only). Must SUM across both to get aggregate naturalization counts.
- tidstat = previous/former nationality before naturalization. niveau=3 individual countries (~198 countries). No total code — SUM across countries for overall count.
- tid is annual (1979–2024). indhold = number of naturalizations granted that year.
- Use ColumnValues("lande_psd", "titel", for_table="dkstat") to browse previous nationalities in this table.