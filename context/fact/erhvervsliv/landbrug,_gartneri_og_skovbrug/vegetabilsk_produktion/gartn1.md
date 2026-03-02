table: fact.gartn1
description: Produktion af frugt og grønt efter område, enhed, afgrøde og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- tal: values [500=Dyrket areal, hektar, 600=Høstet areal, hektar, 700=Produktion, tons]
- afgrode: values [10=Blomkål, 15=Broccoli, 20=Hvid- og spidskål, 25=Rødkål, 30=Kinakål ... 245=Anden buskfrugt, 250=Jordbær, 255=Hindbær, 260=Brombær, 265=Andre bær]
- tid: date range 2003-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. INNER JOIN gives 10 labeled geographies: niveau=1 (5 regioner: 81-85) and niveau=2 (5 landsdele: 4=Bornholm, 7=Fyn, 8=Sydjylland, 9=Østjylland, 10=Vestjylland). omrade=0 = Hele landet (not in dim.nuts), omrade=15 = unmapped aggregate.
- tal is a measurement selector: 500=Dyrket areal (ha), 600=Høstet areal (ha), 700=Produktion (tons). All three appear for the same omrade/afgrode/tid. Always filter to one.
- afgrode has 53 specific crop codes (10–265), all at the same granularity — no aggregate "I alt" code. Crops cover vegetables (10–130), soft fruits (135–165), orchard fruits (170–240), and berries (245–265).
- To get totals across crops, aggregate in SQL with SUM over the desired afgrode codes.
- Map: context/geo/landsdele.parquet (niveau 2) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.