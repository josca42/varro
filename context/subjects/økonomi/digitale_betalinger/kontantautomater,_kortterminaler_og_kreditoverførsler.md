<fact tables>
<table>
id: dnbskk
description: Kontantautomater og kortterminaler efter enheder og tid
columns: enhed1, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2025-04-01
</table>
<table>
id: dnbshi
description: Hævninger og indskud af kontanter efter hævning og indskud, betjeningssted, datatype og tid
columns: haevind, betjen, data, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2025-07-01
</table>
<table>
id: dnbsvko
description: Kreditoverførsler i valuta efter type, retning, geografisk dækning, datatype og tid
columns: kortype, ret, geodaek, data, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2025-07-01
</table>
<table>
id: dnbsiko
description: Indenlandske kreditoverførsler i kroner efter type, initiering, datatype og tid
columns: kredit, init, datat, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- For ATM/terminal counts: dnbskk — number of cash machines and card terminals in Denmark. Quarterly, from 2016. No measurement selector; all values are raw counts. Pick parent codes (ATM/POS) for totals or subtypes for breakdown.
- For cash withdrawal/deposit activity: dnbshi — volumes and values by haevind type and betjen (own vs other bank). Quarterly, from 2016. Has data selector (A=count in thousands, V=value in millions DKK); always filter it.
- For domestic DKK credit transfers: dnbsiko — indenlandske kreditoverførsler in kroner only. Quarterly, from 2016. Use for Danish bank transfer volumes (straks, standard, intradag etc.). Has datat selector; always filter it.
- For cross-border or multi-currency credit transfers: dnbsvko — covers all currencies (DKK cross-border, SEPA, euro, other). Quarterly, from 2016. Has data selector; always filter it. Note: DKK in this table is only cross-border — domestic DKK is in dnbsiko.
- All tables except dnbskk have a measurement selector column (data / datat): A=antal (in thousands), V=værdi (in millions kr.). Forgetting to filter this doubles all results.
- All tables have hierarchical category columns with parent/total rows. Common pattern: IALT or a named total code is the parent; sub-codes are its children. Never sum parent + children.