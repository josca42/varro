table: fact.livmus02
description: Antal koncerter efter koncertarrangør, koncertstørrelse og tid
measure: indhold (unit Antal)
columns:
- koncertarrangor: values [103005=Folkekirke, 103010=Kulturhus, 103015=Landsdelsorkester, 103020=Musikfestival, 103025=Musikforening, 103030=Regionalt spillested, 103035=Spillested, 103080=Professionel koncertarrangør, 103040=Øvrig koncertarrangør]
- koncertstorrelse: values [0=I alt, 103045=Under 200 personer, 103050=200-499 personer, 103055=500-999 personer, 103060=1.000-4.999 personer, 103065=5.000-9.999 personer, 103070=10.000-29.999 personer, 103075=30.000 personer og derover]
- tid: date range 2018-01-01 to 2023-01-01

notes:
- Same structure as livmus01, but indhold = number of concerts (not audience). Same gotchas apply.
- koncertstorrelse='0' is the "I alt" total. To count concerts for a specific organizer: filter WHERE koncertstorrelse='0'. To break down by size: filter WHERE koncertstorrelse!='0'.
- koncertarrangor has no total code — all 9 values are individual organizer types.