table: fact.bef4
description: Befolkningen 1. januar efter øer og tid
measure: indhold (unit Antal)
columns:
- oer: values [1000=Sjællandske øgruppe (sammentælling), 1010=Agersø, 1020=Amager, 1030=Bogø, 1040=Dybsø ... 2060=Tunø, 2070=Vendsyssel-Thy, 2080=Venø, 2090=Vorsø, 2100=Årø]
- tid: date range 1901-01-01 to 2025-01-01

notes:
- oer includes both individual islands and aggregate group codes (e.g., 1000=Sjællandske øgruppe). Mixing individual islands with their group total will double-count. Filter to individual island codes if summing.
- No sex/age breakdown — total population per island only.
- Back to 1901. Use ColumnValues("bef4", "oer") to see all island codes.