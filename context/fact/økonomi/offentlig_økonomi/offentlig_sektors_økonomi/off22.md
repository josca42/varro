table: fact.off22
description: Finansielle konti efter konto, finansielt instrument, aktiv/passiv, konsolideret/ukonsolideret, modpartssektor og tid
measure: indhold (unit Mio. kr.)
columns:
- konto: values [P=Primo, U=Ultimo, T=Transaktioner, OA=Omvurderinger og andre mængdemæssige ændringer]
- finins: values [F=F Finansielle instrumenter i alt, F.1=F.1 Monetært guld og særlige trækningsrettigheder (SDR), F.2=F.2 Sedler og mønt samt indskud, F.3=F.3 Gældsbeviser, F.31=F.31 Kortfristede gældsværdipapirer, F.32=F.32 Langfristede gældsværdipapirer, F.4=F.4 Lån, F.41=F.41 Kortfristede lån, F.42=F.42 Langfristede lån, F.5=F.5 Ejerandele og andele i investeringsforeninger, F.51=F.51 Ejerandele, F.52=F.52 Andele i investeringsforeninger, F.6=F.6 Forsikrings- og pensionsordninger og ordninger med standardiserede garantier, F.7=F.7 Finansielle derivater og medarbejderoptioner, F.8=F.8 Andre forfaldne ikke-betalt mellemværender, BF.90=BF.90 Finansielle aktiver, netto, B.9=B.9 Finansielle fordringserhvervelse, netto]
- aktpas: values [AS=Finansielle aktiver, LI=Passiver]
- konsol: values [CO=Konsolideret, NCO=Ukonsolideret]
- modseknat: values [MO=S. Alle, MOS1=S.1 Alle indenlandske sektorer, MOS2=S.2 Udlandet]
- tid: date range 1995-01-01 to 2025-04-01
notes:
- No sektor dimension — covers the whole public sector. For sektor breakdown (stat/kommuner/regioner), use off13 (annual only).
- konto: P=Primo, U=Ultimo, T=Transaktioner, OA=Omvurderinger og andre mængdemæssige ændringer (combined, vs separate O and A in off13). Not additive — always filter to one. For balance-sheet use P or U; for flows use T.
- aktpas: AS=Finansielle aktiver, LI=Passiver — always filter to one.
- konsol: CO=Konsolideret, NCO=Ukonsolideret — pick one.
- modseknat: MO=alle, MOS1=indenlandske, MOS2=udland — pick one; MO for totals.
- finins: hierarchical (F=total, F.1, F.2, F.3...). Don't sum parent and child codes.
- Quarterly (1995Q1–2025Q4).
