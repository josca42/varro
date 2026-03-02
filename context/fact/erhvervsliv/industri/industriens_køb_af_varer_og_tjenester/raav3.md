table: fact.raav3
description: Industriens køb af tjenester efter varegruppe (6 cifre), branche (DB07), enhed og tid
measure: indhold (unit -)
columns:
- vargr6: values [993=I alt køb af tjenester, 1T=Produktionsrelaterede tjenester, 991001=991001 Produktudvikling, 991002=991002 Licensudgifter/royalties/typegodkendelser o.lign., 991003=991003 Teknisk assistance (inkl. montage) ... 998004=998004 Renovation, 998005=998005 Rengøring, 998006=998006 Porto, 998007=998007 Kontingenter, 999001=999001 Ikke-fordelte eksterne udgifter]
- branche07: join dim.nr_branche on branche07=kode [approx]; levels [1, 2, 3]
- enhed: values [V=Værdi (1000 kr.), P=Andel i pct. af omsætning]
- tid: date range 2002-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- enhed is a selector: V=Værdi (1.000 kr.), P=Andel i pct. af omsætning. Always filter to one.
- vargr6 hierarchy: 993=grand total (I alt køb af tjenester), codes with T suffix (1T–8T)=service category aggregates (1T=Produktionsrelaterede tjenester, 4T=Markedsomkostninger, etc.), 6-digit numeric codes=detail level. Filter to one level.
- Same branche07 structure as raav1/raav2: custom aggregates BC and CDE not in dim.nr_branche, and niveau duplication for B/C on join. See raav1 notes for join strategy.