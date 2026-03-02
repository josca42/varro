table: fact.dnshsrea
description: Danske realkreditobligationer holdt af eurolande (SHS) efter type af realkreditobligation, investorland, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- typreal: values [A0=Alle realkreditobligationer, FK=1.1 Fastforrentede obligationer, FK30=1.1.1 Fastforrentede konverterbare obl. 30 år løbetid, FKOV=1.1.2 Fastforrentede obl. øvrige, RTL=1.2 Obligationer bag rentetilpasningslån (RTL obligationer), V=1.3 Variabelt forrentede obligationer]
- investland: join dim.lande_uhv on investland=kode [approx]; levels [4]
- datat: values [N1=Beholdning - Nominel værdi, B1=Beholdning - Markedsværdi]
- tid: date range 2019-01-01 to 2025-04-01
dim docs: /dim/lande_uhv.md

notes:
- investland: 5 values total — I8=Euroområdet (i alt), DE, IE, IT, LU. I8 is an aggregate not in dim.lande_uhv (join will silently drop it). Use ColumnValues("dnshsrea", "investland") to see all available countries. For all euro-area holdings use investland='I8'; for country breakdown use the specific country codes (avoid mixing I8 with DE+IE+IT+LU as I8 includes all eurozone countries).
- datat is a measurement selector: N1=nominel værdi, B1=markedsværdi. Both represent beholdning (holdings). Filter to one.
- typreal has hierarchy: A0=alle realkreditobligationer includes FK (fastforrentede), RTL, and V. FK includes FK30 and FKOV. Filter to one level.
- This table covers only Danish mortgage bonds (realkreditobligationer) held by euro-area countries — a narrow, specialized table for tracking foreign institutional holdings of Danish realkreditobligationer.