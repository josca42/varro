table: fact.fouoff06
description: FoU-årsværk udført af personale på højere læreanstalter under universitetsloven efter institution, stillingskategori og tid
measure: indhold (unit Årsværk)
columns:
- insti: values [7000=Københavns Universitet, 7100=Aarhus Universitet, 7200=Syddansk Universitet, 7300=Roskilde Universitet (RUC), 7400=Aalborg Universitet, 7500=Danmarks Tekniske Universitet, 7600=CBS (Handelshøjskolen i København), 7700=IT-Universitetet]
- stilkat: values [310=Professor, 320=Lektor/ Docent, 330=Øvrige VIP, 340=Adjunkt/ Post. Doc., 350=Ph.d- og Kandidat-, 360=Schollar- ship, 370=TAP]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- Covers only universities under universitetsloven (8 institutions: KU, AU, SDU, RUC, AAU, DTU, CBS, ITU). No total institution row — sum all insti codes for the combined figure.
- stilkat has 7 position categories (310–370), no total code — sum all for the combined FoU årsværk.
- This is the most granular university-level breakdown; for aggregate sector totals use fouoff01/fouoff02.
