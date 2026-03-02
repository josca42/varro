<fact tables>
<table>
id: dnvpdks
description: Værdipapirstatistik efter papirtype, kupon, valuta, løbetid, udstedersektor, investorsektor, værdiansættelse, datatype og tid
columns: papir, kupon, valuta, lobetid, udstedsektor, invsektor, vaerdian, data, tid (time), indhold (unit Mio. kr.)
tid range: 1999-12-01 to 2015-01-01
</table>
<table>
id: dnvpdku
description: Udbytter for VP-registrerede værdipapirer efter papirtype, udstedersektor og tid
columns: papir, udstedsektor, tid (time), indhold (unit Mio. kr.)
tid range: 1999-12-01 to 2025-09-01
</table>
<table>
id: dnvpdkf
description: Værdipapirstatistik (markedsværdi) efter ISIN_NAVN, investorsektor og tid
columns: isninavn, invsektor, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-09-01
</table>
<table>
id: dnvpdkbr
description: VP-registrerede papirer efter papirtype, valuta, udstederbranche, investorbranche, værdiansættelse, datatype og tid
columns: papir, valuta, udstedbranc, holbranc, vaerdian, data, tid (time), indhold (unit Mio. kr.)
tid range: 2008-11-01 to 2025-09-01
</table>
<table>
id: dnvpejer
description: Ejerkoncentration i realkreditobligationer efter ISIN og tid
columns: isin, tid (time), indhold (unit Koncentrationsmål)
tid range: 2005-01-01 to 2025-09-01
</table>
<table>
id: dnvpstrs
description: Strukturerede obligationer fordelt på forskellige karakteristika efter underliggende aktivtype, optionstyper, hovedstolsgaranti, løbetid (oprindelig løbetid), kupontype, værdiansættelse, datatype og tid
columns: uakt, opt, hoved1, lobetid1, kupon1, vaerdian, data, tid (time), indhold (unit Mio. kr.)
tid range: 1999-12-01 to 2025-08-01
</table>
<table>
id: dnvpstrh
description: Strukturerede obligationer fordelt på underliggende aktivtype og investorsektor efter underliggende aktivtype, investorsektor, værdiansættelse, datatype og tid
columns: uakt, invsektor, vaerdian, data, tid (time), indhold (unit Mio. kr.)
tid range: 1999-12-01 to 2025-08-01
</table>
<table>
id: dnvpu
description: Papirer udstedt i udlandet efter papirtype, kupon, valuta, løbetid, udstedersektor, udstedelsesland, værdiansættelse, datatype og tid
columns: papir, kupon, valuta, lobetid, udstedsektor, udstland, vaerdian, data, tid (time), indhold (unit Mio. kr.)
tid range: 2003-01-01 to 2025-09-01
</table>
<table>
id: mpk13
description: Aktieindeks ultimo efter type og tid
columns: type, tid (time), indhold (unit Indeks)
tid range: 1996-01-01 to 2025-09-01
</table>
<table>
id: dncfe
description: Klimarelaterede indikatorer for den finansielle sektors porteføljer efter investor, investering, udstedersektor, udstedelsesland, udledningskategori, værdier og tid
columns: investor, invest1, udstedsektor, udstland2, udlkat, vaerdi1, tid (time), indhold (unit -)
tid range: 2018-01-01 to 2025-04-01
</table>
<table>
id: dncfem
description: Klimarelaterede indikatorer for danske realkreditobligationer baseret på energimærker efter investor, investering, udledningskategori, værdier og tid
columns: investor, invest1, udlkat, vaerdi1, tid (time), indhold (unit -)
tid range: 2022-10-01 to 2025-04-01
</table>
<table>
id: dnshsrea
description: Danske realkreditobligationer holdt af eurolande (SHS) efter type af realkreditobligation, investorland, datatype og tid
columns: typreal, investland, datat, tid (time), indhold (unit Mio. kr.)
tid range: 2019-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- Sector codes: most VP tables (dnvpdks, dnvpdku, dnvpdkbr, dnvpstrh, dnvpu) use DST-internal numeric sector codes (0000, 1000, 1100, 1212, 122P, etc.) rather than ESA S.xxx notation. These codes do NOT join to dim.esa despite the annotation. Treat all sector columns as inline coded values using the descriptions in each fact doc.

- Measurement selectors (vaerdian, data): tables with both vaerdian (B/N) and data (1/2/3 or 8/4/9) multiply every row by up to 6. Always filter both. Default: vaerdian='B' (markedsværdi), data=1 or data=8 (beholdning). Note that dnvpstrs and dnvpstrh use data codes 8/4/9 while dnvpdks and dnvpu use 1/2/3.

- Table selection guide:
  - General securities holdings by sector: dnvpdks (historical to 2015, richer dimensions: kupon, lobetid, invsektor+udstedsektor) or dnvpdkbr (current from 2008, branch breakdown instead of sector)
  - Holdings by specific ISIN: dnvpdkf (10,661 ISINs, markedsværdi only, from 2005)
  - Dividends paid by sector: dnvpdku (aktier + beviser only, from 1999)
  - Foreign-issued bonds by Danish entities: dnvpu (obligationer only, from 2003)
  - Stock market indices: mpk13 (OMXC series + sector indices, from 1996) — indhold is an index value, never sum across types
  - Structured bonds by characteristics: dnvpstrs; by investor sector: dnvpstrh (both from 1999)
  - Ownership concentration in mortgage bonds: dnvpejer (per-ISIN concentration measure, not Mio. kr.)
  - Euro-area countries' holdings of Danish mortgage bonds: dnshsrea (from 2019, 5 investor countries)
  - Climate indicators for financial sector portfolios: dncfe (from 2018, stocks+corporate bonds); dncfem (from 2022, mortgage bonds only via energy labels)

- vaerdian='N' (nominel) gives face value; vaerdian='B' (markedsværdi) gives market value. For aktier, nominel is typically 0 (no par value). Use markedsværdi for most analysis.

- papir hierarchy appears in many tables: 10A/11A/20A/30A are totals; subtypes like 11N, 11U, 24A, 25A are components. Never sum a total row with its components.