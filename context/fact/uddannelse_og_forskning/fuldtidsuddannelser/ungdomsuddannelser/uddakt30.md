table: fact.uddakt30
description: Uddannelsesaktivitet på gymnasiale uddannelser efter uddannelse, bopælsregion, herkomst, national oprindelse, køn, status og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [TOT=I alt, H20=H20 Gymnasiale uddannelser, H2010=H2010 Alment gymnasiale uddannelser, H201010=H201010 Stx, H201020=H201020 Hf ... H351010=H351010 Gymnasial supplering, H3520=H3520 Adgangseksamen - ingeniøruddannelse, H352010=H352010 Adgangseksamen - ingeniøruddannelse, H3530=H3530 Adgangsgivende værkstedsskoleforløb, H353010=H353010 Adgangsgivende værkstedsskoleforløb]
- bopreg: join dim.nuts on bopreg=kode [approx: Values 0 and 999 in fact not in dimension]; levels [1]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- fstatus separates three distinct measurement types: B=Elever pr. 1. oktober (stock/enrollment), F=Fuldført (completions), T=Tilgang (new intake). These are independent measures — always filter to exactly one fstatus. Summing across them is meaningless.
- uddannelse is hierarchical with 3 levels encoded by code length: 3 chars (e.g. H20, H35) = overordnet gruppe, 5 chars (e.g. H2010) = mellemgruppe, 7 chars (e.g. H201010=Stx) = specifik uddannelse. TOT spans all. Filter to one level to avoid double-counting. For a single program (e.g. Stx), use the 7-char code.
- bopreg joins dim.nuts but only niveau=1 (5 regioner: 81-85). bopreg=0 is the national total (I alt), bopreg=999 is uoplyst bopælsregion (students with unknown/foreign address). Both are outside dim.nuts. For a regional breakdown, filter WHERE bopreg IN (81,82,83,84,85) or join and get 5 rows.
- herkomst and herkomst1 are complementary origin dimensions. herkomst = origin type (5=dansk, 4=indvandrer, 3=efterkommer, 0=uoplyst), herkomst1 = geographic origin country group. Both have TOT totals. For a plain count, set both to TOT.
- To get enrollment by region: WHERE fstatus='B' AND uddannelse='H20' AND herkomst='TOT' AND herkomst1='TOT' AND kon='10' AND bopreg IN (81,82,83,84,85). All five filters needed to avoid overcounting.
- Map: /geo/regioner.parquet (niveau 1) — merge on bopreg=dim_kode. Exclude bopreg IN (0, 999).