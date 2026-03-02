table: fact.hotel31
description: Hoteller og feriecentre efter størrelse, kapacitet og tid
measure: indhold (unit -)
columns:
- storrelse: values [TOT=Alle hoteller og feriecentre med mindst 40 senge, 40069=Hoteller og feriecentre med 40-69 senge, 70099=Hoteller og feriecentre med 70-99 senge, 100124=Hoteller og feriecentre med 100-124 senge, 125149=Hoteller og feriecentre med 125-149 senge, 150199=Hoteller og feriecentre med 150-199 senge, 200249=Hoteller og feriecentre med 200-249 senge, 250299=Hoteller og feriecentre med 250-299 senge, 300349=Hoteller og feriecentre med 300-349 senge, 350399=Hoteller og feriecentre med 350-399 senge, 400449=Hoteller og feriecentre med 400-449 senge, 450499=Hoteller og feriecentre med 450-499 senge, 500=Hoteller og feriecentre med mere end 500 senge]
- kapacitet: values [1080=Hoteller og feriecentre (antal), 1082=Udlejede værelser (antal), 1084=Overnatninger (antal), 1090=Værelser (antal), 1100=Senge (antal), 1110=Værelser (kapacitetsudnyttelse, pct.), 1120=Senge (kapacitetsudnyttelse, pct.)]
- tid: date range 1992-01-01 to 2025-08-01

notes:
- tid is monthly (like hotel3/hotel5). No omrade column — data is national level only. No regional breakdown available.
- storrelse covers only hotels/feriecentre with at least 40 beds. Smaller establishments are excluded. TOT = alle med mindst 40 senge (not all hotels in Denmark).
- kapacitet is a measurement selector — always filter to one value. Seven metrics: 1080=antal hoteller/feriecentre, 1082=udlejede værelser (antal), 1084=overnatninger (antal), 1090=antal værelser, 1100=antal senge, 1110=værelsesbel. pct., 1120=sengebel. pct. Note: 1082 and 1084 are available here (rented rooms and overnights) but not in hotel3. Never SUM across kapacitet.
- storrelse size bands are mutually exclusive and sum to TOT. For all large hotels combined, filter storrelse='TOT'.