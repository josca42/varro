table: fact.vhus2
description: Væksthussektorens forbrug efter produktion, væksthusareal i kvadratmeter (m2), areal og forbrug og tid
measure: indhold (unit -)
columns:
- prod: values [1150=Hovedkultur, alle produktioner, 1155=Hovedkultur, salater, 1160=Hovedkultur, tomater, 1165=Hovedkultur, agurker, 1170=Hovedkultur, diverse grøntsager, 1176=Hovedkultur, snitblomster og snitgrønt, 1182=Hovedkultur, potteplanter, 1195=Hovedkultur, udplantningsplanter, 1200=Hovedkultur, planteskoleprodukter, 1205=Hovedkultur, diverse produktion]
- vaekst: values [0000=I alt, 1000-1999=1000-1999 m2, 2000-4999=2000-4999 m2, 5000-9999=5000-9999 m2, 14999=10000-14999 m2, 19999=15000-19999 m2, 20000=20000 m2 og der over]
- areal2: values [M2=Areal, 1000 kvadratmeter (m2), M3=Vand, 1000 kubíkmeter (m3), GJ=Energi, 1000 Giga-Joule (GJ)]
- tid: date range 2002-01-01 to 2023-01-01

notes:
- areal2 is a measurement selector with fundamentally incompatible units — M2=Areal (1000 m2), M3=Vand (1000 m3), GJ=Energi (1000 GJ). All three appear for the same prod/vaekst/tid combination. Always filter to one areal2 value.
- vaekst=0000 (I alt) is the aggregate across all size classes. The other 6 values are size ranges (1000-1999 m2 up to 20000+ m2). Don't sum vaekst=0000 with the specific size classes.
- prod=1150 (Alle produktioner) is the aggregate across all plant types. Specific production types (1155-1205) are children.
- No regional breakdown. National-level only.