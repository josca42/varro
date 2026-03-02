<fact tables>
<table>
id: gron1a
description: Grønne varer og tjenester (ny gruppering 2024) efter miljøformål, branche, enhed og tid
columns: mformaal, branche, enhed, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: gron1
description: Grønne varer og tjenester efter miljøformål, branche, enhed og tid
columns: mformaal, branche, enhed, tid (time), indhold (unit -)
tid range: 2012-01-01 to 2023-01-01
</table>
<table>
id: gron2
description: Grønne varer og tjenester efter branche (DB07), miljøformål, enhed og tid
columns: branche07, mformaal, enhed, tid (time), indhold (unit -)
tid range: 2012-01-01 to 2023-01-01
</table>
<table>
id: mreg22
description: Offentlig miljøbeskyttelse efter miljøformål, udgifter/indtægter, sektor og tid
columns: kategori, ui, sektor, tid (time), indhold (unit 1.000 kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: mbu
description: Industriens miljøbeskyttelsesudgifter efter branche (DB07), miljøformål og tid
columns: branche07, mformaal, tid (time), indhold (unit Mio. kr.)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: mreg21
description: Grønne afgifter efter miljøkategori og tid
columns: miljokat, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: mrs1
description: Grønne afgifter efter branche, miljøkategori og tid
columns: branche, skatteart, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: mms1
description: Miljøstøtte efter miljøkategori og tid
columns: miljokat, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: mms2
description: Miljøstøtte efter miljøformål og tid
columns: mformaal, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: mms3
description: Miljøstøtte efter branche, miljøkategori og tid
columns: branche, miljokat, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- For green goods and services (grønne varer og tjenester): gron1a (new 2024 classification, 2015–2023) and gron1 (old classification, 2012–2023) have the same sector breakdown but different mformaal codes. gron2 (2012–2023) has detailed DB07 industry breakdown but fewer mformaal categories. All three have an enhed column (measurement selector) — always filter to one enhed (XOM/EKS/BESK/XVT) or sums are meaningless.
- For public environmental protection spending: mreg22 (1995–2024) — covers all public sectors with CEPA environmental purpose breakdown and full expenditure/revenue breakdown. Note: kategori column uses CEPA1–CEPA9 codes, not plain numeric; join as REPLACE(f.kategori,'CEPA','') = d.kode::text.
- For industry environmental protection spending: mbu (2014–2023, industry only). mformaal mixes expenditure types (G_11–G_14) and environmental purposes (G_15/G_20/G_25...) in one column — pick one grouping, not both.
- For green taxes: mreg21 (1995–2024, national aggregate by tax type) and mrs1 (1995–2024, by industry + tax type). mrs1.branche uses V-prefix coding — join dim.nr_branche with TRIM(d.kode) = REPLACE(REGEXP_REPLACE(f.branche,'^V',''),'_','-').
- For environmental subsidies: three complementary tables all covering 1995–2024. mms1 = by detailed kategori (hierarchical SUB codes). mms2 = by environmental purpose (MF codes). mms3 = by industry + top-level kategori only. Use mms3 when you need industry breakdowns; mms1/mms2 for detailed category analysis.
- Common pitfall across all tables: mformaal, miljokat, ui, and sektor columns all contain hierarchical totals mixed with sub-categories. Summing all values double-counts. Always identify and filter to a single level before aggregating.
