table: fact.dnintval
description: Nationalbankens internationale reserveaktiver efter instrument, aktivtype, datatype, valuta og tid
measure: indhold (unit Mia. kr.)
columns:
- instrument: values [AMS=Aktiver modtaget som sikkerhed, FD1=Finansielle derivater, andre end forwards og swaps, FIN=Finansielle derivater, i alt, FOR=Finansielle derivater, Forwards, GUL=Guld (monetært), LIC=Lån og indskud i valuta, centralbanker og BIS, LIO=Lån og indskud i valuta, øvrige sektorer, LIP=Lån og indskud i valuta, danske pengeinstitutter, LIT=Lån og indskud i valuta, i alt, LIU=Lån og indskud i valuta, udenlandske pengeinstitutter, RES=Reservestillingen over for IMF, SDR=Særlige trækningsrettigheder i IMF (SDR), SWA=Finansielle derivater, swaps, UAK=Udlånte aktiver, VAL=Reserveaktiver i alt, VIP=Værdipapirer i valuta, i alt]
- akttyp: values [V=Reserveaktiver, A=Andre valutaaktiver, E=Andet]
- data: values [S=Beholdning, ultimo periode, K=Kursregulering (Kun Reserveaktiver i alt)]
- valuta: join dim.valuta_iso on valuta=kode [approx]
- tid: date range 1999-12-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- valuta has only 3 codes: Z41=alle valutaer (aggregate total, ~90% of rows), SDX and SDZ (SDR-related reporting). None of these are ISO 4217 codes — the dim.valuta_iso link is incorrect (0% match). Treat valuta as inline values.
- akttyp distinguishes: V=reserveaktiver (the main category), A=andre valutaaktiver, E=andet. Rows across akttyp are not additive for the same instrument — they're different categories.
- data: S=end-of-period holding (use for stock data), K=revaluation adjustments (only valid for VAL/instrument=reserveaktiver i alt).
- instrument hierarchy: VAL=reserveaktiver i alt (total); GUL, VIP, LIT, RES, SDR, FIN are sub-components. LIT=lån og indskud i alt (LIC+LIO+LIP+LIU). FIN=finansielle derivater (FD1+FOR+SWA). Don't sum sub-components with VAL.
- For total foreign reserves: instrument='VAL', akttyp='V', data='S', valuta='Z41'.