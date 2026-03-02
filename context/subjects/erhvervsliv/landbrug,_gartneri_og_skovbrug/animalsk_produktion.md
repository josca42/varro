<fact tables>
<table>
id: ani11
description: Samlede værdier og indeks for animalske landbrugsprodukter (kvartal) efter indekstype og tid
columns: indekstype, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2025-04-01
</table>
<table>
id: ani2
description: Samlede værdier og indeks for animalske landbrugsprodukter (år) efter indekstype og tid
columns: indekstype, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: ani4
description: Slagtninger og produktion af kvæg efter kategori, enhed og tid
columns: dyrkat, enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: ani41
description: Slagtninger og produktion af kvæg efter kategori, enhed og tid
columns: dyrkat, enhed, tid (time), indhold (unit -)
tid range: 1995-01-01 to 2025-08-01
</table>
<table>
id: ani5
description: Slagtninger og produktion af svin efter kategori, enhed og tid
columns: dyrkat, enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: ani51
description: Slagtninger og produktion af svin efter kategori, enhed og tid
columns: dyrkat, enhed, tid (time), indhold (unit -)
tid range: 1995-01-01 to 2025-08-01
</table>
<table>
id: ani6
description: Slagtninger og produktion af fjerkræ efter kategori, enhed og tid
columns: dyrkat, enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: ani61
description: Slagtninger og produktion af fjerkræ efter kategori, enhed og tid
columns: dyrkat, enhed, tid (time), indhold (unit -)
tid range: 1995-01-01 to 2025-04-01
</table>
<table>
id: ani9
description: Slagtninger og eksport efter kategori, enhed og tid
columns: dyrkat, tal, tid (time), indhold (unit 1.000 stk.)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: ani7
description: Mælkeproduktion og anvendelse efter enhed og tid
columns: enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: ani71
description: Mælkeproduktion og anvendelse efter enhed og tid
columns: maengde4, tid (time), indhold (unit -)
tid range: 1995-01-01 to 2025-08-01
</table>
<table>
id: ani8
description: Ægproduktion og produktionsformer efter enhed og tid
columns: enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: ani81
description: Ægproduktion og produktionsformer efter enhed og tid
columns: enhed, tid (time), indhold (unit -)
tid range: 1995-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- **Table naming**: tables ending in no suffix (ani4, ani5, ani6, ani7, ani8, ani9) are annual; tables ending in "1" (ani41, ani51, ani61, ani71, ani81) are the monthly/quarterly counterpart of the same data. ani11 is the exception — it's the quarterly index table. Pick the suffix based on time granularity needed.
- **Cattle slaughter**: ani4 (annual, 1990-2024) / ani41 (monthly, 1995-2025). Both have count, weight, price, and value via the `enhed` selector. Hierarchy in `dyrkat`: KVAEGIALT > VOKSKVAEGIALT + KALVEIALT > individual animal types.
- **Pig slaughter**: ani5 (annual, 1990-2024) / ani51 (monthly, 1995-2025). `dyrkat` mixes animal-type categories and slaughter-location categories — not a clean hierarchy. SVINIALT is the correct total; never sum sub-categories to get it.
- **Poultry slaughter**: ani6 (annual, 1990-2024) / ani61 (quarterly, 1995-2025). FJERKREKS = total incl. live exports; FJERKRIALT = slaughter only. Species sub-categories available (KYLLING dominates).
- **Cross-species comparison**: use ani9 (annual, 2005-2024) for slaughter counts across all animal types in one query. Count only — no weight or price data. `tal` column splits into SLAGEKS (total) = SLASLA (domestic) + EKSLEV (live exports).
- **Milk production**: ani7 (annual, 1990-2024, 27 measures) / ani71 (monthly, 1995-2025, 15 measures). The monthly table uses column name `maengde4` instead of `enhed`. Use for milk volumes, dairy product output, prices, and fat/protein content.
- **Egg production**: ani8 (annual, 1990-2024) / ani81 (monthly/quarterly, 1995-2025). `enhed` classifies eggs by both husbandry method (BUR/FRIT/SKRAB/OKOAEG) and destination (KON1/KON2/KON3/RUG) — these are alternative views, not additive.
- **Value/price indices**: ani2 (annual, 1995-2024) / ani11 (quarterly, 2015-2025) cover aggregate animal product values and indices across all product types. `indekstype` is a measurement selector — filter to one series. Multiple base years available in ani2; use 2015-base (indekstype 15/25) for current comparisons.
- **Universal gotcha**: every table in this subject has a measurement selector column (`enhed`, `indekstype`, `maengde4`, or `tal`) where each value is a different metric. Always filter to exactly one selector value — failing to do so inflates or scrambles results.