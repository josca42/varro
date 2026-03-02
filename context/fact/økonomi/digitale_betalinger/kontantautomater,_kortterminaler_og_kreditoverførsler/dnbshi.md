table: fact.dnbshi
description: Hævninger og indskud af kontanter efter hævning og indskud, betjeningssted, datatype og tid
measure: indhold (unit -)
columns:
- haevind: values [HAEVNING=1. Hævninger i alt, HAEVNINGATM=1.1. Hævninger via kontantautomat, HAEVNINGKASSE=1.2. Hævninger ved kassen, INDSKUD=2. Indskud i alt, INDSKUDATM=2.1. Indskud via kontantautomat, INDSKUDKASSE=2.2. Indskud ved kassen, INDSKUDDBOKS=2.3. Indskud via døgnboks]
- betjen: values [IALT=I alt, EGNE=I kortholders banks egne filialer eller kontantautomater, ANDRES=I andres filialer eller kontantautomater (kun hævninger)]
- data: values [A=Antal (1.000 stk.) , V=Værdi (mio. kr.)]
- tid: date range 2016-01-01 to 2025-07-01

notes:
- data is a measurement selector: A=Antal (1.000 stk.) vs V=Værdi (mio. kr.). Always filter to one — every combination of haevind/betjen repeats once for A and once for V, so failing to filter silently doubles counts/values.
- haevind is hierarchical: HAEVNING=total withdrawals (parent of HAEVNINGATM + HAEVNINGKASSE), INDSKUD=total deposits (parent of INDSKUDATM + INDSKUDKASSE + INDSKUDDBOKS). Never sum a parent with its children.
- betjen: IALT=total, EGNE=own bank, ANDRES=other banks. IALT=EGNE+ANDRES, so never sum across betjen values. ANDRES only exists for withdrawals (haevind starting with HAEVNING*), not deposits — there's no INDSKUD/ANDRES.
- HAEVNINGKASSE/ANDRES (counter withdrawals at other banks) has a shorter series: count data (A) runs only to 2023-10-01 and value data (V) to 2024-04-01 — this sub-series appears discontinued. Be aware of gaps if comparing across haevind/betjen combinations.
- Typical query: total withdrawal count per month: SELECT tid, SUM(indhold) FROM fact.dnbshi WHERE haevind='HAEVNING' AND betjen='IALT' AND data='A' GROUP BY tid ORDER BY tid;