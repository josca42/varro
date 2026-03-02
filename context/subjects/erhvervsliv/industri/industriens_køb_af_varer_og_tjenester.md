<fact tables>
<table>
id: raav
description: Industriens køb af råvarer, komponenter og hjælpestoffer efter varegruppe (6 cifre), enhed og tid
columns: vargr6, enhed, tid (time), indhold (unit -)
tid range: 2002-01-01 to 2023-01-01
</table>
<table>
id: raav1
description: Industriens køb af varer efter varegruppe (2 cifre), branche (DB07), enhed og tid
columns: vargr2, branche07, enhed, tid (time), indhold (unit -)
tid range: 2002-01-01 to 2023-01-01
</table>
<table>
id: raav2
description: Industriens køb af emballage efter varegruppe (6 cifre), branche (DB07), enhed og tid
columns: vargr6, branche07, enhed, tid (time), indhold (unit 1.000 kr.)
tid range: 2002-01-01 to 2023-01-01
</table>
<table>
id: raav3
description: Industriens køb af tjenester efter varegruppe (6 cifre), branche (DB07), enhed og tid
columns: vargr6, branche07, enhed, tid (time), indhold (unit -)
tid range: 2002-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- These four tables cover Danish manufacturing's annual purchases, split by purchase type: raav (raw materials/components/auxiliaries), raav2 (packaging), raav3 (services). raav1 is a hybrid — 2-digit product level with industry breakdown, covering the same goods as raav but at coarser product granularity.
- For the most granular product view with no industry sub-sector: use raav (6-digit product codes, all manufacturing aggregated). For product + industry breakdown: use raav1 (2-digit products × industry sector).
- For packaging purchases: raav2. For service purchases (R&D, logistics, cleaning, etc.): raav3. Neither has an equivalent in the other tables.
- All four tables share the same time range (2002–2023, annual) and the same enhed selector (V=Värdi 1.000 kr., P=Andel i pct. af omsætning). Always filter enhed to one value — forgetting this doubles or triples every result.
- raav1, raav2, raav3 all use the same branche07 column with 15 codes: B, C, CA–CM (manufacturing sub-sectors), plus custom aggregate codes BC (=B+C combined) and CDE (composition unclear — value is far smaller than C alone, likely D+E only). These custom codes are not in dim.nr_branche. When joining, note that B matches niveau 1/2/3 and C matches niveau 1/2 in the dim — always filter d.niveau to avoid row multiplication.
- For "what does industry buy most?" questions: raav1 vargr2='991' + enhed='V', grouped by branche07 (exclude BC/CDE if you want individual sectors).
- P (percentage of turnover) values across the four tables let you compare purchasing intensity across sectors, but they are rates — never sum them.