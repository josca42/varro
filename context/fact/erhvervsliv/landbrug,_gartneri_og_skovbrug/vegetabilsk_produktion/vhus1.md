table: fact.vhus1
description: Væksthuse efter område, strukturforhold og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- struk: values [1010=Antal bedrifter, 1011=Antal bedrifter med væksthuse mellem 0-9 år, 1012=Antal bedrifter med væksthuse mellem 10-19 år, 1013=Antal bedrifter med væksthuse over 20 år, 1015=Væksthusareal i alt (1000 m2) ... 1120=Teknik med rulleborde (1000 m2), 1125=Teknik med faste borde (1000 m2), 1130=Teknik med mobile borde (1000 m2), 1135=Vanding med recirkulering (1000 m2), 1140=Vanding uden recirkulering (1000 m2)]
- tid: date range 1993-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. INNER JOIN gives 10 labeled geographies: niveau=1 (5 regioner: 81-85) and niveau=2 (5 landsdele: 4=Bornholm, 7=Fyn, 8=Sydjylland, 9=Østjylland, 10=Vestjylland). omrade=0 = Hele landet (not in dim.nuts), omrade=15 = unmapped aggregate.
- struk codes (1010–1140) represent entirely different structural statistics — number of farms, greenhouse area by age of greenhouse, heating systems, irrigation methods. These are not sub-categories of one total. Each struk code is its own distinct metric. Only compare or aggregate struk codes if they are the same type of measure (e.g. summing area codes).
- struk=1015 (Væksthusareal i alt) is the top-level area measure. Codes 1016-1025 are area by crop type, 1030-1045 are area by heating type, 1050-1065 by construction type, etc. Don't mix categories.
- No enhed/measurement selector — unit varies by struk code (bedrifter, 1000 m2, etc.).
- Map: /geo/landsdele.parquet (niveau 2) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.