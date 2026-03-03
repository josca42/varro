<fact tables>
<table>
id: ejdfoe1
description: Formue i fast ejendom efter værdisætning, bopælskommune, enhed, ejendomstype og tid
columns: vaerdi, bopkom, enhed, ejentyp, tid (time), indhold (unit -)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: ejerfof1
description: Husholdningernes formue i fast ejendom og gældskomponenter for familier efter komponenttype, bopælskommune, enhed, familietype og tid
columns: formgld, bopkom, enhed, famtype, tid (time), indhold (unit -)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: ejerfof2
description: Husholdningernes formue i fast ejendom og gældskomponenter for familier efter komponenttype, bopælskommune, enhed, husstandsgrupper og tid
columns: formgld, bopkom, enhed, husgrp, tid (time), indhold (unit -)
tid range: 2004-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- ejdfoe1: use when you need a breakdown by ejendomstype (12 types: enfamiliehuse, ejerlejligheder, sommerhuse, erhvervsejendomme, etc.) or when you want to compare markedsværdi vs offentlig ejendomsvurdering. Covers antal ejendomme, total mio. kr., and gennemsnit kr.
- ejerfof1: use when you need to break down real estate wealth/debt by familietype (enlige vs par, with/without children, by age). Has the same formue+gæld component structure as ejerfof2.
- ejerfof2: use when you need breakdown by socioøkonomisk status (selvstændige, lønmodtagerniveauer, pensionister, etc.) or by uddannelsesniveau. Same formue+gæld components as ejerfof1.
- All three tables share bopkom (kommune/region, 2004-2024) and have enhed as a measurement selector — always filter enhed to one value.
- All three require care with hierarchical columns: ejdfoe1 has ejentyp T as aggregate; ejerfof1/ejerfof2 have hierarchical formgld (105/135/145 are aggregates) and hierarchical famtype/husgrp totals. Summing without filtering these inflates results.
- Map: All three tables support choropleth maps via bopkom. Use /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on bopkom=dim_kode. Exclude bopkom='0'.