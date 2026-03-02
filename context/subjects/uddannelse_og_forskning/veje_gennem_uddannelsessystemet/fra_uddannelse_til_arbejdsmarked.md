<fact tables>
<table>
id: ovgarb10
description: Fra uddannelsesgrupper til fortsat uddannelse eller arbejdsmarked efter slutuddannelse i gruppen, herkomst, køn, uddannelsesstatus, status efter afgang, statustidspunkt efter afgang, alder ved afgang fra gruppe og tid
columns: uddangroup, ietype, kon, uddstat, statusafg, statustid, alderlev, tid (time), indhold (unit Antal)
tid range: 2012-01-01 to 2021-01-01
</table>
</fact tables>

notes:
- Only one table in this subject: ovgarb10 tracks labor market outcomes (employed/unemployed/outside workforce/still studying) for people who left an education group, measured at 3, 9, 15, and 21 months after departure.
- statustid (3M/9M/15M/21M) is a measurement selector — always filter to one value or results multiply by 4. The 9M snapshot is the most commonly cited in Danish education statistics.
- uddangroup encodes education at 3 hierarchy levels (length=3/5/7). Use length=7 for program-level detail (76 groups), length=3 for broad groupings (10 groups). Never sum across levels.
- statusafg is the outcome: 001=employed, 002=unemployed, 003=outside labor force, 000=still studying, 950=not in population. Use statusafg='TOT' only when summing across all outcomes.
- uddstat separates completers (0), dropouts (1), and partial completers (2); use uddstat='T' for all leavers combined.