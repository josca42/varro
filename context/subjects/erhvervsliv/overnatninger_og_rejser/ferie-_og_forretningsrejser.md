<fact tables>
<table>
id: ff1
description: Ferierejser til udlandet efter destination, varighed og tid
columns: destina, kmdr, tid (time), indhold (unit Pct.)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: ff2
description: Ferierejser efter destination, varighed, formål og tid
columns: destina, kmdr, formaaal, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ff3
description: Antal rejser efter formål med rejse, transportmiddel, varighed, destination og tid
columns: seg, transmid, kmdr, destina, tid (time), indhold (unit Antal)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: ff4
description: Ferierejser efter formål med rejse, overnatningsform, varighed, destination og tid
columns: seg, overnatf, kmdr, destina, tid (time), indhold (unit Pct.)
tid range: 2017-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- ff3 is the only count table (Antal rejser). ff1, ff2, ff4 are all percentage/share tables — their indhold values already sum to ~100 within a dimension slice and must not be summed across categories.
- For trip counts by transport mode: use ff3. For accommodation shares: use ff4. For destination shares of holidays abroad: use ff1. For purpose-of-trip shares: use ff2.
- ff1 vs ff2 destination granularity: ff1 has 50 individual country/region codes (abroad only); ff2 has just 2 (DAN / UDLAN). Use ff1 when the question is about which foreign country, ff2 when the question is domestic vs abroad.
- ff3 and ff4 cover both ferierejser (seg=6) and forretningsrejser (seg=8); ff1 and ff2 cover ferierejser only.
- Time coverage gap: ff3/ff4 start in 2017, ff2 in 2007, ff1 in 2001. For historical trends in holiday destinations, ff1 is the only option.
- All tables have a kmdr column splitting short (<4 nights) vs long (≥4 nights) trips. Always filter to one value or handle both separately — queries without a kmdr filter will double-count.
- Series break in ff2: formaaal categories collapsed from ~12 to 4 after 2017. Time series comparisons of trip purpose across this break are unreliable.
- forretningsrejser data (seg=8) in ff3/ff4 only starts from 2019, not 2017.