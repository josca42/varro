table: fact.bil57
description: Brugte personbiler efter sæsonkorrigering og tid
measure: indhold (unit Antal)
columns:
- saeson: values [3080=Brugtvognshandel, total, 3085=Brugtvognshandel i husholdninger, 3090=Brugtvognshandel i erhverv, 3095=Brugtvognshandel, total, sæsonkorrigeret, 3100=Brugtvognshandel i husholdninger, sæsonkorrigeret, 3105=Brugtvognshandel i erhverv, sæsonkorrigeret]
- tid: date range 2004-01-01 to 2025-09-01
notes:
- saeson encodes 6 independent series — 3 segments × 2 variants (raw vs. seasonally adjusted). Do NOT sum across saeson values.
  - 3080=total raw, 3085=husholdninger raw, 3090=erhverv raw
  - 3095=total sæsonkorrigeret, 3100=husholdninger sæsonkorrigeret, 3105=erhverv sæsonkorrigeret
- 3080 = 3085 + 3090 (verified numerically). Use 3080 for total used-car trade without a dim breakdown.
- No fuel-type breakdown — for that, use bil56. Goes back to 2004-01-01, four years earlier than bil56.
- Simple table: saeson × tid only. Pick one saeson code, no other filters needed.
