table: fact.aus05
description: Kontanthjælpsmodtagere (ikke arbejdsmarkedsparate) og feriedagpengemodtagere efter ydelsestype, sæsonkorrigering og tid
measure: indhold (unit Antal)
columns:
- ydelsestype: values [FKOM45=Aktiverede kontanthjælpsmodtagere (ikke arbejdsmarkedsparate), FPASSIV=Øvrige kontanthjælpsmodtagere (ikke arbejdsmarkedsparate), FFERIE=Feriedagpenge]
- saeson: values [10=Sæsonkorrigeret, 11=Ikke sæsonkorrigeret]
- tid: date range 2007-01-01 to 2025-09-01

notes:
- saeson is a measurement selector: every (ydelsestype, tid) appears twice. Filter to one: 10=sæsonkorrigeret or 11=ikke sæsonkorrigeret.
- ydelsestype: FKOM45, FPASSIV, FFERIE are three independent series — not summing categories, just different types in the same table. FKOM45+FPASSIV = alle kontanthjælpsmodtagere (ikke arbejdsmarkedsparate).
- Covers a niche group: kontanthjælpsmodtagere that are NOT arbejdsmarkedsparate (not included in standard bruttoledige count) and feriedagpengemodtagere. National figures only, no demographic breakdown.