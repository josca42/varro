table: fact.regnla4
description: Regnskabsstatistik for primære erhverv efter branche (DB07), regnskabsposter og tid
measure: indhold (unit -)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- regnskposter: values [ANTFIR=Firmaer (antal), XOM=Omsætning (mio. kr.), BESK=Antal beskæftigede (i årsværk), AARSV=Heraf: ansatte (i årsværk), ADR=Andre driftsindtægter (mio. kr.) ... XINT=INVESTERINGER, NETTO (mio. kr.), XOB=Driftsindtægter pr. beskæftiget (1000 kr.), gennemsnit, XLA=Løn pr. ansat (1000 kr.), gennemsnit, XOBM=Driftsindtægter pr. beskæftiget (1000 kr.), median, XLAM=Løn pr. ansat (1000 kr.), median]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- regnskposter is a measure-selector: MUST filter to a single value or you mix units (mio. kr., antal, 1000 kr.). 52 distinct measures. Use ColumnValues("regnla4", "regnskposter") to see all. Most used: ANTFIR=antal firmaer, XOM=omsætning, XVT=værditilvækst, AARE=resultat efter selskabsskat.
- branche07 has a leading-zero mismatch with dim.db. Fact stores 6-digit codes ("011100") while dim.db stores 5-digit ("11100"). Correct join: JOIN dim.db d ON LTRIM(f.branche07, '0') = d.kode::text. With this, 17/19 codes join. Shorter codes like "014", "031", "032" are 3-digit Gruppe niveau; they join to dim.db at niveau 3 (e.g., kode=14=Husdyravl).
- "A" = Landbrug, skovbrug og fiskeri total — not in dim.db. "01000" = Landbrug og gartneri subtotal — not in dim.db.
- Don't SUM across branche07 codes without filtering: aggregate codes (A, 01000, 014) include the detail codes below them (011100, 014100 etc.), so double-counting is easy. Filter to a single niveau for summation, e.g. WHERE branche07 LIKE '0_____' for 6-digit codes only.
- ColumnValues("regnla4", "branche07") shows all 19 codes with labels — use this to pick codes rather than browsing dim.db.