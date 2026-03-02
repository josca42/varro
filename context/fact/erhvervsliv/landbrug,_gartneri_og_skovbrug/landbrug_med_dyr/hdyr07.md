table: fact.hdyr07
description: Landbrug med dyr efter område, enhed, art og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- enhed: values [ANTAL=Bedrifter (antal), DYR=Dyr (antal)]
- dyr: values [D1=Heste, D2=Tyre- og studekalve, - under 1/2 år, D3=Tyre- og studekalve, 1/2-1 år, D39=Tyre- og studekalve i alt, D4=Tyre og stude, 1-2 år ... D35=Høns i alt, D36=Kalkuner, D362=Ænder, D364=Gæs, D366=Fjerkræ i alt]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- enhed is a measurement selector (ANTAL=bedrifter/farms, DYR=dyr/animals). Every dyr×omrade combination is repeated for both enhed values. Always filter enhed to one value or results are doubled.
- dyr has 144 values mixing two distinct coding schemes: D-prefix codes are specific animal categories (D1=Heste, D14=Malkekøer, D366=Fjerkræ i alt, etc.); letter-prefix codes are herd size groups per animal type (MK=malkekøer, AK=ammekøer, KK=alle køer, K=kvæg, SO=søer, SS=slagtesvin, S=svin, F=får, MF=moderfår). Never sum across different prefix families. Use "i alt" codes (D366, KIALT, SOIALT, etc.) for totals within a type. Use ColumnValues("hdyr07", "dyr") to find the right code.
- omrade has 12 values but only 10 join to dim.nuts: 5 regioner (81-85, niveau 1) and 5 landsdele (4,7,8,9,10, niveau 2). Code 0=Hele landet and code 15="Landsdelene Byen København, Københavns omegn og Nordsjælland" (a merged aggregate of what dim.nuts has as 3 separate landsdele: 1, 2, 3) are not in dim.nuts. Filter omrade='0' for national total; omrade='15' for the merged Copenhagen-area landsdel.
- To query by region: JOIN dim.nuts d ON f.omrade=d.kode AND d.niveau=1 (gives 5 regioner). For landsdele: d.niveau=2 (gives 5 landsdele, excluding the merged code 15 area).
- Typical query: filter enhed, dyr, optionally omrade+tid. Example: number of farms with malkekøer by region = WHERE enhed='ANTAL' AND dyr='MK50' (alle bedrifter med malkekøer) joined to dim.nuts niveau=1.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade IN (0, 15).