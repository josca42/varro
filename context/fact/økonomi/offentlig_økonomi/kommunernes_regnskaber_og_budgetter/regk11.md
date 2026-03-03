table: fact.regk11
description: Kommunernes regnskaber på hovedkonti efter område, hovedkonto, dranst, art, prisenhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- funk1: values [X=I alt hovedkonto 0-8, 0=0 Byudvikling, bolig- og miljøforanstaltninger, 1=1 Forsyningsvirksomheder m.v., 2=2 Transport og infrastruktur, 3=3 Undervisning og kultur, 4=4 Sundhedsområdet, 5=5 Sociale opgaver og beskæftigelse, 6=6 Fællesudgifter og administration, 7=7 Renter, tilskud, udligning og skatter, 8=8 Balanceforskydninger]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 5=5 Finansforskydninger, 6=6 Afdrag på lån, 7=7 Finansiering]
- art: values [TOT=I alt (netto), UE=Bruttoudgifter, I=Indtægter, S0=0 Beregnede omkostninger, S1=1 Lønninger ... 89=8.9 Øvrige finansindtægter, 91=9.1 Overførte lønninger, 92=9.2 Overførte varekøb, 94=9.4 Overførte tjenesteydelser, 97=9.7 Interne indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts on omrade=kode. niveau=1 gives 5 regioner, niveau=3 gives kommuner. Extra codes not in dim.nuts: 0 (Hele landet), 910 (Hovedstadskommuner), 920 (Storbykommuner), 930 (Provinsbykommuner), 940 (Oplandskommuner), 960 (Landkommuner). These municipality-type groupings are useful for urban/rural comparisons — query them directly without joining dim.nuts.
- prisenhed is a measurement selector that exactly doubles all rows: LOBM=løbende priser (1.000 kr.), INDL=pr. indbygger løbende priser (kr.). Always filter to one — omitting silently doubles any sum.
- funk1='X' is the aggregate of funk1 values 0–7 (verified). Do not sum funk1='X' with individual funk1 codes.
- art includes aggregates: TOT=netto (= UE minus I), UE=bruttoudgifter, I=indtægter, then S0–S9 subtotals and 00–97 detail codes. Use art='TOT' for net expenditure. Do not sum TOT with UE or I.
- dranst has no aggregate code — each value (1=drift, 2=statsrefusion, 3=anlæg, 4=renter, 5=finansforskydninger, 6=afdrag, 7=finansiering) is a separate category. Sum across dranst values to combine.
- Minimal correct query — driftsudgifter (netto) by region 2023: SELECT d.titel, SUM(f.indhold) FROM fact.regk11 f JOIN dim.nuts d ON f.omrade=d.kode AND d.niveau=1 WHERE f.funk1='X' AND f.dranst='1' AND f.art='TOT' AND f.prisenhed='LOBM' AND f.tid='2023-01-01' GROUP BY d.titel;
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
