table: fact.sha1
description: Udgifter til sundhed efter funktion, aktør, finansieringskilde, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- funktion: join dim.icha on funktion=kode [approx]
- aktoer: join dim.icha_hp on aktoer=kode [approx]
- finanskilde1: values [HFTOT=Finansiering i alt, HF1=1. Offentlige sundhedsordninger og obligatoriske sundhedsforsikringsordninger, HF11=1.1 Offentlige sundhedsordninger, HF2=2. Frivillige sundhedsforsikringssordninger, HF21=2.1 Frivillige sundhedsforsikringsordninger, HF22=2.2 Non profit institutioner rettet mod husholdninger (NPISH), HF3=3. Husholdningernes egenbetaling, HF4=4. Resten af verden]
- prisenhed: values [ENH1=Løbende priser]
- tid: date range 2010-01-01 to 2024-01-01
dim docs: /dim/icha.md, /dim/icha_hp.md

notes:
- funktion joins dim.icha but the fact table drops dots: HC.1.3 → HC13. Use REPLACE(d.kode, '.', '') = f.funktion in the join. Example: JOIN dim.icha d ON f.funktion = REPLACE(d.kode, '.', '').
- 12/39 funktion codes have no dim match: HCTOT (grand total across all functions), HC10, HC100 (unspecified treatment sub-categories), HC300–305 (nursing/personal care sub-codes), HC511–513 (pharmaceuticals sub-codes). These are real data rows but will be dropped by a dim join — include them as 'Uspecificeret' or query without joining if completeness matters.
- aktoer joins dim.icha_hp with the same dot-drop pattern: f.aktoer = REPLACE(d.kode, '.', ''). 31/32 codes match; only HPTOT (grand total) is unmatched.
- Both dims are 3-level hierarchies (niveau 1–3). The fact table contains codes at all three levels — joining without filtering niveau causes double/triple counting. For a clean breakdown, filter to one niveau: WHERE d.niveau = 1 for 8 funktion categories or 9 aktoer categories.
- finanskilde1 has its own 2-level hierarchy in the column itself (HFTOT > HF1 ≥ HF11, HF2 > HF21+HF22, HF3, HF4). Summing all finanskilde1 values drastically overcounts. Filter to HFTOT for total, or pick one consistent level (e.g. HF1/HF2/HF3/HF4 for the top-level breakdown).
- prisenhed has only one value: ENH1 (Løbende priser). Still include it in WHERE to be safe but it doesn't affect aggregation.
- For a correct total expenditure query: filter funktion='HCTOT', aktoer='HPTOT', finanskilde1='HFTOT', prisenhed='ENH1' — then break out one dimension at a time using the dim join with niveau filter.
- Example — expenditure by provider type (2024): JOIN dim.icha_hp hp ON f.aktoer = REPLACE(hp.kode, '.', '') AND hp.niveau = 1, then WHERE f.funktion='HCTOT' AND f.finanskilde1='HFTOT' AND f.prisenhed='ENH1'.