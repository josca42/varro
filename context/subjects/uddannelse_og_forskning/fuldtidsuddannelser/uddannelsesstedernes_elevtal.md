<fact tables>
<table>
id: inst11
description: Uddannelsesinstitutioner med almengymnasiale uddannelser efter status, institution, uddannelse, herkomst, køn og tid
columns: fstatus, insti, uddannelse, herkomst, kon, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: inst12
description: Uddannelsesinstitutioner med erhvervsgymnasiale uddannelser efter status, institution, uddannelse, herkomst, køn og tid
columns: fstatus, insti, uddannelse, herkomst, kon, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: inst15
description: Uddannelsesinstitutioner med erhvervsfaglige uddannelser efter status, institution, uddannelse, herkomst, køn, alder og tid
columns: fstatus, insti, uddannelse, herkomst, kon, alder, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: inst16
description: Erhvervsakademier efter status, institution, uddannelse, herkomst, køn, alder og tid
columns: fstatus, insti, uddannelse, herkomst, kon, alder, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: inst17
description: Professionshøjskoler efter status, institution, uddannelse, herkomst, køn, alder og tid
columns: fstatus, insti, uddannelse, herkomst, kon, alder, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: inst18
description: Maritime uddannelsesinstitutioner efter status, institution, uddannelse, herkomst, køn, alder og tid
columns: fstatus, insti, uddannelse, herkomst, kon, alder, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: inst19
description: Politiet og forsvarets uddannelsesinstitutioner efter status, institution, uddannelse, herkomst, køn, alder og tid
columns: fstatus, insti, uddannelse, herkomst, kon, alder, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: inst20
description: Universiteter efter status, institution, uddannelse, herkomst, køn, alder og tid
columns: fstatus, insti, uddannelse, herkomst, kon, alder, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: inst25
description: Kunstneriske og kulturelle uddannelsesinstitutioner efter status, institution, uddannelse, herkomst, køn, alder og tid
columns: fstatus, insti, uddannelse, herkomst, kon, alder, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Each table covers one type of institution — pick the table that matches the sector you need: inst11=almengymnasiale (stx/hf), inst12=erhvervsgymnasiale (hhx/htx), inst15=erhvervsfaglige (EUD), inst16=erhvervsakademier, inst17=professionshøjskoler, inst18=maritime institutioner, inst19=politi og forsvar, inst20=universiteter, inst25=kunstneriske og kulturelle institutioner.
- All tables share the same structure: fstatus, insti, uddannelse, herkomst, kon, tid — plus alder in inst15–inst25.
- fstatus is the critical gotcha across all tables. It is a measurement selector (B=elever, F=fuldført, T=tilgang), not a summing dimension. Every row exists 3 times — once per fstatus value. Always filter to one: typically fstatus = 'B' for student counts.
- kon total is '10' (not 'TOT') across all tables.
- uddannelse codes have 2 hierarchy levels in most tables (5-char parent, 7-char child). inst20 has 3 levels (3-char, 5-char, 7-char). TOT is always available. Never GROUP BY uddannelse without filtering to a single level — parent codes sum their children.
- For cross-sector analysis (e.g. total students in higher education across all institution types), sum across inst16+inst17+inst18+inst19+inst20+inst25 at insti='TOT', uddannelse='TOT', fstatus='B'. These tables do not overlap.
- inst15 is the largest in terms of uddannelse codes (EUD has many sub-programs). inst18 and inst19 are the smallest (9 and 6 institutions respectively).