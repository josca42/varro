table: fact.jord100
description: Regnskabsstatistik i 100 år efter bedriftstype, enhed, regnskabsposter og tid
measure: indhold (unit -)
columns:
- brugstype: values [5010=Alle landbrug (1916- ), 5015=Heltidslandbrug (1973- ), 5020=Heltidslandbrug med malkekvæg (1973- ), 5025=Heltidslandbrug med svin (1973- ), 5030=Heltidslandbrug med pelsdyr (1997- ), 5035=Heltidslandbrug med planteavl (1973- ), 5040=Deltidslandbrug (1973- )]
- tal: values [10=Pr. ha (kr.), 20=Pr. bedrift (1.000 kr.)]
- regnskposter: values [10=Areal, ha, 20=Landbrugsaktiver, primo, 30=Bruttoudbytte, 40=Driftsomkostninger, 45=Lejet arbejdskraft, 50=Ejeraflønning, 60=Nettoudbytte, 70=Afkastningsgrad, pct.]
- tid: date range 1916-01-01 to 2024-01-01
notes:
- tal is a measurement selector: 10=pr. ha (kr.), 20=pr. bedrift (1.000 kr.). Always filter to ONE tal — every (brugstype, regnskposter, tid) combination appears twice.
- brugstype labels include start years (e.g., "Heltidslandbrug (1973- )"). Subtypes only have data from their stated start year; querying earlier years returns no rows.
- regnskposter has just 7 items: areal, aktiver, bruttoudbytte, driftsomkostninger, lejet arbejdskraft, ejeraflønning, nettoudbytte, afkastningsgrad (pct.). Afkastningsgrad is a rate — do not sum with money items.
- Longest series in the subject: 1916–2024 for alle landbrug. Useful for century-scale trend questions.
