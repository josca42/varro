table: fact.anbaar15
description: Anbragte børn og unge pr. 31. december efter anbringelsessted, alder, køn og tid
measure: indhold (unit Antal)
columns:
- anbringelse: values [0=I alt, 1=Netværksplejefamilie, 21=Almindelig plejefamlie, 22=Kommunal plejefamilie, 26=Plejefamilie efter §76 a (unge med funktionsnedsættelse), 23=Almen plejefamilie, 24=Forstærket plejefamilie, 25=Specialiseret plejefamlie, 9=Døgninstitution, almindelig afdeling, 7=Delvis lukket døgninstitution eller delvis lukket afdeling på åben døgninstitution, 8=Døgninstitution, sikret afdeling, 27=Opholdssted for børn og unge, 11=Kost- og eller efterskole, 6=Eget værelse, kollegium, kollegielignende opholdssted, 99=Uoplyst]
- alder1: values [0=I alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 19=19 år, 20=20 år, 21=21 år, 22=22 år, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn]
- tid: date range 2011-01-01 to 2024-01-01

notes:
- Like anbaar2 but broken down by anbringelsessted (placement type) instead of legal basis. Same alder1 and kon encoding applies (0=I alt, D/P).
- anbringelse code 0 = I alt. Codes 21-26 are plejefamilie subtypes (almen, forstærket, specialiseret, kommunal, netværk, §76a); code 9 = ordinary døgninstitution; code 27 = opholdssted.
- Note that plejefamilie types 23/24/25 were introduced with a 2024 reform (replacing the old 21/22 categories). Data before 2024 uses codes 21 (Almindelig) and 22 (Kommunal).
- No geographic breakdown — national totals only. For regional placement type breakdown use anbaar16.