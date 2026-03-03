table: fact.indkf11a
description: Antal familier i indkomststatistikken efter område, familietype og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- famtyp: values [FAIA=Familier i alt, FAUB=Familier uden børn, FAMB=Familier med børn, PAIA=Par i alt, PAUB=Par uden børn, PAMB=Par med børn, ENIA=Enlige i alt, ENUB=Enlige uden børn, ENMB=Enlige med børn, EKIA=Enlige kvinder i alt, EKUB=Enlige kvinder uden børn, EKMB=Enlige kvinder med børn, EMIA=Enlige mænd i alt, EMUB=Enlige mænd uden børn, EMMB=Enlige mænd med børn]
- tid: date range 1987-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at all three levels (1=5 regioner, 2=landsdele, 3=kommuner). Filter WHERE d.niveau=... when joining.
- omrade='0' is national aggregate, not in dim.nuts.
- indhold = Antal (count of families). No enhed selector — simpler than most family tables.
- famtyp totals: FAIA=familier i alt. Includes gender-specific singles (EKIA=enlige kvinder, EMIA=enlige mænd).
- Goes back to 1987. Longest family count series with full geographic detail.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
