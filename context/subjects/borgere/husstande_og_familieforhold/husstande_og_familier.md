<fact tables>
<table>
id: fam55n
description: Husstande 1. januar efter område, husstandstype, husstandsstørrelse, antal børn i husstand og tid
columns: omrade, hustyp, husstor, antbornh, tid (time), indhold (unit Antal)
tid range: 1986-01-01 to 2025-01-01
</table>
<table>
id: fam122n
description: Voksne 1. januar efter område, husstandstype, antal personer i husstand , antal børn i husstand, køn, alder og tid
columns: omrade, hustyp, antpersh, antbornh, kon, alder, tid (time), indhold (unit Antal)
tid range: 1986-01-01 to 2025-01-01
</table>
<table>
id: by4
description: Husstande 1. januar efter byområder og landdistrikter, husstandstype, antal børn og tid
columns: byer, hustyp, antborn, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: laby50
description: Husstandes afstand til nærmeste dagligvarebutik efter kommunegruppe, afstand og tid
columns: komgrp, afstand, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2022-01-01
</table>
<table>
id: laby50a
description: Husstandes afstand til nærmeste dagligvarebutik (andel i  pct.) efter kommunegruppe, afstand og tid
columns: komgrp, afstand, tid (time), indhold (unit Andel i pct.)
tid range: 2009-01-01 to 2022-01-01
</table>
<table>
id: fam44n
description: Familier 1. januar efter område, familietype, familiestørrelse, antal børn og tid
columns: omrade, famtyp, famstor, antborn, tid (time), indhold (unit Antal)
tid range: 1986-01-01 to 2025-01-01
</table>
<table>
id: laby04
description: Familier m/u børn i procent af alle familier i samme kommune eller kommunegruppe efter område, familietype og tid
columns: omrade, famtyp, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: fam100n
description: Voksne 1. januar efter område, familietype, antal personer i familien, antal børn i familien, køn, alder og tid
columns: omrade, famtyp, antpf, antbrnf, kon, alder, tid (time), indhold (unit Antal)
tid range: 1986-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- Households (husstande) vs families (familier): fam55n/fam122n/by4 count husstande (dwelling units); fam44n/fam100n/laby04 count familier (nuclear family units). A household can contain multiple families. Use husstand tables for "how many people live together," family tables for "couple/single-parent family structure."
- For counts by region/kommune: fam55n (husstande) or fam44n (familier) — both have omrade at niveau 1 (regioner) + 3 (kommuner) and go back to 1986. fam122n and fam100n are kommune-only (niveau 3), no regional or national aggregates.
- For demographic breakdown of adults (age/sex) within household/family types: fam122n (husstand-based) or fam100n (familie-based). Both have individual single-year ages from 15 upward and no total codes — very granular, always filter tid + omrade first.
- For family type percentages (ready-to-use rates): laby04 gives shares of family types as pct per landsdel or kommune from 2007. Faster than computing from fam44n counts if you just need shares.
- For sub-municipality geography: by4 has byområde and landdistrikt detail (1829 codes) from 2010, but only husstandstype + has-children breakdown. No dim join — use ColumnValues with fuzzy_match_str to find place codes.
- For distance to grocery store: laby50 (counts) and laby50a (pct) by kommunegruppe, 2009–2022. laby50a pct is share of each distance band that falls in a kommunegruppe — NOT the distribution within a kommunegruppe. Use laby50 counts to compute within-komgrp distributions.
- All fam/husstand count tables lack total codes in their category dimensions (hustyp, husstor, antbornh, famtyp, famstor, antborn, kon, alder). There is no IALT shortcut — to get marginal totals, SUM across all values of a dimension explicitly. Forgetting any dimension inflates counts.
- Map support: fam55n and fam44n support kommune + region choropleths; fam122n and fam100n support kommune-only; laby04 supports kommune + landsdel. All merge on omrade=dim_kode, exclude omrade=0. by4, laby50, laby50a have no standard geo join.