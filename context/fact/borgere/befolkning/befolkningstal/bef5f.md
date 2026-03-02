table: fact.bef5f
description: Personer født på Færøerne og bosat i Danmark 1. januar efter køn, alder, forældrenes fødested og tid
measure: indhold (unit Antal)
columns:
- kon: values [M=Mænd, K=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- ff: values [BDK=Begge forældre født i Danmark, BFÆR=Begge forældre født på Færøerne, BUDL=Begge forældre født i udlandet, BUOP=Begge forældre uoplyst, DKFÆR=En forælder født i Danmark og en forælder født på Færøerne, DKUDL=En forælder født i Danmark og en forælder født i udlandet, DKUOP=En forælder født i Danmark og en forælder uoplyst, FÆRUDL=En forælder født på Færøerne og en forælder født i udlandet, FÆRUOP=En forælder født på Færøerne og en forælder uoplyst, UDLUOP=En forælder født i udlandet og en forælder uoplyst]
- tid: date range 2008-01-01 to 2025-01-01

notes:
- Niche table: only Faroese-born people residing in Denmark. Total population is small (a few thousand rows per year).
- kon uses M/K (not 1/2). No total for kon — sum M+K. No total for alder — sum desired range.
- ff has 10 parental origin combinations covering all combinations of DK/Færøerne/Udland/Uoplyst parents. The 10 codes are mutually exclusive and exhaustive — summing all ff for one kon+alder+tid gives total Faroese-born residents.
- Structurally identical to bef5g (Greenlandic-born). Compare with bef5 for all birth countries.