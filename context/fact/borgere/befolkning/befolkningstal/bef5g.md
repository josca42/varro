table: fact.bef5g
description: Personer født i Grønland og bosat i Danmark 1. januar efter køn, alder, forældrenes fødested og tid
measure: indhold (unit Antal)
columns:
- kon: values [M=Mænd, K=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- ff: values [BDK=Begge forældre født i Danmark, BGRL=Begge forældre født i Grønland, BUDL=Begge forældre født i udlandet, BUOP=Begge forældre uoplyst, DKGRL=En forælder født i Danmark og en forælder født i Grønland, DKUDL=En forælder født i Danmark og en forælder født i udlandet, DKUOP=En forælder født i Danmark og en forælder uoplyst, GRLUDL=En forælder født i Grønland og en forælder født i udlandet, GRLUOP=En forælder født i Grønland og en forælder uoplyst, UDLUOP=En forælder født i udlandet og en forælder uoplyst]
- tid: date range 2008-01-01 to 2025-01-01

notes:
- Niche table: only Greenlandic-born people residing in Denmark. Structurally identical to bef5f but ff codes use GRL instead of FÆR.
- kon uses M/K (not 1/2). No total for kon — sum M+K. No total for alder — sum desired range.
- ff has 10 mutually exclusive parental origin combinations covering DK/Grønland/Udland/Uoplyst. Summing all ff gives total Greenlandic-born residents in Denmark for that kon+alder+tid.
- Compare with bef5 (fodland=5101 Grønland) for a simpler view without parental origin breakdown.