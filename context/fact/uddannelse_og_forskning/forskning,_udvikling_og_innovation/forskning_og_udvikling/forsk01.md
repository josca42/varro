table: fact.forsk01
description: Erhvervslivets udgifter til egen FoU efter branche - størrelsesgruppe - region mv, udgifter til egen FoU og tid
measure: indhold (unit Mio. kr.)
columns:
- fui01: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1020=Bygge og anlæg, 1030=Handel, 1040=Transport ... 84=Region Hovedstaden, 85=Region Sjælland, 83=Region Syddanmark, 82=Region Midtjylland, 81=Region Nordjylland]
- fui08: values [10=Udgifter til egen FoU i alt, 20=Driftsudgifter i alt, 30=Driftsudgifter: løn, 40=Driftsudgifter: øvrige, 50=Investeringsudgifter i alt, 60=Investeringsudgifter: bygninger, 70=Investeringsudgifter: apparatur]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- fui01 encodes four distinct classification perspectives in a single column — pick exactly ONE per query:
  - Industry (DB07): 1000=ALLE BRANCHER (total), 1010–1090 = individual branches
  - Technology level: 2000=total of this cut, 2010=Lavteknologisk, 2020=Mellemteknologisk, 2030=Højteknologisk (covers a subset of industries only — 2000 ≠ 1000)
  - IT-branches: 2040=IT-BRANCHER I ALT, 2050–2080 = sub-branches (subset of all industries)
  - Knowledge services: 2090=VIDENSERVICE I ALT, 2100–2160 = sub-branches (subset of all industries)
  - Size groups: 3000=STØRRELSESGRUPPER I ALT (total), 3010=Under 10, 3020=10–49, 3030=50–249, 3040=250+ årsværk
  - Regions: 0=REGIONER I ALT (total), 81=Region Nordjylland, 82=Region Midtjylland, 83=Region Syddanmark, 84=Region Hovedstaden, 85=Region Sjælland
  - All three aggregate totals (fui01='0', '1000', '3000') give the same national grand total. Never mix codes from different perspectives in the same aggregation.
- fui08='10' = Udgifter til egen FoU i alt (main aggregate). Values 20–70 are sub-components (driftsudgifter + investeringsudgifter). Filter to fui08='10' for a simple total.
- To get a single national total: WHERE fui01='1000' AND fui08='10' AND tid='...'
- Map: /geo/regioner.parquet — filter fui01 IN (81,82,83,84,85) for the region perspective, then merge on fui01=dim_kode.
