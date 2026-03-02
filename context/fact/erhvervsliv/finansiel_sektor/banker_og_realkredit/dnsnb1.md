table: fact.dnsnb1
description: Specifikation til Nationalbankens balance - Beholdninger efter specifikation, instrument og tid
measure: indhold (unit Mia. kr.)
columns:
- specnat: values [I=Ikke angivet, V=Valutareserve, N=Kreditinstitutters nettostilling, U=Valutareserve omregnet til USD]
- instrument: values [ATA=Alle aktiver (aktiv), AKA=Indenlandske aktier mv. (aktiv), IOA=Indenlandske obligationer (aktiv), VFA=Indenlandske værdipapirer udstedt af finansielle institutioner (aktiv), VIA=Indenlandske værdipapirer i alt (aktiv) ... GAI=Garantier (ikke-balanceført post) (Ikke-sepcificeret), AFI=Andre forpligtelser (ikke-balanceført post) (Ikke specificeret), VPI=VP-registrerede obligationer pantsat til brug for kredit i Nationalbanken (2004M6-2011M7), VGI=VP-registrerede statspapirer pantsat til brug for kredit i Nationalbanken (2004M6-2011M7), VMI=VP-registrerede realkreditobl. pantsat til brug for kredit i Nationalbanken (2004M6-2011M7)]
- tid: date range 1987-01-01 to 2025-09-01

notes:
- Long time series from 1987 — Nationalbankens balance, holdings (beholdninger).
- specnat selects the reporting context: V=valutareserve, N=kreditinstitutters nettostilling, I=ikke angivet (most instruments), U=valutareserve omregnet til USD. Always filter to one specnat value.
- The same instrument code can appear under multiple specnat values (e.g. ATA appears under both I and V). Don't query without filtering specnat.
- instrument ATA=alle aktiver total; all other codes are sub-components.
- Unit is mia. kr. (billions).
- dnsnb1 = holdings (beholdninger); dnsnb2 = transactions (transaktioner). Use dnsnb1 for stock data, dnsnb2 for flow/change data.