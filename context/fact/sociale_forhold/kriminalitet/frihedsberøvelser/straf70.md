table: fact.straf70
description: Anholdelser efter køn, overtrædelsens art, afslutningsmåde, alder og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx: OVERTRÆD is object type with AVA suffixes (e.g. 3AVA, 111AVA) while overtraedtype.KODE is int64. Semantic match but requires stripping AVA suffix and converting to int.]; levels [1, 2, 3]
- afslut: values [B00=I alt, B10=Løsladt fra anholdelse, B11=Overgået til varetægtsfængsling, B12=Overgået til afsoning]
- alder: values [TOT=Alder i alt, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70OV=70 år og derover]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- All 5 dimensions have total rows: kon='TOT', overtraed='TOT', afslut='B00', alder='TOT'. Filter all non-target dimensions to their total to get a simple arrest count — forgetting any one silently multiplies the result.
- overtraed joins dim.overtraedtype via `f.overtraed::text = d.kode::text`. The fact table contains codes at niveau 1, 2, and 3 simultaneously, so always filter `WHERE d.niveau = X` to pick one level. Querying without a niveau filter double- or triple-counts.
- The 29% unmatched overtraed codes are expected aggregates, not data errors: 'TOT' (grand total), AVA-suffix codes like '13AVA'/'111AVA' (subtotals for DST-specific sub-groups with no single dim kode), 8-digit range codes like '12101220' (two concatenated niveau-3 kodes representing a merged group), and codes like '38102'/'38105'. Exclude these by joining to the dim — unmatched rows drop out automatically.
- afslut: B00=I alt, B10=Løsladt, B11=Varetægtsfængsling, B12=Afsoning. Filter to B00 for totals or pick one category for breakdown.
- alder: individual years 15–24 plus 5 age-group bands (25-29, 30-39, …, 70+) plus TOT. Groups and individual years are not mutually exclusive — do not sum across both.
- Sample query — arrests by offense category (niveau 1):
  SELECT d.titel, SUM(f.indhold)
  FROM fact.straf70 f
  JOIN dim.overtraedtype d ON f.overtraed::text = d.kode::text AND d.niveau = 1
  WHERE f.kon = 'TOT' AND f.afslut = 'B00' AND f.alder = 'TOT'
  GROUP BY d.titel;