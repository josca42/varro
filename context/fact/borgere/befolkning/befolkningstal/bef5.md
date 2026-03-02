table: fact.bef5
description: Befolkningen 1. januar efter køn, alder, fødeland og tid
measure: indhold (unit Antal)
columns:
- kon: values [M=Mænd, K=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- fodland: values [5100=Danmark, 5901=Færøerne, 5101=Grønland, 5122=Albanien, 5124=Andorra ... 5275=Vanuatu, 5532=Østtimor, 5599=Øer i Stillehavet, 5103=Statsløs, 5999=Uoplyst]
- tid: date range 1990-01-01 to 2025-01-01

notes:
- kon uses M/K (not 1/2 as in folk1a). No total row for kon — sum M+K to get both sexes.
- alder is individual ages 0–125 with no total row. Sum all ages for total by birth country.
- fodland has 200+ individual country codes (5100=Danmark, 5103=Statsløs, 5999=Uoplyst, etc.). Use ColumnValues("bef5", "fodland") to browse. Prefix 5 + 3-digit code.
- No geographic breakdown. Back to 1990 — good for long-run immigration origin trends.