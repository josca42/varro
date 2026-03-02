table: fact.off13
description: Finansielle konti efter konto, finansielt instrument, aktiv/passiv, sektor, konsolideret/ukonsolideret, modpartssektor og tid
measure: indhold (unit Mio. kr.)
columns:
- konto: values [P=Primo, U=Ultimo, T=Transaktioner, O=Omvurderinger, A=Andre mængdemæssige ændringer]
- finins: values [F=F Finansielle instrumenter i alt, F.1=F.1 Monetært guld og særlige trækningsrettigheder (SDR), F.11=F.11 Monetært guld, F.12=F.12 Særlige trækningsrettigheder (SDR), F.2=F.2 Sedler og mønt samt indskud ... F.8=F.8 Andre forfaldne ikke-betalt mellemværender, F.81=F.81 Handelskreditter og forudbetalinger, F.89=F.89 Andre forfaldne, ikke betalte mellemværender, andre, BF.90=BF.90 Finansielle aktiver, netto, B.9=B.9 Finansielle fordringserhvervelse, netto]
- aktpas: values [AS=Finansielle aktiver, LI=Passiver]
- sektor: join dim.esa on sektor=kode [approx]
- konsol: values [CO=Konsolideret, NCO=Ukonsolideret]
- modseknat: values [MO=S. Alle, MOS1=S.1 Alle indenlandske sektorer, MOS2=S.2 Udlandet]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md
notes:
- sektor uses codes WITHOUT dots ('S13', 'S1311', etc.) while dim.esa uses dotted codes ('S.13', 'S.1311'). Direct join fails at 0%. To join: JOIN dim.esa d ON d.kode = REPLACE(f.sektor, 'S', 'S.'). Only 4 sektors exist: S13=offentlig forvaltning og service (total), S1311=stat, S1313=kommuner, S1314=regioner. S1312 (socialforsikring) is absent.
- konto: 5 account types that are NOT additive — P=Primo (opening stock), U=Ultimo (closing stock), T=Transaktioner (flows), O=Omvurderinger (revaluations), A=Andre mængdemæssige ændringer. Always filter to exactly one. For balance-sheet positions use P or U; for flows use T.
- aktpas: AS=Finansielle aktiver, LI=Passiver — always filter to one side.
- konsol: CO=Konsolideret, NCO=Ukonsolideret — pick one. For net public debt use CO.
- modseknat: MO=alle modparter, MOS1=indenlandske, MOS2=udland. MOS1/MOS2 only available for sektor=S13 with konsol=CO; other sektors have only MO.
- finins: hierarchical (F=total, F.1, F.11, F.12, F.2, ...). Don't sum parent and child codes.
- Annual (1995–2024). For quarterly without sektor split, see off22.
