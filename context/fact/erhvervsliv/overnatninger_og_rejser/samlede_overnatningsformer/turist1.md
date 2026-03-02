table: fact.turist1
description: Overnatninger efter overnatningsform, sæsonkorrigering, gæstens nationalitet og tid
measure: indhold (unit Antal)
columns:
- overnatf: values [120=Hoteller, 130=Feriecentre, 140=Camping, 150=Vandrerhjem, 170=Feriehuse]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark]
- tid: date range 2004-01-01 to 2025-08-01

notes:
- saeson is a measurement selector — every dimension combination appears exactly twice: once as EJSÆSON (raw, not seasonally adjusted) and once as SÆSON (seasonally adjusted). ALWAYS filter to one: WHERE saeson = 'SÆSON' or WHERE saeson = 'EJSÆSON'. Without this filter all aggregations double-count, and mixing the two is meaningless.
- No omrade column — this table has no regional breakdown. For regional data use turist (overnatninger) or turist2 (gæster).
- nation1 is limited to just three values (TOT, DAN, UDLAN) — no individual country breakdown. Use turist for full nationality detail.
- overnatf covers specific accommodation types only (120=Hoteller, 130=Feriecentre, 140=Camping, 150=Vandrerhjem, 170=Feriehuse) — no aggregate "100=Alle typer" or "160=Lystbådehavne". You cannot get a single total across all accommodation types from this table.
- No periode column — no monthly sub-period; each tid is a single monthly observation. This makes it simpler than turist/turist2 which have the ambiguous periode column.