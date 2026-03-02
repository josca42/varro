table: fact.fond17
description: Bevilligede fondsmidler til almennyttige- og ikke-almennyttige formål efter fondstype, nøgletal, formål og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- aktp: values [1105=Bevilgede midler (mio. kr.), 1110=Udbetalte midler (mio. kr.)]
- formal: values [1200=Alle formål, 3045=Almennyttige formål, 3050=Ikke-almennyttige formål]
- tid: date range 2021-01-01 to 2023-01-01

notes:
- aktp is a measurement selector — always filter to one value: 1105=bevilgede midler (mio. kr.) or 1110=udbetalte midler (mio. kr.). Note: no antal (count) in this table unlike fond01.
- formal=1200 is the aggregate total of 3045+3050 (verified). Filter it out when summing across almennyttig/ikke-almennyttig. Note: the formal coding here (3045/3050) is different from the formål taxonomy in fond01-04 (1200-1250).
- fondstype=1000 is the aggregate total of 1005+1010.
- Only 3 years of data (2021-2023). Use fond01 for longer time series.
- Use this table specifically for almennyttig vs. ikke-almennyttig breakdowns, which are not available in any other fond table.