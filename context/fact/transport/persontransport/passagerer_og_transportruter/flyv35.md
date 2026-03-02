table: fact.flyv35
description: Passagerer på udenrigsflyvninger efter rejselængde, flyvning, enhed og tid
measure: indhold (unit 1.000 personer)
columns:
- rejse: values [0=I ALT, 500=1-1000 km, 510=1001-2000 km, 515=2001-3000 km, 520=3001-4000 km, 525=4001-5000 km, 530=5001 km eller mere]
- flyvning: values [20080=Flyvninger i alt, 20085=Ruteflyvninger, 20090=Charter/taxi flyvning]
- maengde4: values [160=Mio. personkm, 3020=Passagerer]
- tid: date range 2004-01-01 to 2024-01-01

notes:
- maengde4 is a measurement selector with two incompatible units (Mio. personkm vs. 1.000 passagerer). Always filter to exactly one maengde4 value.
- rejse=0 and flyvning=20080 are totals — filter to these for overall figures, or to individual codes for breakdown. Do not include totals alongside their sub-categories in a sum.
- International flights only. Annual data.
