table: fact.isbu01
description: Aktive indsatser og støtte til børn og unge i året efter kommune, indsats og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- indsatser: values [3=INDSATSER OG STØTTE I ALT, 5=TIDLIGT FOREBYGGENDE INDSATSER EFTER LOV OM SOCIAL SERVICE / BARNETS LOV, 405=Konsulentbistand, herunder familierettede indsatser (SEL §11.3.1 / BL §30.1.1), 401=Netværks- eller samtalegrupper (SEL §11.3.2 / BL §30.1.2), 402=Rådgivning om familieplanlægning (SEL §11.3.3 / BL §30.1.3) ... 268=Aflastningsophold for barnet eller den unge (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.6), 269=Fast kontaktperson for den unge alene (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.7), 499=Kontaktperson for hele familien (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.7. Til 2023), 277=Formidling af praktiktilbud til unge (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.8), 278=Anden hjælp, der har til formål at yde rådgivning, behandling og støtte (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.9)]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Counts INTERVENTIONS (indsatser), not children — one child can have multiple active interventions. Compare with isbu02 which counts CHILDREN receiving support.
- indsatser has 55 hierarchical codes. Top-level totals: 3=I alt, 5=Tidligt forebyggende (SEL/BL), 6=SEL/BL indsatser og støtte, 7=Ungdomskriminalitetsloven. Specific intervention types (codes 210+, 400+) are children of 5, 6, or 7. Summing parent + child codes double-counts — pick either a parent total OR specific subtypes.
- kommunedk joins dim.nuts at niveau 3 (98 kommuner). Code 0 = national total.
- Use ColumnValues("nuts", "titel", for_table="isbu01") to see available kommuner.
- For total active interventions per kommune: WHERE indsatser=3 AND tid='2024-01-01'.
- Map: /geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.