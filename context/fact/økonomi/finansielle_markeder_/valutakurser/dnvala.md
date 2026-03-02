table: fact.dnvala
description: Valutakurser efter valuta, kurstype, opgørelsesmetode og tid
measure: indhold (unit -)
columns:
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- kurtyp: values [KBH=Valutakurser (DKK pr. 100 enheder valuta), TT3=Terminstillæg, 3 mdr. (kun USD og EUR fra 1998), DKK pr. 100 enheder valuta (USD 1998 dec-2013 dec og EUR 1999 jan-2013 dec), TT6=Terminstillæg, 6 mdr. (kun USD og EUR fra 1998), DKK pr. 100 enheder valuta (USD 1998 dec-2013 dec og EUR 1999 jan-2013 dec), INX=Indeks (kun nominel effektiv kronekurs), indeks 1980=100, REK=Real effektiv kronekurs baseret på forbrugerpriser, indeks 1980=100, DKI=Forbrugerprisindeks i Danmark, indeks 1980=100, Z9I=Vægtet udenlandsk forbrugerprisindeks, indeks 1980=100, EUI=Forbrugerprisindeks for euroområdet, indeks 2005=100, RET=Real effektiv kronekurs baseret på timelønninger, indeks 1980=100, LOI=Timelønsindeks for industrien i Danmark, sæsonkor., indeks 1980=100, LOU=Vægtet timelønsindeks for industrien i udlandet, sæsonkor., indeks 1980=100, EFB=Vigtigste valutaers bidrag til ændring i nominel effektiv kronekurs, procentpoint]
- opgoer: values [A=Årsgennemsnit, E=Årsultimo, B=Beregnet, Y=Årlig stigningstakt]
- tid: date range 1970-01-01 to 2024-01-01
dim docs: /dim/valuta_iso.md

notes:
- opgoer is a required filter: A=annual average, E=year-end closing rate, B=calculated, Y=annual growth rate. Omitting it gives multiple rows per (valuta, kurtyp, year).
- kurtyp is a measurement selector. For annual spot rates: kurtyp='KBH' (54 currencies). Also includes full set of competitiveness indices: INX, REK, RET (real effective rates), EFB (contributions), and underlying price/wage indices (DKI, Z9I, EUI, LOI, LOU).
- This is the broadest table — it combines spot rates (like dnvalm) and competitiveness indices (like dnvalq) in annual form.
- Values for KBH are DKK per 100 units of foreign currency. Divide by 100 for per-unit rate.
- Same valuta join limitation as dnvalm/dnvald: 22 historical currencies present but not in dim.valuta_iso.
- X00 and Z60 appear in EFB series; not in dim.valuta_iso.