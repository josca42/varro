table: fact.ani81
description: Ægproduktion og produktionsformer efter enhed og tid
measure: indhold (unit -)
columns:
- enhed: values [BUR=Buræg (mio kg), FRIT=Frilandsæg (mio kg), SKRAB=Skrabeæg (mio. kg), OKOAEG=Økologiske æg (mio. kg), KON1=Konsumæg salg til pakkerier (mio kg), KON2=Konsumæg direkte salg og eget forbrug (mio. kg), KON3=Konsumægsproduktion i alt (mio. kg), KON4=Konsumægsværdi i alt ab producent (mio. kr), SALG1=Salgspris konsumæg gnsntl. ab producent (øre pr. kg), SALG2=Salgspris skrabeæg ab producent (øre pr. kg), SALG3=Salgspris økologiske æg ab producent (øre pr. kg), RUG=Rugeæg (mio. kg)]
- tid: date range 1995-01-01 to 2025-04-01

notes:
- Same structure as ani8 (annual æg table) but monthly/quarterly frequency.
- `enhed` selector — same 12 values as ani8 in the same three groups: husbandry method (BUR, FRIT, SKRAB, OKOAEG), destination (KON1, KON2, KON3, KON4, RUG), prices (SALG1, SALG2, SALG3). The two volume group classifications (method vs destination) are not additive with each other.
- Monthly/quarterly data from 1995. For annual aggregates back to 1990, use ani8.