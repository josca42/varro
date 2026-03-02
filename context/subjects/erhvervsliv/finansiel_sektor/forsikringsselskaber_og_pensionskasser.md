<fact tables>
<table>
id: dnfpbal
description: Forsikrings- og pensionssektorens balance efter virksomhedstype, værdier, balancepost og tid
columns: virktypnb, vaerdi1, balpostnat1, tid (time), indhold (unit Mia. kr.)
tid range: 2015-01-01 to 2025-04-01
</table>
<table>
id: dnfphen
description: Forsikrings- og pensionssektorens hensættelser efter virksomhedstype, værdier, balancepost og tid
columns: virktypnb, vaerdi1, balpostnat1, tid (time), indhold (unit Mia. kr.)
tid range: 2015-01-01 to 2025-04-01
</table>
<table>
id: dnfpafkl
description: Forsikrings- og pensionssektorens afkast af investeringer, efter virksomhedstype, værdier, investeringstype, sektor, land og tid
columns: virktypnb, vaerdi1, investnat, sektornat, land, tid (time), indhold (unit Mia. kr.)
tid range: 2015-01-01 to 2025-09-01
</table>
<table>
id: dnfpafkv
description: Forsikrings- og pensionssektorens afkast af investeringer efter virksomhedstype, værdier, investeringstype, sektor, valuta og tid
columns: virktypnb, vaerdi1, investnat, sektornat, valuta, tid (time), indhold (unit Mia. kr.)
tid range: 2015-01-01 to 2025-09-01
</table>
<table>
id: dnfpinvl
description: Forsikrings- og pensionssektorens investeringer efter virksomhedstype, værdier, investeringstype, sektor, land og tid
columns: virktypnb, vaerdi1, investnat, sektornat, land, tid (time), indhold (unit Mia. kr.)
tid range: 2015-01-01 to 2025-09-01
</table>
<table>
id: dnfpinvv
description: Forsikrings- og pensionssektorens investeringer efter virksomhedstype, markedsværdier, investeringstype, sektor, valuta og tid
columns: virktypnb, markvaerdi, investnat, sektornat, valuta, tid (time), indhold (unit Mia. kr.)
tid range: 2015-01-01 to 2025-09-01
</table>
<table>
id: dnfpvale
description: Forsikrings- og pensionssektorens valutaeksponering og -afdækning efter værdier, valuta og tid
columns: vaerdi1, valuta, tid (time), indhold (unit Mia. kr.)
tid range: 2015-01-01 to 2025-09-01
</table>
</fact tables>

notes:
- All 7 tables cover 2015–2025 quarterly data. dnfpafkl, dnfpafkv, dnfpinvl, dnfpinvv extend to Q3 2025; dnfpbal and dnfphen only to Q2 2025.
- Table families: (1) Balance sheet: dnfpbal (full balance: assets + liabilities). (2) Provisions detail: dnfphen (hensættelser breakdown with payment flows). (3) Investment holdings: dnfpinvl (by country), dnfpinvv (by currency). (4) Investment returns: dnfpafkl (by country), dnfpafkv (by currency). (5) Currency hedging: dnfpvale.
- For investment portfolio size: use dnfpinvl (country breakdown) or dnfpinvv (currency breakdown), filter vaerdi1='BEHOLD'.
- For investment returns: use dnfpafkl (country) or dnfpafkv (currency). CRITICAL: vaerdi1=AFKPCT is a percentage rate (not Mia. kr.) — never sum it across dimensions. Filter to AFKDKK or AFKUVAL for amount-based queries.
- dnfpvale is the only table for currency exposure and hedging analysis. It has no virktypnb column (sector-level aggregate only).
- Shared gotcha across all 6 tables with virktypnb: ALL, PEN, LIV, PKS, SKADE are hierarchical — summing them overcounts. Use virktypnb='ALL' for sector totals. LOOKTHR (in afkl/afkv/invl/invv) is an alternative sector aggregate with domestic fund look-through, not a child of ALL.
- investnat is hierarchical in all investment/return tables: ALLINV is the total. Always filter to ALLINV for totals or pick non-overlapping children.
- land (dnfpafkl, dnfpinvl) and valuta (dnfpafkv, dnfpinvv, dnfpvale) contain custom aggregate codes not in their dim tables. Use ColumnValues to get labels with correct descriptions — dim joins only work for individual countries/currencies.
- For company-type breakdown: PEN (pension companies) = LIV (life insurance) + PKS (pension funds); SKADE = non-life insurance. These sub-types are in all tables except dnfpvale.