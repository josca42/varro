table: fact.arealdk
description: Areal efter arealdække, område, enhed og tid
measure: indhold (unit -)
columns:
- are1: values [TOT=I alt, A=Veje, jernbaner og landingsbaner, A1=Veje, befæstede, A15=Veje, ubefæstede, A2=Jernbaner ... F2=Enge, moser og anden våd natur, G=Søer og vandløb, G1=Søer, G2=Vandløb, H=Ikke klassificeret]
- omrade: values [LAND=Hele landet, inkl. ikke-matrikuleret areal, IKMAK=Ikke fordelt på kommune (ikke matrikulerede arealer på land), 000=Hele landet, 084=Region Hovedstaden, 101=København ... 773=Morsø, 840=Rebild, 787=Thisted, 820=Vesthimmerlands, 851=Aalborg]
- enhed: values [120=Kvadratkilometer (km2), 130=Kvadratmeter (m2) pr. indbygger, 140=Procent]
- tid: date range 2011-01-01 to 2021-01-01

notes:
- enhed is a measurement selector: all rows are repeated 3 times (km2, m2/person, pct). Always filter to one enhed — e.g. WHERE enhed='120' for km2. Forgetting this triples the sum.
- are1 has a true hierarchy: TOT > letter codes (A, B, C...) > alphanumeric subcodes (A1, A15, A2, A3...). Confirmed: A = A1+A15+A2+A3. Only pick one level — either TOT or letter groups or leaf codes, never mix.
- omrade has 106 values: 000=Hele landet, 081-085=5 regioner, 101-860=98 kommuner (3-digit codes), plus LAND=Hele landet inkl. ikke-matrikuleret areal and IKMAK=Ikke fordelt på kommune. No dim join — values are inline. Use 000 for national total (excludes non-cadastral). LAND > 000 by the non-cadastral margin.
- No dim table link; commune codes here use 3-digit scheme (e.g. 101, 147) matching the standard DST commune numbering.
- Map: context/geo/kommuner.parquet (omrade 101-860) or context/geo/regioner.parquet (omrade 081-085) — merge on omrade=dim_kode (cast omrade to int). Exclude omrade IN ('000', 'LAND', 'IKMAK').