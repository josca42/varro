<fact tables>
<table>
id: ror1
description: Rørledningsnettet efter rørledningstype og tid
columns: ror, tid (time), indhold (unit Km)
tid range: 1981-01-01 to 2024-01-01
</table>
<table>
id: ror2
description: Investeringer i rørledningsnettet efter rørledningstype, enhed og tid
columns: ror, enhed, tid (time), indhold (unit Mio. kr.)
tid range: 1980-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- ror1 = network length (km); ror2 = investment spending (Mio. kr.). They cover the same pipeline types but measure different things — don't confuse them.
- Both tables use a 3-level `ror` hierarchy (100=total → 110/150=gas/oil subtotals → leaf codes). Always pick one hierarchy level; mixing levels double-counts.
- ror2 has an `enhed` column (price base: 1990/1995/2000/2004-priser). This is a measurement selector — always filter to one enhed or counts are 4x inflated.
- Oil investment data in ror2 ends in 2017; gas data continues to 2024. For questions about recent pipeline investment, results will be gas-only post-2017.