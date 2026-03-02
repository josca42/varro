table: fact.skib41
description: Godstransport over danske havne efter enhed og tid
measure: indhold (unit 1.000 ton)
columns:
- enhed: values [5000=GODSTRANSPORT I ALT, 5010=MED FRAGTSKIBE I ALT, 5020=Med fragtskibe, fra og til udland i alt, 5030=Med fragtskibe, indgående gods fra udland, 5040=Med fragtskibe, udgående gods til udland, 5050=Med fragtskibe, indgående gods fra indland i alt, 5060=Med fragtskibe, indgående gods fra indland, opfriskning af sten, sand og grus fra søbunden, 5070=Med fragtskibe, udgående gods til indland, 5080=MED FÆRGE I ALT, 5090=Med færger, fra og til udland, 5100=Med færger, indgående gods fra udland, 5110=Med færger, udgående gods til udland, 5120=Med færger, indenlansk gods]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- enhed is a hierarchical measurement selector — every year appears 13 times, once per enhed. Always filter to a single enhed value. Never sum across enhed values.
- enhed hierarchy: 5000=GODSTRANSPORT I ALT (top total) = 5010 (fragtskibe i alt) + 5080 (færger i alt). Sub-codes under fragtskibe: 5020 fra/til udland, 5030 indgående fra udland, 5040 udgående til udland, 5050 indgående fra indland, 5060 opfriskning sten/sand/grus, 5070 udgående til indland. Sub-codes under færger: 5090 fra/til udland, 5100 indgående fra udland, 5110 udgående til udland, 5120 indenrigs.
- For a simple yearly total of all goods transported: WHERE enhed='5000'.
- This is the longest series in the subject (from 1990) but has no port or cargo-type breakdown — only direction/vessel-type splits via enhed.