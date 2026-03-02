table: fact.ani8
description: Ægproduktion og produktionsformer efter enhed og tid
measure: indhold (unit -)
columns:
- enhed: values [BUR=Buræg (mio kg), FRIT=Frilandsæg (mio kg), SKRAB=Skrabeæg (mio. kg), OKOAEG=Økologiske æg (mio. kg), KON1=Konsumæg salg til pakkerier (mio kg), KON2=Konsumæg direkte salg og eget forbrug (mio. kg), KON3=Konsumægsproduktion i alt (mio. kg), KON4=Konsumægsværdi i alt ab producent (mio. kr), SALG1=Salgspris konsumæg gnsntl. ab producent (øre pr. kg), SALG2=Salgspris skrabeæg ab producent (øre pr. kg), SALG3=Salgspris økologiske æg ab producent (øre pr. kg), RUG=Rugeæg (mio. kg)]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- enhed is a measurement selector — never sum across enhed values. Units differ completely: mio. kg for egg volumes, mio. kr for value (KON4), øre pr. kg for prices (SALG1–SALG3).
- Production system types (BUR, FRIT, SKRAB, OKOAEG) do not sum to KON3 total. In 2024: BUR+FRIT+SKRAB+OKOAEG=77 mio. kg but KON3=89 mio. kg. Use KON3 for total konsumægsproduktion; do not derive it by summing the system types.
- KON1+KON2 = KON3 (salg til pakkerier + direkte salg + eget forbrug = total). These three are internally consistent.
- SALG1/SALG2/SALG3 are average prices (øre pr. kg), not volumes — do not sum or aggregate across years without weighting.
- For organic eggs: OKOAEG = production volume (mio. kg), SALG3 = average farm-gate price.