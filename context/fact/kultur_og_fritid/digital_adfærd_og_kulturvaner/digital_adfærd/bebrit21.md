table: fact.bebrit21
description: Udskiftning af it-udstyr - procent af befolkningen (16-74 år) efter type, udstyr, adfærd ved udskiftning og tid
measure: indhold (unit Pct.)
columns:
- type: values [10=I alt, 40=Alder: 16-19 år, 50=Alder: 20-39 år, 60=Alder: 40-59 år, 70=Alder: 60-74 år ... 210=Indkomst: 0-49.999 kr., 220=Indkomst: 50.000-99.999 kr., 230=Indkomst: 100.000-199.999 kr., 240=Indkomst: 200.000-299.999 kr., 250=Indkomst: 300.000 og derover]
- udstyr: values [4000=Mobil eller smartphone, 4010=Bærbar eller tablet, 4020=Stationær computer]
- adfaerd: values [4030=Den er gemt, 4040=Den er solgt eller foræret væk, 4050=Den er sorteret til elektronisk affald eller genbrug, 4060=Den er smidt ud, men ikke som elektronisk affald, 4070=Har aldrig ejet en eller den er stadig i brug, 4080=Andet]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- type is a demographic selector: type='10' = national total. Never sum across type values.
- udstyr (mobil/bærbar+tablet/stationær) rows are independent questions per device type — do not sum across udstyr.
- adfaerd values are NOT mutually exclusive — a person may have done multiple things with their replaced device (e.g. stored it AND sorted it for recycling). Each row is an independent % of population who took that action. Do not sum.
- 2024 data only (single time point).
