table: fact.bil8
description: Bestand af køretøjer pr. 1. januar efter køretøjstype, alder og tid
measure: indhold (unit Antal)
columns:
- biltype: values [4000101002=Personbiler i alt, 4000101011=Personbiler til hyrevognskørsel, 4000101012=Personbiler til udlejning, 4000101013=Personbiler til skolekørsel, 4000101014=Personbiler til sygekørsel ... 4000000008=Traktorer i alt, 4000000009=Traktorer, registrerede, 4000000010=Traktorer, godkendte, 4000103001=Campingvogne i alt, 4000105000=Vare- og lastbiler til brand- og redningskørsel]
- alder1: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 22=22 år, 23=23 år, 24=24 år, 24OV=Mere end 24 år, 620=Gnst. alder i antal år]
- tid: date range 1993-01-01 to 2025-01-01

notes:
- alder1=620 (Gnst. alder i antal år) is a floating-point average age, not a count. It cannot be summed or grouped with other alder1 codes. Always filter it out when computing age distributions or totals: WHERE alder1 != '620'.
- alder1=IALT is the count total across all ages; individual ages 0–24 are individual year bands; 24OV=more than 24 years.
- biltype has many subcodes — use ColumnValues("bil8", "biltype") to browse. Same large list as bil707.