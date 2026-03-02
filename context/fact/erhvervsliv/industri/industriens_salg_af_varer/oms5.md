table: fact.oms5
description: Industriens salg (kvartal) efter branche (DB07), omsætningstype, sæsonkorrigering og tid
measure: indhold (unit 1.000 kr.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- omstype: values [SAMLET=SAMLET OMSÆTNING, EGVARE=SALG AF EGNE VARER I ALT, EGVARET1=Salg af egenproducerede varer, EGVARET2=Salg af varer produceret af underleverandør, RABTIL=Fakturerede rabatter og tillæg, ikke fordelt på varekoder, TJENIALT=INDUSTRIELLE TJENESTEYDELSER I ALT, OPSTIL=Opstillingsarbejde for andre, REP=Reparationsarbejde for andre, LOEN=Lønarbejde for andre, HANDEL=Salg af handelsvarer, ANDEN=Anden omsætning]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2000-01-01 to 2024-10-01
dim docs: /dim/db.md

notes:
- branche07 uses a custom survey classification — NOT joinable to dim.db (only 5 of 48 codes coincidentally match). The classification mixes NACE letter codes for aggregates (B, BC, C, CA, CB, CC, CDE, CF, CG, CH, CI, CJ, CK, CL, CM) and 5-digit numeric codes for sub-industries (10001=Slagterier, 10002=Fiskeindustri, etc.). Use ColumnValues("oms5", "branche07") to browse all 48 codes with labels.
- omstype has a hierarchical structure — do NOT sum across values. SAMLET is the grand total. EGVARE=salg af egne varer (= EGVARET1 + EGVARET2 + RABTIL). TJENIALT=industrielle tjenesteydelser (= OPSTIL + REP + LOEN). To get total turnover: filter omstype='SAMLET'. To break down: pick one level of the hierarchy (e.g., EGVARE + TJENIALT + HANDEL + ANDEN). Mixing levels inflates totals.
- saeson is a measurement selector: EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret. Every branche07×omstype×tid combination appears twice. Always filter to one value.
- With 3 non-time dimensions (branche07, omstype, saeson), a typical query needs to filter all three: e.g., WHERE branche07='C' AND omstype='SAMLET' AND saeson='EJSÆSON'.