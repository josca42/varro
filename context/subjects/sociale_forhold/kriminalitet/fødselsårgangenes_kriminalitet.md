<fact tables>
<table>
id: straffo1
description: Fødselsårgange (opgjort pr 31. december 2024) efter enhed, fødselsår, køn, alder ved første dom, lovovertrædelse og tid
columns: overnat1, fodaar, konams, fdomald, lovov, tid (time), indhold (unit -)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: straffo2
description: Fødselsårgange (opgjort pr. 31. december 2024) efter enhed, fødselsår, køn, alder ved første frihedsstraf, frihedsstraf og tid
columns: overnat1, fodaar, konams, avffs, fristraf, tid (time), indhold (unit -)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: straffo3
description: Domme (opgjort pr. 31. december 2024) fordelt på fødselsårgang efter enhed, fødselsår, køn, alder på domstidspunktet, lovovertrædelse og tid
columns: overnat1, fodaar, konams, adom, lovov, tid (time), indhold (unit -)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: straffo4
description: Domme til frihedsstraf (opgjort pr. 31. december 2024) efter enhed, fødselsår, køn, frihedsstraf, alder på domstidspunktet og tid
columns: overnat1, fodaar, konams, fristraf, adom, tid (time), indhold (unit -)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All four tables have a single tid value (2024-01-01) — this is a cross-sectional snapshot of birth cohorts as of 31 December 2024, not a time series. The temporal dimension is age/birth year, not tid.
- All tables share overnat1 as a measurement selector that multiplies row counts — always filter it. Forgetting overnat1 silently inflates all aggregates.
- Two fundamentally different semantics across the tables:
  - straffo1/straffo2: Person-level, first-event tracking. Each person counted once (at age of first conviction/first prison sentence). Has TOT and sentinel values (IDOMT, IFRI) in age columns. overnat1: 100=count, 200=cumulative count, 300=% of cohort, 400=cumulative %.
  - straffo3/straffo4: Conviction-event rates per 1000 persons. Counts convictions (not persons) at each age. No TOT in age column. overnat1: 500=rate, 600=cumulative rate.
- For "what % of a birth cohort ever got convicted": straffo1 (overnat1=400, fdomald=TOT gives cumulative share). For "at which age was conviction most common": straffo3 (overnat1=500). For prison sentences specifically: straffo2 (person-level) or straffo4 (rate-level).
- straffo1 and straffo3 have lovov joining dim.overtraedtype but only cover Straffelov (niveaus 1 and 2). No Færdselslov or Særlov data in these tables.
- lovov (crime type) and fristraf (sentence type) values are NOT mutually exclusive within a single case/person — never sum across these columns. Use the top-level aggregates (lovov=1 or fristraf=1) for totals.
- fodaar covers 1965–2008, but older cohorts have data up to age 58 while younger cohorts have fewer age-level observations (e.g. the 2008 cohort only has data from age 15). Filter or GROUP BY carefully when comparing age-specific rates across cohorts.