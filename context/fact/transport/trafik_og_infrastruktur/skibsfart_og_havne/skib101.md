table: fact.skib101
description: Trafikhavnenes skibsanløb, passagerer og godsomsætning efter havn, enhed og tid
measure: indhold (unit -)
columns:
- havn: values [0=HAVNE I ALT, 1000=LANDSDEL BYEN KØBENHAVN, 25=Københavns Havn, 2000=LANDSDEL KØBENHAVNS OMEGN, 10=Avedøreværkets Havn ... 790=Skagen Havn, 720=Thisted Havn, 795=Vesterø Havn, 730=Aalborg Havn, 735=Aalborg Portland Havn]
- enhed: values [7000=Skibsanløb, antal, 7005=GODSOMSÆTNING I ALT,  1000 ton, 7008=Godsomsætning, Udenrigs, 1000 ton, 7006=Godsomsætning, Indenrigs, 1000 ton, 7010=PASSAGERER I ALT, 1000, 7020=Udenrigspassagerer, 1000, 7015=Indenrigspassagerer, 1000]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- enhed is a measurement selector with 7 values across three different unit types — NEVER sum across enhed values: 7000=Skibsanløb (antal), 7005=Godsomsætning I ALT (1000 ton), 7006=Godsomsætning Indenrigs (1000 ton), 7008=Godsomsætning Udenrigs (1000 ton), 7010=Passagerer I ALT (1000), 7015=Indenrigspassagerer (1000), 7020=Udenrigspassagerer (1000). Always filter to one enhed.
- Note that 7005=7006+7008 and 7010=7015+7020 — these are sub-total relationships within enhed. Picking the I ALT codes avoids double-counting when you want totals.
- havn='0' (HAVNE I ALT) is the national total. Codes 1000–11000 are LANDSDEL regional aggregates. Specific harbor codes are below 1000. Only pick one level — they are not additive across levels.
- This is the most comprehensive single table: covers ship arrivals, cargo tonnage (domestic/international), and passengers (domestic/international) all in one. Use it when you need multiple metrics for the same harbor.
- For a simple query: WHERE enhed='7000' AND havn='0' AND tid='2024-01-01' gives total national ship arrivals for 2024.