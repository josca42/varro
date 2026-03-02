table: fact.oeko11
description: Økologiske bedrifter og arealer efter økologisk status, afgrøde og tid
measure: indhold (unit -)
columns:
- oekostatus: values [225=Areal i alt på økologiske bedrifter, 210=Omlægning til økologi ikke påbegyndt, 215=Under omlægning til økologi, 220=Fuldt omlagt økologisk areal]
- afgrode: values [1080=Areal i alt (ha), 1015=Korn (ha), 1020=Bælgsæd (ha), 1025=Rodfrugter (ha), 1030=Industrifrø (ha), 1035=Frø til udsæd (ha), 1040=Græs og grøntfoder (ha), 1045=Gartneri (ha), 1050=Braklægning (ha), 1055=Andre afgrøder (ha), 1070=Landbrugsafgrøder i alt (ha), 2000=Bedrifter (antal), 1075=Skov (ha)]
- tid: date range 2012-01-01 to 2024-01-01

notes:
- oekostatus 225 ("Areal i alt på økologiske bedrifter") is the aggregate of 210+215+220. Never sum all four oekostatus values — use 225 alone for totals, or 210/215/220 for breakdown by conversion status.
- afgrode mixes two semantic types: area measures in ha (1015–1080) and farm count (2000=Bedrifter antal). afgrode=2000 only exists under oekostatus=225. Filter to one type per query.
- afgrode 1080 ("Areal i alt") = 1070 ("Landbrugsafgrøder i alt") + 1075 ("Skov"). afgrode 1070 is itself the aggregate of 1015–1055. For crop-level breakdown use afgrode IN (1015,1020,1025,1030,1035,1040,1045,1050,1055) — exclude 1070 and 1080 to avoid double-counting.
- Typical pattern: WHERE oekostatus=225 AND afgrode=1080 for total organic area by year; swap oekostatus for breakdown by conversion stage.