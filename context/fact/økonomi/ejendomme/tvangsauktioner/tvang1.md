table: fact.tvang1
description: Bekendtgjorte tvangsauktioner efter type og tid
measure: indhold (unit Antal)
columns:
- type: values [5520010001=Tvangsauktioner i alt, 84=Region Hovedstaden (2007 -), 85=Region Sjælland (2007 -), 83=Region Syddanmark (2007 -), 82=Region Midtjylland (2007 -), 81=Region Nordjylland (2007 -), 5520010010=Landbrugsejendomme, 5520010020=Enfamiliehuse, 5520010030=Ejerlejligheder, 5520010040=Sommerhuse, 5520010050=Ejendomme med 2 eller flere lejligheder, 5520010060=Blandet beboelses- og forretningsejendomme, 5520010062=Rene forretningsejendomme (2018-), 5520010064=Fabrik- og lagerejendomme (2018-), 5520010066=Andet bebygget (2018-), 5520010070=Ubebyggede grunde, 5520010082=Erhvervsejendomme ( -2017), 5520010084=Nedlagte landbrug ( -2017), 5520010101=Tvangsauktioner i alt (sæsonkorrigeret)]
- tid: date range 1993-01-01 to 2025-09-01

notes:
- type encodes multiple orthogonal categorizations in one column — never sum across all type values. Pick one lens at a time:
  - National total: type = '5520010001'
  - By region (from 2007): type IN ('81','82','83','84','85')
  - By property type: type IN ('5520010010','5520010020','5520010030','5520010040','5520010050','5520010060','5520010070', ...)
  - Seasonally adjusted total: type = '5520010101'
- The regional codes 81-85 only have data from 2007 (225 rows vs 393 for property types from 1993).
- Property type categories changed in 2018: pre-2018 "Erhvervsejendomme" (5520010082) and "Nedlagte landbrug" (5520010084) were replaced by three finer codes (5520010062, 5520010064, 5520010066). Avoid summing across these without accounting for the break.
- Monthly frequency. Use ColumnValues("tvang1", "type") to see the full list of type codes with labels.