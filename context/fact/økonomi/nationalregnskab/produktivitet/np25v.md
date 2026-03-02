table: fact.np25v
description: Vækstregnskab efter branche, type, prisenhed og tid
measure: indhold (unit Pct.)
columns:
- branche: join dim.nr_branche on branche=kode [approx]
- type: values [BVT=Bruttoværditilvækst, V_IT=It-kapital, V_AK=Anden kapital, V_LQ=Uddannelsesniveau, V_LM=Arbejdskraftmængde, V_TF=Totalfaktorproduktivitet, V_LP=Arbejdsproduktivitet, V_T=Arbejdstimer]
- prisenhed: values [VPR_V=Årlig vækstrate i pct., VPR_G=Årlig vækstrate i pct., rullende 5-års gennemsnit]
- tid: date range 1967-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- branche uses V-prefixed codes that do NOT directly match dim.nr_branche. Correct join: JOIN dim.nr_branche d ON d.kode = REPLACE(SUBSTRING(f.branche, 2), '_', '-'). Handles letter codes, combined codes (VD_E→D-E etc.), and numeric codes.
- branche niveaux 1–4 are all present simultaneously. Filter WHERE d.niveau = N to pick one level.
- Three productivity-specific aggregate codes outside dim.nr_branche: PBY, PMIALT, PTJEN (same as np25).
- prisenhed is a measurement selector — always filter to one: VPR_V (annual growth rate) or VPR_G (rolling 5-year avg).
- type is a growth accounting decomposition. BVT is the total (gross value added growth); the others are additive contributions that roughly sum to BVT: V_IT + V_AK + V_LQ + V_LM + V_TF ≈ BVT. Do NOT sum across types unless intentionally building the decomposition. To get total GVA growth, filter type='BVT'. For the productivity residual (TFP contribution), use type='V_TF'.
- This table differs from np25 in that np25 decomposes labour productivity growth, while np25v decomposes total GVA growth (growth accounting framework). Use np25v when the question is about sources of GVA growth including the labour quantity channel (V_LM, V_T).