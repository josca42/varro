table: fact.filmind1
description: Indtægter til danske spillefilm efter indtægtstype, målgruppe, nøgletal og tid
measure: indhold (unit -)
columns:
- indttype: values [F05=Indtægter i alt, F06=Biografindtægter, F07=Video-, DVD- og VOD-indtægter, F08=TV-indtægter, F09=Udlandsindtægter, F10=Andre indtægter]
- mlgrp: values [M00=Alle publikumsgrupper, M01=Børn/unge/familie, M02=Voksne]
- aktp: values [N03=Film (antal), N05=Indtægt (mio. kr.)]
- tid: date range 2010-01-01 to 2021-01-01

notes:
- aktp is a measurement selector. Filter to one: N03=Film (antal), N05=Indtægt (mio. kr.).
- indttype: F05 = total (= F06+F07+F08+F09+F10). Filter to F05 for overall income or pick a sub-type.
- mlgrp: M00=Alle as total; M01+M02 add up to M00.
- Note: this table only goes to 2021, while filmfin1/filmfin2/filmomk1 go to 2023. For the most recent film economics data, use the fin/omk tables.