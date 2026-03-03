<fact tables>
<table>
id: vie1
description: Gennemsnitsalder for viede mænd og kvinder efter alder og tid
columns: alder, tid (time), indhold (unit -)
tid range: 1901-01-01 to 2024-01-01
</table>
<table>
id: vie7
description: Vielser efter type og tid
columns: type, tid (time), indhold (unit Antal)
tid range: 1989-01-01 to 2024-01-01
</table>
<table>
id: vie9
description: Vielser efter vielsesmyndighed, vielsesmåned og tid
columns: vimyn, vimdr, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: viedag
description: Vielser efter vielsesdag, vielsesmåned og tid
columns: vdag, vimdr, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: vie225
description: Vielser efter mandens eller ældste persons bopæl, Kvindens eller yngste persons bopæl, mandens eller ældste persons alder, kvindens eller yngste persons alder, mandens eller ældste persons tidligere civilstand, kvindens eller yngste persons tidligere civilstand og tid
columns: bopaegt1, bopaegt2, alderaegt1, alderaegt2, civilaegt1, civilaegt2, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: vie325
description: Vielser efter mandens eller ældste persons bopæl, Kvindens eller yngste persons bopæl, vielsesmåned, vielsesmyndighed og tid
columns: bopaegt1, bopaegt2, vimdr, vimyn, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: vie825
description: Vielser efter mandens eller ældste persons alder, kvindens eller yngste persons alder, vielsesmyndighed og tid
columns: alderaegt1, alderaegt2, vimyn, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: vie7kvt
description: Vielser efter type og tid
columns: type, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2025-06-01
</table>
<table>
id: vie825k
description: Vielser efter mandens eller ældste persons alder, kvindens eller yngste persons alder, vielsesmyndighed, vielsesmåned og tid
columns: alderaegt1, alderaegt2, vimyn, vimdr, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For annual marriage counts by type (man+woman vs same-sex): vie7 (1989–2024) or vie7kvt for quarterly (2020–2025Q2). Both have type='VIRP' as aggregate total — filter to VIRP for the total, or VMK/V2M/V2K for subtypes.
- For average marriage age trends back to 1901: vie1. Note that indhold is an average (not a count) and alder is a measurement selector — filter to one code per query.
- For monthly and authority-type breakdown (Kirkelig/Borgerlig/Udlandet): vie9 (2007–2024). Month codes are zero-padded '001'–'012' with 'TOT' as total. Use vimyn='TOT' AND vimdr='TOT' for annual national total.
- For marriage day patterns: viedag (2007–2024). Same zero-padded month coding as vie9. Day codes are D01–D31.
- For regional breakdown by both partners' kommuner: vie225 (also has age and previous civil status) or vie325 (has month and authority type instead). Both use code '0' as "I alt" marginal total in the bopæl columns — always include or exclude it explicitly. Both join dim.nuts at niveau 3 only (99 kommuner).
- For age × authority type: vie825 (2007–2024, longest series) or vie825k (2020–2024, adds month). Neither has total codes for vimyn or vimdr — sum across all values to get totals.
- Month code inconsistency across tables: vie9 and viedag use zero-padded strings '001'–'012' + 'TOT'; vie325 and vie825k use plain integers 1–12 (no total code, no zero-padding). Do not copy month filter values between these groups.
- All tables from 2007 onward use gender-neutral language (ældste/yngste person) to accommodate same-sex marriages.
- Map: vie225 and vie325 support choropleth maps at kommune level (niveau 3) via /geo/kommuner.parquet — merge on bopaegt1 or bopaegt2=dim_kode, fixing the other bopæl to '0'. Exclude codes 0 and 997.