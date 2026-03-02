<fact tables>
<table>
id: bog02
description: Udkomne bøger efter emne, omfang, udgave, medie og tid
columns: boger, bogtype, udgave, medie, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: bog03
description: Bogproduktion efter emne, originalsprog, udgivet på, medie og tid
columns: boger, sprog, oversat, medie, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: bog04
description: Skolebøger og børnebøger efter emne, bogtype, udgave, medie og tid
columns: boger, btype, udgave, medie, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: bog05
description: Bogtitler efter emne, publiceringstype, medie og tid
columns: boger, oplag1, medie, tid (time), indhold (unit Antal)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: bog06
description: Kommercielt udkomne bøger efter emne, omfang, udgave, medie, originalsprog og tid
columns: boger, bogtype, udgave, medie, sprog, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: bogs01
description: Solgte bøger efter genre, format og tid
columns: genre, format, tid (time), indhold (unit Antal)
tid range: 2022-07-01 to 2024-04-01
</table>
<table>
id: bogs02
description: Solgte bøger efter hovedgenre, udgivelsessprog og tid
columns: hovedgenre, udgivelsessprog, tid (time), indhold (unit Antal)
tid range: 2022-07-01 to 2024-04-01
</table>
<table>
id: bogs03
description: Solgte bøger efter genre, originalsprog, udgivelsessprog og tid
columns: genre, sprog, udgivelsessprog, tid (time), indhold (unit Antal)
tid range: 2022-07-01 to 2024-04-01
</table>
<table>
id: kv2lit1
description: Forbrug af litteratur efter genre, hyppighed, køn, alder og tid
columns: genre, hyp, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2lit2
description: Forbrug af skønlitteratur efter format, køn, alder og tid
columns: format, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2lit3
description: Forbrug af skønlitteratur efter adgang, køn, alder og tid
columns: adgang, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2lit4
description: Barrierer for forbrug af litteratur efter årsag, køn og tid
columns: aarsag, kon, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Two distinct data sources: bog02-06 track *book production* (titles published), bogs01-03 track *book sales* (units sold). Don't mix them for the same question.
- bog02-06 are annual, 2007-2024 (bog05 from 2012, bog06 from 2009). bogs01-03 are quarterly, 2022 Q3 onwards — sales data is recent only.
- For book production by subject: bog02 (all books, by size/edition/media), bog03 (by original + publication language), bog04 (children's/school books only), bog05 (by publication type: Danish vs foreign editions), bog06 (commercially published only, adds original language).
- For book sales: bogs01 (genre × format, most detailed), bogs02 (genre × publication language, simplest), bogs03 (genre × original language × publication language).
- bogs01 and bogs03 genre column has a 3-level hierarchy (1000=total > 1010/1070/1200/1280=subtotals > leaf codes). Always pick one consistent level — mixing levels causes double-counting.
- All bog02-06 share the same boger subject codes (100=Bøger i alt, 101-118=skønlitteratur, 201-290=faglitteratur). boger=100 is the only aggregate; there is no skønlitteratur/faglitteratur subtotal.
- kv2lit1-4 are 2024-only survey tables (Pct.) about reading consumption habits: kv2lit1=frequency by genre, kv2lit2=format preferences, kv2lit3=access channels, kv2lit4=barriers. kv2lit2/3/4 have NON-mutually exclusive categories (values sum >100%) — never sum across the category column.