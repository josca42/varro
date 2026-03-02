table: fact.regn10
description: Regnskabsstatistik for private byerhverv i mio. kr. efter branche, regnskabsposter og tid
measure: indhold (unit -)
columns:
- erhverv: join dim.nr_branche on erhverv::text=kode [approx]; levels [4]
- regnskposter: values [ANTFIR=Firmaer (antal), XOM=Omsætning (mio. kr.), BESK=Antal beskæftigede (i årsværk), AARSV=Heraf: ansatte (i årsværk), ADR=Andre driftsindtægter (mio. kr.) ... XINT=INVESTERINGER, NETTO (mio. kr.), XOB=Driftsindtægter pr. beskæftiget (1000 kr.), gennemsnit, XLA=Løn pr. ansat (1000 kr.), gennemsnit, XOBM=Driftsindtægter pr. beskæftiget (1000 kr.), median, XLAM=Løn pr. ansat (1000 kr.), median]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md
notes:
- erhverv uses 101 custom NR-branche derived codes (e.g. 6000, 10001, 26001) that mostly don't join to dim.nr_branche. Only 23/101 match dim.nr_branche at niveau 4 directly by code. Use ColumnValues("regn10", "erhverv") — the labels are embedded (e.g. "10001 Slagterier", "26001 Fremst. af computere og kommunikationsudstyr mv."). No reliable dim join strategy; treat erhverv as a self-labeling coded column.
- This is the most granular industry breakdown in the regnskab tables (101 sub-branches vs 16 in regn50). Choose regn10 when you need fine-grained industry detail; choose regn50 for broad sector overview.
- regnskposter is a measure-selector: MUST filter to one value. Same large set as regn50 (antal, mio. kr., 1000 kr. gennemsnit/median). Use ColumnValues("regn10", "regnskposter").
- No total code in erhverv — to get an all-industry total, SUM across the individual codes (there's no TOTR equivalent here, unlike regn50).
