table: fact.ani8
description: Ægproduktion og produktionsformer efter enhed og tid
measure: indhold (unit -)
columns:
- enhed: values [BUR=Buræg (mio kg), FRIT=Frilandsæg (mio kg), SKRAB=Skrabeæg (mio. kg), OKOAEG=Økologiske æg (mio. kg), KON1=Konsumæg salg til pakkerier (mio kg), KON2=Konsumæg direkte salg og eget forbrug (mio. kg), KON3=Konsumægsproduktion i alt (mio. kg), KON4=Konsumægsværdi i alt ab producent (mio. kr), SALG1=Salgspris konsumæg gnsntl. ab producent (øre pr. kg), SALG2=Salgspris skrabeæg ab producent (øre pr. kg), SALG3=Salgspris økologiske æg ab producent (øre pr. kg), RUG=Rugeæg (mio. kg)]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- `enhed` is a measurement selector — always filter to exactly one value. The 12 values fall into three non-mixing groups:
  1. By husbandry method (mio.kg): BUR (caged), FRIT (free-range), SKRAB (barn), OKOAEG (organic). These classify eggs by production system.
  2. By destination (mio.kg or mio.kr): KON1 (sold to packing stations), KON2 (direct sale + own use), KON3=KON1+KON2 (total consumption eggs), KON4 (total value, mio.kr), RUG (hatching eggs).
  3. Prices (øre/kg): SALG1 (avg consumption egg price), SALG2 (skrabeæg price), SALG3 (organic egg price).
- The husbandry-method series and destination series are alternative classifications of the same eggs — BUR+FRIT+SKRAB+OKOAEG ≠ KON3 (the former may include hatching eggs and uses a different boundary). Never mix groups in a single query.
- Annual data (1990-2024). For monthly/quarterly data from 1995, use ani81.