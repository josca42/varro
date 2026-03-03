<fact tables>
<table>
id: ski6
description: Skilsmisser efter type og tid
columns: type, tid (time), indhold (unit Antal)
tid range: 1999-01-01 to 2024-01-01
</table>
<table>
id: ski125
description: Skilsmisser efter mandens eller ældste persons bopæl, Kvindens eller yngste persons bopæl, mandens eller ældste persons alder, kvindens eller yngste persons alder, ægteskabets varighed og tid
columns: bopaegt1, bopaegt2, alderaegt1, alderaegt2, agtvar, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ski225
description: Skilsmisser efter mandens eller ældste persons bopæl, Kvindens eller yngste persons bopæl, skilsmissemåned og tid
columns: bopaegt1, bopaegt2, skmdr, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ski55
description: Skilsmisseprocent efter enhed og tid
columns: tal, tid (time), indhold (unit Pct.)
tid range: 1986-01-01 to 2024-01-01
</table>
<table>
id: opl2025
description: Ægteskaber efter vielsesår, ægteskabets varighed, ægteskabsopløsning og tid
columns: vielsesaar, agtvar, agtopl, tid (time), indhold (unit -)
tid range: 2025-01-01 to 2025-01-01
</table>
<table>
id: ski6kvt
description: Skilsmisser efter type og tid
columns: type, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2025-06-01
</table>
<table>
id: ski125k
description: Skilsmisser efter mandens eller ældste persons alder, kvindens eller yngste persons alder, ægteskabets varighed, skilsmissemåned og tid
columns: alderaegt1, alderaegt2, agtvar, skmdr, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For total divorce counts by type (heterosexual vs same-sex): ski6 (annual 1999–2024) or ski6kvt (monthly 2020–2025, despite "kvt" in the name it is monthly). Both have type=SKIOP as aggregate total — never sum all types.
- For divorce rate (percentage): ski55 — single metric per year, longest series (1986–2024).
- For geographic breakdown (kommuner): ski125 (with age + duration) or ski225 (with month of divorce). Both use dim.nuts niveau=3. Code 0 = "Hele landet" (national total), code 997 = "Uoplyst bopæl" — neither joins to dim.nuts.
- For age + duration analysis without geography: ski125k (2020–2024, also has month of divorce).
- For cohort survival analysis (track a marriage year through time): opl2025 — unique table with vielsesaar × agtvar matrix. agtopl mixes counts (=1) and rates per 10,000 (=2,3,4); always filter to one agtopl value.
- ski125 and ski225 share the same bopaegt1/bopaegt2 geography — use ski125 when you need age/duration, ski225 when you need month of divorce.
- Map: ski125 and ski225 support choropleth maps at kommune level via /geo/kommuner.parquet — merge on bopaegt1=dim_kode or bopaegt2=dim_kode. Exclude codes '0' and '997'.
- None of the detailed tables (ski125, ski225, ski125k) include aggregate totals in the non-geographic dimensions (alderaegt, agtvar) — you cannot filter to an "IALT" code to get a marginal total for those columns. Sum across values in SQL instead.