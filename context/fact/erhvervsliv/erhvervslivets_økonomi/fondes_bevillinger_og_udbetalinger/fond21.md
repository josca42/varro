table: fact.fond21
description: Bevilligede fondsmidler til grøn forskning efter fondstype, underområde og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- underomrade: values [4050=Bæredygtige energiteknologier og -produktion mv., 4060=Energieffektivisering, 4070=Bæredygtig fødevareproduktion, landbrug og skove, 4080=Grøn transport, 4090=Miljøbeskyttelse, cirkulær økonomi og miljøteknologi, 4100=Naturbeskyttelse, biodiversitet og klimaforandringer, 4110=Bæredygtig adfærd og samfundsmæssige konsekvenser]
- tid: date range 2022-01-01 to 2023-01-01

notes:
- underomrade has 7 leaf-level codes with no aggregate total. All can be summed freely.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.
- Only 2 years of data (2022-2023). This table is a sub-breakdown of fond19 (natur/klima/miljø) specifically for green research. Fond21 gives research-specific green categories; fond19 covers the broader environmental formål including non-research grants.
- For "green research" questions, prefer fond21 for topic detail. For "environmental grants overall" use fond19 or fond01 formal=1220.