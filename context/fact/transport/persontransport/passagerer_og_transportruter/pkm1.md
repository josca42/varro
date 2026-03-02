table: fact.pkm1
description: Persontransport efter transportmiddel og tid
measure: indhold (unit Mio. personkm)
columns:
- transmid: values [1=KØRETØJER PÅ VEJE I ALT, 5=Cykler/knallert-30, 10=Motorkøretøjer i alt, 12=Personbiler og varebiler under 2.001 kg., 14=Varebiler over 2.000 kg., 20=Taxier, 25=Motorcykler, 30=Knallert-45, 105=Busser i alt, 110=Rutebusser i alt, 113=Turistbusser og andre busser, 125=Tog, 130=Skib, 135=Fly]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- transmid has a nested hierarchy — do not sum sub-codes with their parents. Structure: transmid=1 (all road vehicles) = 5 (Cykler) + 10 (Motorkøretøjer). transmid=10 = 12 + 14 + 20 + 25 + 30 + 105. transmid=105 likely aggregates 110 (Rutebusser) + 113 (Turistbusser) — check before using 110/113 in recent years.
- transmid=125 (Tog), 130 (Skib), 135 (Fly) are standalone non-road modes — NOT included in transmid=1. There is no grand total across all modes. To sum all transport: WHERE transmid IN (1, 125, 130, 135).
- Annual data only. The long series from 1980 makes this the best table for long-run modal split trends.
