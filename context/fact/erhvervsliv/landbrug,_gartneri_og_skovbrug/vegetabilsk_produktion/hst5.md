table: fact.hst5
description: Prognose for vinterafgrøder til høst efter afgrøde, enhed og tid
measure: indhold (unit 1.000 ha)
columns:
- afgrode: values [H102=Samlet vintersæds areal, H110=Vinterhvede, H130=Rug, H140=Triticale, H150=Vinterbyg, H210=Vinterraps]
- enhed: values [3A=Prognose, 4A=Høstet areal]
- tid: date range 2000-01-01 to 2025-01-01

notes:
- enhed distinguishes forecast from actual: 3A=Prognose (forecast), 4A=Høstet areal (realised). Both appear for the same afgrode/tid. Filter to 4A for actual harvest area or 3A for the forecast.
- H102=Samlet vintersæds areal is an aggregate of H110+H130+H140+H150+H210. Don't sum H102 with the specific crops.
- National-level only. No regional breakdown.
- The unit in the table header is 1.000 ha (indhold is already in thousands of hectares).