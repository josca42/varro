<fact tables>
<table>
id: statusu1
description: 18-25 åriges ungdomsuddannelser efter uddannelsesstatus, uddannelse, alder, køn, herkomst og tid
columns: uddstat, uddannelse, alder, kon, herkomst, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusu2
description: 18-25 årige efter uddannelsesstatus, uddannelse, alder, forældres højest fuldførte uddannelse og tid
columns: uddstat, uddannelse, alder, forudd1, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusu3
description: 18-25 årige efter uddannelsesstatus, alder, forældres indkomstniveau og tid
columns: uddstat, alder, forind, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusu4
description: 18-25 årige efter uddannelsesstatus, alder, forældres beskæftigelsesstatus og tid
columns: uddstat, alder, forbesk, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusu5
description: 18-25 årige efter uddannelsesstatus, alder, grundskoleinstitutionstype og tid
columns: uddstat, alder, grundskol, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusu6
description: 18-25 årige efter uddannelsesstatus, uddannelse, grundskolens beliggenhed og tid
columns: uddstat, uddannelse, grundbel, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: statusu7
description: 18-25 årige efter uddannelsesstatus, alder, gns. grundskolekarakter for dansk og matematik og tid
columns: uddstat, alder, dkmat, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: laby36a
description: 20-åriges ungdomsuddannelser (andel i procent) efter kommunegruppe, uddannelsesstatus og tid
columns: komgrp, uddstat, tid (time), indhold (unit Andel i pct.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: laby36
description: 18-25 åriges ungdomsuddannelser efter uddannelsesstatus, uddannelse, alder, kommunegruppe og tid
columns: uddstat, uddannelse, alder, komgrp, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All tables cover 18–25-year-olds and run from 2008 to 2024. All uddstat columns include AA_TOTAL (all statuses combined) — always filter to the uddstat value you want.
- Core breakdowns live in separate tables by background variable:
  - statusu1: gender (kon) and origin (herkomst) — the most commonly needed demographic breakdown
  - statusu2: parental education level (forudd1)
  - statusu3: parental income bracket (forind)
  - statusu4: parental employment status (forbesk)
  - statusu5: primary school type (grundskol) — folkeskole vs private vs efterskole etc.
  - statusu6: municipality of primary school (grundbel) — geographic breakdown via dim.nuts niveau 3
  - statusu7: primary school grades in Danish + Math (dkmat) — 4 grade bands
- laby36 vs laby36a: laby36 gives counts (Antal) for ages 18–25 by kommunegruppe; laby36a gives percentage shares for 20-year-olds only by kommunegruppe. Use laby36a for quick "completion rate by kommunegruppe" without needing to compute shares yourself.
- herkomst gotcha (statusu1): fact codes are 0/10/20/30, not 1/2/3. The dim.herkomst join requires dividing by 10, but since there are only 3 categories the inline codes are usually sufficient — no join needed.
- uddstat totals: AA_TOTAL is the aggregate of all education statuses. The four status categories (FULDFOERT, IGANG, AFBRUDT, INGENREG) partition the total — summing them equals AA_TOTAL.
- For a simple "how many completed/dropped out" query: use statusu1 (most dimensions) or any statusu table filtered to uddstat='FULDFOERT', alder='IALT', and all other non-focus columns set to their total values.
- Map: statusu6 supports choropleth via context/geo/kommuner.parquet — merge on grundbel=dim_kode. Excludes grundbel=0 and grundbel=98. Note: geography is municipality of primary school, not student's home municipality.