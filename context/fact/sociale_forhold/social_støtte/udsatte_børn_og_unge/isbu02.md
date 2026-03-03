table: fact.isbu02
description: Børn og unge der modtager indsatser og støtte efter kommune, indsats og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- indsatser: values [2=BØRN OG UNGE DER MODTAGER FOREBYGGENDE FORANSTALTNINGER OG INDSATSER I ALT, 5=TIDLIGT FOREBYGGENDE INDSATSER EFTER LOV OM SOCIAL SERVICE / BARNETS LOV, 405=Konsulentbistand, herunder familierettede indsatser (SEL §11.3.1 / BL §30.1.1), 401=Netværks- eller samtalegrupper (SEL §11.3.2 / BL §30.1.2), 402=Rådgivning om familieplanlægning (SEL §11.3.3 / BL §30.1.3) ... 268=Aflastningsophold for barnet eller den unge (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.6), 269=Fast kontaktperson for den unge alene (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.7), 499=Kontaktperson for hele familien (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.7. Til 2023), 277=Formidling af praktiktilbud til unge (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.8), 278=Anden hjælp, der har til formål at yde rådgivning, behandling og støtte (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.9)]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Counts CHILDREN (unique children receiving support), not interventions. Use this when the question is "how many children" not "how many interventions". See isbu01 for intervention counts.
- indsatser has the same 55 hierarchical codes as isbu01, but the total code differs: 2=BØRN OG UNGE DER MODTAGER FOREBYGGENDE FORANSTALTNINGER OG INDSATSER I ALT (vs code 3 in isbu01). Same hierarchy rules apply — do not sum parent + child codes.
- kommunedk joins dim.nuts at niveau 3 (98 kommuner). Code 0 = national total.
- For total children with support per kommune: WHERE indsatser=2 AND tid='2024-01-01'.
- Map: /geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.