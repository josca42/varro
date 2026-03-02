<fact tables>
<table>
id: flyv41
description: Lufttransport af gods over betjente danske lufthavne efter lufthavn, transporttype og tid
columns: lufthavn, transport, tid (time), indhold (unit 100 ton)
tid range: 1990-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Only one table: flyv41, covering annual air cargo (100 ton) through Danish airports 1990–2024.
- Both dimension columns (lufthavn, transport) have inline coded values — no dim table joins needed.
- Always filter transport to a single value (0=total, 15=national, 25=international) and lufthavn to either the total (10010) or individual airports — never sum across all values of either column.