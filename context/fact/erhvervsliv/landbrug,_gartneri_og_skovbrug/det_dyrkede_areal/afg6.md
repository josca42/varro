table: fact.afg6
description: Afgrøder efter afgrøde, enhed, areal og tid
measure: indhold (unit -)
columns:
- afgrode: values [0=Landbrug og gartneri i alt, 5=1. Korn til modenhed, 10=1.1 Hvede, 15=1.1.1 Vinterhvede, 20=1.1.2 Vårhvede ... 280=A 1. Areal som er blevet vandet det seneste år, 285=B. Areal med reduceret jordbearbejdning, 290=B 1 Areal dyrket uden pløjning, 295=B 2 Areal dyrket uden bearbejdning af hele jordoverfladen, 300=C. Skov på landbrugbedrifter]
- enhed: values [ANTAL=Bedrifter (antal), HA=Hektar]
- areal1: values [AIALT=I alt, A1=Under 10,0 ha, A19=10,0 - 19,9 ha, A29=20,0 - 29,9 ha, A49=30,0 - 49,9 ha, A62=50,0 - 74,9 ha, A100=75,0 - 99,9 ha, A210=100,0 - 199,9 ha, A220=200,0 ha og derover]
- tid: date range 1982-01-01 to 2024-01-01

notes:
- afgrode is a hierarchical crop classification with 61 codes. The hierarchy is encoded in the text label: "1. Korn til modenhed" (level 1), "1.1 Hvede" (level 2), "1.1.1 Vinterhvede" (level 3). afgrode=0 = grand total (Landbrug og gartneri i alt). Summing across all afgrode overcounts massively — pick one specific code or one hierarchy level.
- Codes 275–300 (A, B, C series: areal som kan vandes, reduceret jordbearbejdning, skov på bedrifter) are cross-cutting overlapping measures that do NOT roll up into the main hierarchy. Never add them to other crop totals.
- enhed is a measurement selector: ANTAL=Bedrifter, HA=Hektar. Every afgrode × areal1 row appears twice. Always filter: WHERE enhed='HA' or WHERE enhed='ANTAL'.
- areal1 is the farm size class: AIALT=I alt (totals across farm sizes), A1=Under 10 ha, A19=10–19.9 ha, up to A220=200+ ha. Filter to areal1='AIALT' for national crop totals.
- All 3 non-time columns must be filtered for a clean result. Example — total grain area in 2024: SELECT indhold FROM fact.afg6 WHERE tid='2024-01-01' AND afgrode=5 AND enhed='HA' AND areal1='AIALT'.