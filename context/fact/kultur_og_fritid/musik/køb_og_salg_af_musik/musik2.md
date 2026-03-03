table: fact.musik2
description: Køb af rettigheder til afspilning af musik efter branche (DB07), område og tid
measure: indhold (unit Kr.)
columns:
- branche07: values [BD=Industri, byggeri og anlæg, A=A Landbrug, skovbrug og fiskeri, 4=4 Handel og transport mv., I=I Hoteller og restauranter, JA=JA Forlag, tv og radio, JB=JB Telekommunikation, JC=JC It- og informationstjenester, K=K Finansiering og forsikring, L=L Ejendomshandel og udlejning, 8=8 Erhvervsservice, O=O Offentlig administration, forsvar og politi, R=R Kultur og fritid, X=X Uoplyst aktivitet, Y=Vederlag fra udlandet]
- omrade: join dim.nuts on omrade=kode [approx]; levels [1]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau=1 (5 regioner: 81–85). Only 5 of 7 omrade codes join — omrade=99 and omrade=997 are not in dim.nuts.
- omrade=99 only appears with branche07='X' (Uoplyst aktivitet) and represents payments from unidentified/unlocatable sources. Small amounts.
- omrade=997 appears only with branche07='X' (Uoplyst) and 'Y' (Vederlag fra udlandet). The values are far larger than the sum of the 5 regions — it is NOT a national total of the regions but rather a separate non-regional aggregate (likely centrally-reported national blanket + foreign income).
- branche07='Y' (Vederlag fra udlandet) only appears under omrade=997 — it has no regional breakdown.
- For a clean regional breakdown by branche: filter omrade IN (81,82,83,84,85) and join dim.nuts. Omitting this filter inflates counts via 99 and 997.
- For total national income by branche, SUM all omrade values (81–85 + 99 + 997) but note this mixes regional and non-regional figures.
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Filter omrade IN (81,82,83,84,85) before merging; exclude 99 and 997.