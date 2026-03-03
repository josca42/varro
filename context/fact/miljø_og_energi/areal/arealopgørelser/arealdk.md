table: fact.arealdk
description: Areal efter arealdække, område, enhed og tid
measure: indhold (unit -)
columns:
- are1: values [TOT=I alt, A=Veje, jernbaner og landingsbaner, A1=Veje, befæstede, A15=Veje, ubefæstede, A2=Jernbaner ... F2=Enge, moser og anden våd natur, G=Søer og vandløb, G1=Søer, G2=Vandløb, H=Ikke klassificeret]
- omrade: values [LAND=Hele landet, inkl. ikke-matrikuleret areal, IKMAK=Ikke fordelt på kommune (ikke matrikulerede arealer på land), 000=Hele landet, 084=Region Hovedstaden, 101=København ... 773=Morsø, 840=Rebild, 787=Thisted, 820=Vesthimmerlands, 851=Aalborg]
- enhed: values [120=Kvadratkilometer (km2), 130=Kvadratmeter (m2) pr. indbygger, 140=Procent]
- tid: date range 2011-01-01 to 2021-01-01

notes:
- enhed is a measurement selector (120=km2, 130=m2 pr. indbygger, 140=%). The table repeats every combination for all three units — always filter to one enhed, e.g. WHERE enhed = '120'. Forgetting this triples all counts.
- are1 has a two-level hierarchy: single-letter codes (A, B, C, D, E, F, G, H) are category totals, letter+number codes (A1, A15, A2, B1, B2, etc.) are sub-categories. TOT is the grand total. Summing both parent and child codes double-counts. Filter to one level, e.g. WHERE LENGTH(are1) = 1 for top-level only.
- omrade uses inline codes — does NOT join to dim.nuts. Special codes: LAND=Hele landet inkl. ikke-matrikuleret areal, IKMAK=Ikke fordelt på kommune. Geographic codes use zero-padded strings: 000=Hele landet, 081–085=regioner, 101+=kommuner. Note: regions use 3-digit zero-padded format (084) unlike dim.nuts kode (84).
- No dimension table joins needed. All column values are inline.
- Map: /geo/kommuner.parquet — filter omrade codes 101+, merge on CAST(omrade AS INT)=dim_kode. Or /geo/regioner.parquet — filter omrade IN ('081','082','083','084','085'), merge on CAST(omrade AS INT)=dim_kode (strips leading zero). Exclude LAND and IKMAK.