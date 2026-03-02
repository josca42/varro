table: fact.dnvalm
description: Valutakurser efter valuta, kurstype, opgørelsesmetode og tid
measure: indhold (unit -)
columns:
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- kurtyp: values [KBH=Valutakurser (DKK pr. 100 enheder valuta), TT3=Terminstillæg, 3 mdr. (kun USD og EUR fra 1998), DKK pr. 100 enheder valuta (USD 1998 dec-2013 dec og EUR 1999 jan-2013 dec), TT6=Terminstillæg, 6 mdr. (kun USD og EUR fra 1998), DKK pr. 100 enheder valuta (USD 1998 dec-2013 dec og EUR 1999 jan-2013 dec), INX=Indeks (kun nominel effektiv kronekurs), indeks 1980=100, REK=Real effektiv kronekurs baseret på forbrugerpriser, indeks 1980=100, DKI=Forbrugerprisindeks i Danmark, indeks 1980=100, Z9I=Vægtet udenlandsk forbrugerprisindeks, indeks 1980=100, EUI=Forbrugerprisindeks for euroområdet, indeks 2005=100, EFB=Bidrag til ændring i nominel effektiv kronekurs, procentpoint]
- opgoer: values [A=Månedsgennemsnit, E=Månedsultimo, B=Beregnet, Y=Årlig stigningstakt]
- tid: date range 1970-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- opgoer is a critical filter — always specify it to avoid duplicate rows per (valuta, kurtyp, tid). For spot rates (KBH): A=monthly average, E=month-end. B=calculated, Y=annual growth rate are additional computed series. Omitting opgoer gives 2 rows for every standard (valuta, kurtyp, month) combination.
- kurtyp is a measurement selector — always filter to one value. KBH=spot rate (applies to 54 currencies), TT3/TT6=3- and 6-month forward premiums (USD and EUR only, 1998+), INX=nominal effective exchange rate index (DKK only), REK=real effective exchange rate based on consumer prices (DKK only), EFB=contribution to change in nominal effective exchange rate (EUR, GBP, JPY, NOK, SEK, USD, X00, Z60 only). The EUI/DKI/Z9I kurtyp values are underlying consumer price indices used to compute REK.
- Values are DKK per 100 units of foreign currency (KBH). Divide by 100 for per-unit rate.
- valuta join: same issue as dnvald — 22 historical currencies (pre-euro national currencies + XDR + XEU) are present in the fact table but not in dim.valuta_iso.
- X00 and Z60 are composite basket codes that appear in EFB series; they are not in dim.valuta_iso.
- Typical spot rate query: WHERE kurtyp='KBH' AND opgoer='A' for monthly averages, or opgoer='E' for month-end closing rates.