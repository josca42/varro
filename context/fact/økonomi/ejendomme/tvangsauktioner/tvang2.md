table: fact.tvang2
description: Bekendtgjorte tvangsauktioner efter type og tid
measure: indhold (unit Antal)
columns:
- type: values [5520010001=Tvangsauktioner i alt, 84=Region Hovedstaden (2007 -), 85=Region Sjælland (2007 -), 83=Region Syddanmark (2007 -), 82=Region Midtjylland (2007 -) ... 5520010066=Andet bebygget (2018-), 5520010070=Ubebyggede grunde, 5520010082=Erhvervsejendomme ( -2017), 5520010084=Nedlagte landbrug ( -2017), 90=Uoplyst boligtype]
- tid: date range 1979-01-01 to 2025-07-01

notes:
- type encodes multiple orthogonal categorizations in one column — never sum across all type values. Pick one lens at a time:
  - National total: type = '5520010001'
  - By region (from 2007): type IN ('81','82','83','84','85')
  - By old geographic zone (pre-2007): type IN ('1','2','3') — 1=Hovedstadsregionen, 2=Øerne, 3=Jylland
  - By property type: type IN ('5520010010','5520010020', ...)
- tvang2 covers 1979–present but the geographic breakdown changes mid-series: old zones (codes 1–3) up to 2007, new regions (81–85) from 2007. Joining these across the break requires handling both code sets separately.
- No seasonally adjusted total (unlike tvang1 which has 5520010101).
- Code 90 = "Uoplyst boligtype" — auctions where property type is unknown. Exclude it when summarising by property type.
- Same 2018 property-type break as tvang1: Erhvervsejendomme/Nedlagte landbrug replaced by three finer codes.
- Monthly frequency. Use ColumnValues("tvang2", "type") for full code/label mapping.