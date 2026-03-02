table: fact.oeko88
description: Salg til foodservice efter varetype, kundegrupper, enhed og tid
measure: indhold (unit -)
columns:
- vartyp: values [10=Alle varer, 20=Økologiske varer, 30=Konventionelle varer]
- kundegrp: values [0=Alle kundegrupper, 100=Offentlige institutioner (hospitaler, børnehaver, uddannelse o.l.), 200=Kantiner på offentlige arbejdspladser, 300=Kantiner på private arbejdspladser, 400=Hoteller, restauranter, caféer o.l., 500=Andet (fx diner transportable, takeaway)]
- maengde6: values [30=Mio. kr., 40=Procent]
- tid: date range 2017-01-01 to 2024-01-01

notes:
- vartyp is a type selector: 10=Alle varer (total), 20=Økologiske varer, 30=Konventionelle varer. Same as oeko77: vartyp=10 = 20+30. Never sum all three.
- kundegrp: 0=Alle kundegrupper (total of all customer groups), 100=Offentlige institutioner, 200=Kantiner/offentlige, 300=Kantiner/private, 400=Hoteller/restauranter/caféer, 500=Andet. kundegrp=0 is the sum of 100–500, so do not combine kundegrp=0 with individual groups.
- maengde6 is a unit/measure selector: 30=Mio. kr., 40=Procent. The percent (40) expresses each kundegrp's share of the vartyp total — kundegrp=0 always equals 100%. Never sum percentage rows. For monetary totals use maengde6=30.
- Confirmed: vartyp=10 AND kundegrp=0 AND maengde6=40 = 100 (grand total share). maengde6=40 is safe only for reading individual customer group shares, not for summing.
- Longer history than oeko77 (from 2017 vs 2021). Use this table when you need customer segment breakdown over time.