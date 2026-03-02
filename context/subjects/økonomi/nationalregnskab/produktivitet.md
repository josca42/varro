<fact tables>
<table>
id: np23
description: Arbejdsproduktivitet efter branche, prisenhed og tid
columns: branche, prisenhed, tid (time), indhold (unit -)
tid range: 1966-01-01 to 2024-01-01
</table>
<table>
id: np25
description: Produktivitetsudviklingen efter branche, type, prisenhed og tid
columns: branche, type, prisenhed, tid (time), indhold (unit Pct.)
tid range: 1967-01-01 to 2023-01-01
</table>
<table>
id: np25v
description: Vækstregnskab efter branche, type, prisenhed og tid
columns: branche, type, prisenhed, tid (time), indhold (unit Pct.)
tid range: 1967-01-01 to 2023-01-01
</table>
<table>
id: np28
description: Produktivitetsudviklingen, KLEMS efter branche, type, prisenhed og tid
columns: branche, type, prisenhed, tid (time), indhold (unit Pct.)
tid range: 1967-01-01 to 2017-01-01
</table>
</fact tables>

notes:
- All four tables share the same branche dim join bug: branche codes are V-prefixed (e.g. VA, VC, V01000, VD_E). Join with: JOIN dim.nr_branche d ON d.kode = REPLACE(SUBSTRING(f.branche, 2), '_', '-'). Combined-sector codes use underscore in the fact table but dash in dim (VD_E→D-E, VG_I→G-I, VM_N→M-N, VR_S→R-S).
- All tables include branche at multiple hierarchy levels simultaneously (niveaux 1–4 for np25/np25v/np28; 1–5 for np23). Always filter d.niveau to avoid double-counting.
- All tables repeat rows for each prisenhed (measurement unit) value. Always filter to one prisenhed.
- For absolute productivity level (index 2020=100): use np23 (prisenhed=LPR_I). Only np23 has level data; the others only have growth rates.
- For headline labour productivity growth by sector: use np25 (type=LP). Data from 1967, up to the most recent year.
- For growth accounting decomposition (including labour quantity/hours channel): use np25v (type=BVT for total GVA growth; individual types for contributions).
- For KLEMS decomposition with intermediate inputs (energy, materials, services): use np28 — but data only runs to 2017. For post-2017 analysis use np25 or np25v.
- Productivity-specific aggregate codes not in dim.nr_branche: PIALT (total economy, np23 only), PBY (private business), PMIALT (market economy), PTJEN (services). Use these directly by branche code without a dim join.