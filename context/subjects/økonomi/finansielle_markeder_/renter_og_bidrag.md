<fact tables>
<table>
id: dnindex
description: Reference rente compounded index - dagsobservationer efter instrument, opgørelsesmetode og tid
columns: instrument, opgoer, tid (time), indhold (unit Indeks)
tid range: 2022-04-01 to 2025-10-30
</table>
<table>
id: dnrentd
description: Rentesatser og aktieindeks (dagsobservationer) efter instrument, land, opgørelsesmetode og tid
columns: instrument, land, opgoer, tid (time), indhold (unit Pct.)
tid range: 1983-05-10 to 2025-10-30
</table>
<table>
id: dnrentm
description: Rentesatser og aktieindeks (månedsobservationer) efter instrument, land, opgørelsesmetode og tid
columns: instrument, land, opgoer, tid (time), indhold (unit -)
tid range: 1985-10-01 to 2025-09-01
</table>
<table>
id: dnrenta
description: Rentesatser og aktieindeks (årsobservationer) efter instrument, land, opgørelsesmetode og tid
columns: instrument, land, opgoer, tid (time), indhold (unit Pct.)
tid range: 1985-01-01 to 2024-01-01
</table>
<table>
id: mpk3
description: Rentesatser, ultimo (pct p.a.) efter type og tid
columns: type, tid (time), indhold (unit Pct. pro anno)
tid range: 1985-01-01 to 2025-09-01
</table>
<table>
id: mpk18
description: Gennemsnitsrenter i pengeinstitutterne (pct. p.a.) efter sektor, ud-/indlån og tid
columns: sektor, udindlan, tid (time), indhold (unit Pct. pro anno)
tid range: 2002-01-01 to 2025-04-01
</table>
<table>
id: mpk100
description: Effektiv rente af statsobligationer efter land og tid
columns: land, tid (time), indhold (unit Pct. pro anno)
tid range: 1989-01-01 to 2024-01-01
</table>
<table>
id: dnruum
description: Udestående indenlandsk udlån fra MFI-sektoren ekskl. Nationalbanken efter instrument, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid), formål og tid
columns: instrnat, data, indsek, valuta, lobetid1, formal, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnruuri
description: Udestående indenlandsk udlån fra realkreditinstitutter efter datatype, indenlandsk sektor, valuta og tid
columns: data, indsek, valuta, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnruipi
description: Udestående indenlandsk indlån i pengeinstitutter efter instrument, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid) og tid
columns: instrnat, data, indsek, valuta, lobetid1, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnruim
description: Udestående indenlandsk indlån i MFI-sektoren ekskl. Nationalbanken efter datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid) og tid
columns: data, indsek, valuta, lobetid1, tid (time), indhold (unit -)
tid range: 2013-06-01 to 2025-09-01
</table>
<table>
id: dnrnum
description: Nye indenlandske udlån ekskl. kassekreditter o.l. fra MFI-sektoren ekskl. Nationalbanken efter formål, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid), rentefiksering, lånstørrelse og tid
columns: formal, data, indsek, valuta, lobetid1, rentfix1, laanstr, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnrnupi
description: Nye indenlandske udlån ekskl. kassekreditter o.l. fra pengeinstitutter efter formål, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid), oprindelig rentefiksering, lånstørrelse og repoforretninger og tid
columns: formal, data, indsek, valuta, lobetid1, rentfix, laanstrrepo, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnrnuri
description: Nye indenlandske udlån fra realkreditinstitutter efter datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid), oprindelig rentefiksering, lånstørrelse og tid
columns: data, indsek, valuta, lobetid1, rentfix, laanstr, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnrnim
description: Nye indenlandske indlån i MFI-sektoren ekskl. Nationalbanken efter instrument, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid) og tid
columns: instrnat, data, indsek, valuta, lobetid1, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnrnipi
description: Nye indenlandske indlån i pengeinstitutter efter instrument, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid) og tid
columns: instrnat, data, indsek, valuta, lobetid1, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnrupppi
description: Pengeinstitutternes udestående indenlandske forretninger fordelt på 10 pct. percentiler efter instrument, indenlandsk sektor og tid
columns: instrnat, indsek, tid (time), indhold (unit Pct.)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnrurpi
description: Pengeinstitutternes udestående indenlandske forretninger - Rentemarginaler efter instituttype, datatype, indenlandsk sektor, valuta og tid
columns: institype, data, indsek, valuta, tid (time), indhold (unit Pct.)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnrugpi
description: Pengeinstitutternes nye og udestående indenlandske forretninger - Gruppeinddelt efter instrument, instituttype, indenlandsk sektor, valuta, formål og tid
columns: instrnat, institype, indsek, valuta, formal, tid (time), indhold (unit Pct.)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: dnriurq
description: Realkreditinstitutternes udestående indenl. realkreditudlån - Kvartalsvis ydelse efter datatype, indenlandsk sektor, valuta og tid
columns: data, indsek, valuta, tid (time), indhold (unit Pct.)
tid range: 2013-10-01 to 2025-07-01
</table>
</fact tables>
notes:
- Time granularity is encoded in table suffixes: d=dagsobservationer (daily), m=månedsobservationer (monthly), a=årsobservationer (annual), q=kvartalsvis (quarterly). The dn-prefix tables (dnrentd/m/a) share the same instruments at different frequencies. Pick the frequency matching your analysis.
- For Nationalbanken's benchmark rates (diskonto, folio, udlån, indskudsbeviser): use dnrentd (daily back to 1983), dnrentm (monthly from 1985), or dnrenta (annual from 1985). All three have opgoer as a measurement selector — always filter it.
- For government bond effective yields across countries: use mpk100 (annual, 1989-, 3-digit country codes). For Denmark only: use dnrenta/dnrentm with obligationsrente instruments.
- For DESTR reference rate (since 2022): use dnrentd with instrument='DESNAA'. For the predecessor preDESTR rate (2017-2022): use instrument='PDRNAA'. For the compounded index: use dnindex (daily from 2022-04-01).
- For bank lending/deposit rates and volumes, there are three institution layers: MFI-sector (excl. Nationalbanken) = dnruum (loans) / dnruim (deposits); pengeinstitutter only = dnruipi (deposits outstanding) / dnrnupi (new loans) / dnrnipi (new deposits); realkreditinstitutter only = dnruuri (loans outstanding) / dnrnuri (new loans).
- For new vs. outstanding: "ru" in table name = udestående (outstanding balances); "rn" = nye (new transactions in the period). Outstanding tables show stock; new tables show flow.
- mpk18 gives average rates in pengeinstitutterne by sector (2002-). Its sektor column uses codes without dots (S11, S14 etc.) — do NOT join to dim.esa.
- mpk3 gives selected benchmark rates (ultimo) back to 1985, simpler than the dn-series but covers fewer instruments.
- Critical gotcha shared by most tables: the data column (or instrnat in some tables) is a measurement selector mixing rates (pct) with volumes (mio. kr.). Always filter to one value before aggregating or comparing.
- indsek hierarchy appears in all MFI tables: 1000=total (where present), 1100/1200/1300/1400/1500=top-level sectors, 1410/1430/12CC=sub-sectors. Never sum a total code with its constituent codes.
- valuta Z01 (Alle valutaer) is an aggregate present in most tables but NOT in dim.valuta_iso — treat it as an inline code meaning "all currencies". DKK and EUR are subsets of Z01; don't sum them together.
