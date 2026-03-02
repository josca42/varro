table: fact.formue11
description: Formue efter formuetype, enhed, alder, køn, population og tid
measure: indhold (unit -)
columns:
- form1: values [FGNF2020=Nettoformue I alt (2020-definition A+B+CX-D-E-F), FGNF2014=Nettoformue I alt (2014-definition A+B-B6+CX-D-E-F+F3), FGAK2020=Aktiver I alt (2020-definition A+B+CX), FGAK2014=Aktiver I alt (2014-definition A+B+CX-B6), FGA=A. Reale aktiver i alt ... FGF2014=F. Gæld til det offentlige (2014-definition ekskl. F3), FGF1=F.1. Studielån, FGF2=F.2. Gæld til kommuner, FGF3=F.3. Gæld til inddrivelse (mangler fra 2017-2019), FGF4=F.4. Øvrig gæld til det offentlige]
- enhed: values [200=Median, faste priser (seneste dataårs prisniveau), 205=Nedre kvartil, faste priser (seneste dataårs prisniveau), 210=Øvre kvartil, faste priser (seneste dataårs prisniveau), 215=Gennemsnit, faste priser (seneste dataårs prisniveau), 220=Median (nominelle priser), 225=Nedre kvartil (nominelle priser), 230=Øvre kvartil (nominelle priser), 235=Gennemsnit (nominelle priser), 240=Personer i befolkningen d. 31.12 (antal)]
- alder: values [1802=18 år og derover, 1824=18-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6569=65-69 år, 7074=70-74 år, 7579=75-79 år, 8084=80-84 år, 8589=85-89 år, 9099=90 år og derover]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- popu: values [5005=Alle uanset om de har formuetypen, 5025=Kun personer med formuetypen]
- tid: date range 2014-01-01 to 2023-01-01

notes:
- Three mandatory selector columns — always filter all three to get a single meaningful value:
  - form1: 46 codes in a deep hierarchy (totals, subtotals, line items). Summing across codes massively double-counts since parent totals and their children are both present. Key totals: FGNF2020=nettoformue (2020-def), FGNF2014=nettoformue (2014-def), FGAK2020=aktiver i alt. Use ColumnValues("formue11", "form1") to browse.
  - enhed: pick exactly one — 200=median faste priser, 215=gennemsnit faste priser, 220=median nominelle, 235=gennemsnit nominelle, or 240=antal personer. enhed=240 is a head count, not a wealth measure.
  - popu: 5005=alle (wealth=0 for those without the asset type), 5025=kun med formuetypen. Omitting silently doubles rows.
- kon='MOK' is the total; alder='1802' is all adults 18+. Filter these too unless breaking out.
- Minimal filter for a single median nettoformue figure: form1='FGNF2020', enhed=200, popu=5005, kon='MOK', alder='1802'.
- Has the finest age breakdown of all formue tables: 15 five-year age bands from 18-24 to 90+.