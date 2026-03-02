table: fact.dnmnogl
description: Nøgletal for MFI-sektoren efter nøgletal, sektor og tid
measure: indhold (unit -)
columns:
- aktp: values [CR5MFIMFIEXDN=Koncentrationsindeks CR5 (ekskl. Nationalbanken) (indeks), HERFINMFIMFIEXDN=Koncentrationsindeks Herfindahl-indeks (ekskl. Nationalbanken) (indeks), M1MFI=Pengemængdemål M1 (mio. kr.), SDLMTMFI=- Seddel- og møntomløb (mio. kr.), INDLANMFI=- Indlån på anfordring (mio. kr.), M2MFI=Pengemængdemål M2 (mio. kr.), INDTIDMFI=- Indlån på tidsindskud med oprindelig løbetid op til og med 2 år (mio. kr.), INDOPSMFI=- Indlån med opsigelsesvarsel med oprindelig løbetid op til og med 3 mdr. (mio. kr.), M3MFI=Pengemængdemål M3 (mio. kr.), INDREPOMFI=- Repoindlån (mio. kr.), UDSTGAELDMFI=- Udstedte gældsinstrumenter med oprindelig løbetid op til og med 2 år og pengemarkedspapirer (mio. kr.), M1SKMFI=Sæsonkorrigeret M1 (mio. kr.), SDLMTSKMFI=- heraf sæsonkorrigeret seddel- og møntomløb (mio. kr.), M2SKMFI=Sæsonkorrigeret M2 (mio. kr.), AL00MFIEXDN=Udlån (ekskl. Nationalbanken) (mio. kr.), AL00SKMFIEXDN=Sæsonkorrigeret udlån (ekskl. Nationalbanken) (mio. kr.)]
- sektornat: join dim.esr_sekt on sektornat=kode [approx]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/esr_sekt.md

notes:
- aktp encodes many heterogeneous metrics with different units — concentration indices (CR5, Herfindahl: index values), money supply components (M1/M2/M3 and sub-components: mio. kr.), outstanding loans (AL00: mio. kr.), seasonally adjusted variants. Never sum or compare across aktp values.
- Money supply hierarchy within aktp: M3 > M2 > M1. Sub-components (SDLMT, INDLAN, INDREPOMFI, UDTSGAELD, INDOPSMFI, INDTID) are sub-parts of the respective aggregate. Don't add components to their parent.
- sektornat uses compound sector+country codes (1000A1=alle sektorer worldwide, 1100DK=indenlandske ikke-fin. selskaber, 1400DK=indenlandske husholdninger). These do NOT join to dim.esr_sekt (0% match); treat as inline values.
- The dim link to dim.esr_sekt in this doc is incorrect.