table: fact.oeko3
description: Detailomsætningen af økologiske fødevarer efter varer, enhed og tid
measure: indhold (unit -)
columns:
- vare: values [5000=OMSÆTNING I ALT, 5010=RIS, BRØD, PASTA, MEL, GRYN, KAGER I ALT, 5011=Ris, 5015=Rugbrød, 5017=Hvedebrød ... 5195=JUICE, FRUGTSAFT,  I ALT, 5198=VIN, HEDVIN, CIDER OG SPIRITUS I ALT, 5210=Vin, hedvin og cider (2016 - ), 5215=Spiritus (2016 - ), 5200=ØL I ALT]
- maengde4: values [10=Mængde i tons, 20=Værdi i 1000 kr.]
- tid: date range 2003-01-01 to 2024-01-01

notes:
- maengde4 is a unit selector: 10=Mængde i tons, 20=Værdi i 1000 kr. Always filter to one unit — forgetting this doubles every row.
- vare has a two-level hierarchy. 5000 is the grand total (OMSÆTNING I ALT). Uppercase labels are category subtotals (5010=RIS/BRØD/..., 5030=KØD/PÅLÆG/..., 5050=FISK, 5070=MÆLK/OST/ÆG, 5095=FEDTSTOFFER, 5105=FRUGT, 5130=GRØNTSAGER, 5155=SUKKER/CHOKOLADE/..., 5175=KRYDDERIER, 5190=KAFFE/TE, 5195=JUICE, 5198=VIN/HEDVIN/CIDER/SPIRITUS, 5200=ØL). Lowercase labels are individual items nested within those categories. Never sum across multiple hierarchy levels.
- 76 distinct vare codes. Use ColumnValues("oeko3", "vare") to browse all labels. Uppercase in the label = category subtotal.
- For total organic retail trade: vare='5000', maengde4=20 (value in 1000 kr.) or maengde4=10 (tons).
- Some vare codes have fewer time points (e.g. 5050=FISK only has 19 years vs 22 for most). Some product lines were added later (VIN, SPIRITUS only from 2016).