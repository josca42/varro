table: fact.regn50
description: Regnskabsstatistik for private byerhverv i mio. kr. efter branche, regnskabsposter og tid
measure: indhold (unit -)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx]; levels [2]
- regnskposter: values [ANTFIR=Firmaer (antal), XOM=Omsætning (mio. kr.), BESK=Antal beskæftigede (i årsværk), AARSV=Heraf: ansatte (i årsværk), ADR=Andre driftsindtægter (mio. kr.) ... XIDM=Investeringer i driftsmidler (Mio. kr.), XIFE=Investeringer i fast ejendom (mio. kr.), XIIAA=Investeringer i immaterielle anlægsaktiver (mio. kr.) , XOB=Driftsindtægter pr. beskæftiget (1000 kr.), gennemsnit, XLA=Løn pr. ansat (1000 kr.), gennemsnit]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- regnskposter is a measure-selector: MUST filter to one value or you mix units (antal, mio. kr., 1000 kr.). Use ColumnValues("regn50", "regnskposter") to see all measures.
- erhverv does NOT join to dim.db via standard kode match. The column uses DB07 Afsnit letter codes (B=Råstofindvinding, C=Industri, D=Energiforsyning, E=Vandforsyning, F=Bygge og anlæg, H=Transport, I=Hoteller og restauranter, J=Information og kommunikation, L=Ejendomshandel og udlejning, M=Videnservice, N=Rejsebureauer mv.) mixed with numeric DB07 codes (45, 46, 47, 95 = sub-groups within detailhandel/handel). dim.db only has numeric koder, so letter codes never join. Use ColumnValues("regn50", "erhverv") to browse all 16 codes with labels — no dim join needed.
- TOTR = I alt (total across all sectors). Filter WHERE erhverv != 'TOTR' if you want individual sectors.
- erhverv codes include both section-level (letters) and division-level (numbers 45/46/47/95). Don't sum all erhverv codes — the letter codes are not exhaustive here; they cover different sector groups than 45/46/47/95 which are detail breakdowns of the G-section (Handel). Summing all 16 codes would double-count vs TOTR is misleading; use TOTR or pick specific sectors.
