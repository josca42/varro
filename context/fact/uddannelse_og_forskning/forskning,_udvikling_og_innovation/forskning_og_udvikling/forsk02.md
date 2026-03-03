table: fact.forsk02
description: Erhvervslivets udgifter til købte FoU-tjenester efter branche - størrelsesgruppe - region mv, leverandørtype og tid
measure: indhold (unit Mio. kr.)
columns:
- fui01: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1020=Bygge og anlæg, 1030=Handel, 1040=Transport ... 84=Region Hovedstaden, 85=Region Sjælland, 83=Region Syddanmark, 82=Region Midtjylland, 81=Region Nordjylland]
- levrtyp: values [80=Købte FoU-tjenester i alt, 90=Købte FoU-tjenester i Danmark i alt, 100=Fra virksomheder i samme koncern, 110=Fra andre danske virksomheder, 115=Fra konsulenter i Danmark, 120=GTSer i Danmark, 130=Universiteter mv. i Danmark, 140=Øvrige offentlige institutioner i Danmark, 150=Andre i Danmark, 160=Købte FoU-tjenester i udlandet i alt, 170=Udenlandske virksomheder i egen koncern, 180=Andre udenlandske virksomheder, 185=Fra konsulenter i udlandet, 190=Offentlige forskningsinstitutioner mv. i udlandet]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- fui01 encodes multiple classification perspectives — pick exactly ONE per query. See forsk01 notes for the full breakdown (industry 1000–1090, technology level 2000–2030, IT 2040–2080, knowledge services 2090–2160, size groups 3000–3040, regions 0/81–85).
- levrtyp='80' = grand total. '90' = domestic total, '160' = foreign total. Sub-items under 90 (100–150) and under 160 (170–190) are components — never sum sub-items together with their parent totals.
- To get total purchased R&D spending by industry: WHERE levrtyp='80', filter fui01 to industry range (1000–1090).
- Map: /geo/regioner.parquet — filter fui01 IN (81,82,83,84,85) for the region perspective, then merge on fui01=dim_kode.
