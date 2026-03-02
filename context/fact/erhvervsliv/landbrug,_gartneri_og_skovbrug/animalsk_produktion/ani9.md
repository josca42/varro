table: fact.ani9
description: Slagtninger og eksport efter kategori, enhed og tid
measure: indhold (unit 1.000 stk.)
columns:
- dyrkat: values [D1=Heste, KVAEGIALT=Kvæg, i alt, VKVAEG=Voksent kvæg i alt, TYRE=Tyre, UNGTYRE=Ungtyre ... KYL=Kyllinger, HAENS=Høns, AAND=Ænder, GAES1=Gæs, KALKUN1=Kalkuner]
- tal: values [SLAGEKS=Slagtninger og eksport af levende dyr (1.000 stk.), SLASLA=Slagtninger på slagterier i Danmark (1.000 stk.), EKSLEV=Eksport af levende dyr (1.000 stk.)]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- `tal` (not `enhed`) is the measurement selector: SLAGEKS (total = SLASLA + EKSLEV), SLASLA (domestic slaughter at abattoirs), EKSLEV (live animal exports). Always filter to one tal. Unit is always 1.000 stk. — no weight, price, or value data available.
- `dyrkat` covers all major animal types in one table — best for cross-species comparisons. Aggregate codes: KVAEGIALT (all cattle), SVINIALT (all pigs), FJERTOTAL (all poultry), FLTOTAL (farm livestock total excl. poultry). Sub-categories are present within each species group and overlap with their aggregate.
- Never sum all dyrkat values — pick either the aggregate (KVAEGIALT) or the sub-categories (VKVAEG + KALVE), not both.
- Annual data (2005-2024), count only. For slaughter weight, price, and value data or longer series, use the species-specific tables (ani4/ani41 for kvæg, ani5/ani51 for svin, ani6/ani61 for fjerkræ).