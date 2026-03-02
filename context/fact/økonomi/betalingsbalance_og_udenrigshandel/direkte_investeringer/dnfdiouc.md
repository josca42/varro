table: fact.dnfdiouc
description: Danske direkte investeringer I udlandet efter land, instrument, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- land: join dim.lande_uht_bb on land=kode [approx]; levels [1, 2, 4]
- instrnat: values [2.0=2.0: Direkte investeringer (I alt), 2.1=2.1: Egenkapital, 2.2=2.2: Koncernlån mv.]
- data: values [F=Transaktioner, S=Beholdninger (ultimo året), I=Formueindkomst]
- tid: date range 2004-01-01 to 2024-01-01
dim docs: /dim/lande_uht_bb.md

notes:
- data is a required selector: F=Transaktioner, S=Beholdninger (beholdning ultimo året), I=Formueindkomst. All three values repeat for every land+instrnat combination — always filter to one, or you triple-count.
- instrnat is also a selector: 2.0=total, 2.1=egenkapital, 2.2=koncernlån. Always filter to one (usually 2.0 for total).
- land joins dim.lande_uht_bb at niveaux 1, 2, and 4 (no niveau 3 underregion codes). Use ColumnValues("lande_uht_bb", "titel", for_table="dnfdiouc") to see the ~43 matched codes.
- Three land codes do not exist in dim.lande_uht_bb: W1 (world total/"Verden"), I9 and R12 (custom BoP aggregate groupings). Exclude these when working at individual-country level, or use them knowingly as aggregates.
- To query individual countries: JOIN dim.lande_uht_bb d ON f.land = d.kode WHERE d.niveau = 4. For continental aggregates: niveau = 1 (A1, E1, F1, O1, S1). For EU-level: niveau = 2 (B6 = EU-27).
- Sample query — Danish outward FDI stocks by continent for 2024: SELECT d.titel, f.indhold FROM fact.dnfdiouc f JOIN dim.lande_uht_bb d ON f.land = d.kode WHERE f.data='S' AND f.instrnat='2.0' AND f.tid='2024-01-01' AND d.niveau=1;