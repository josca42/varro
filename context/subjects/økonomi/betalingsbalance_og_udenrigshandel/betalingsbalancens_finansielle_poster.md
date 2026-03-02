<fact tables>
<table>
id: dnbopm
description: Betalingsbalancens finansielle poster - transaktioner mellem Danmark og udlandet efter balance, instrument, indenlandsk sektor, valuta, land og tid
columns: balanc, instrument, indsek, valuta, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-08-01
</table>
</fact tables>

notes:
- This subject contains only one table: dnbopm (monthly, 2005–2025).
- dnbopm covers Denmark's financial account transactions with the rest of the world, broken down by instrument (direct investment, portfolio, derivatives, etc.), domestic sector, currency, and counterpart area.
- Neither the land nor valuta column joins to a dim table despite documentation suggesting so. Both are inline coded: land ∈ {Z9=world, B5=EU-27 excl. DK, I7=Eurozone}; valuta ∈ {Z01=all currencies, DKK}.
- Multiple hierarchical columns require care to avoid overcounting: instrument (100=total), indsek (1000=total), and balanc (N=A−P). For most questions, filter all three to their total values and then drill into the dimension of interest.