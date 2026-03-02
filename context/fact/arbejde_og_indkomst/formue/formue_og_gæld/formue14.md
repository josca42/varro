table: fact.formue14
description: Formue efter formuetype, enhed, alder, herkomst, population og tid
measure: indhold (unit -)
columns:
- form1: values [FGNF2020=Nettoformue I alt (2020-definition A+B+CX-D-E-F), FGNF2014=Nettoformue I alt (2014-definition A+B-B6+CX-D-E-F+F3), FGAK2020=Aktiver I alt (2020-definition A+B+CX), FGAK2014=Aktiver I alt (2014-definition A+B+CX-B6), FGA=A. Reale aktiver i alt ... FGF2014=F. Gæld til det offentlige (2014-definition ekskl. F3), FGF1=F.1. Studielån, FGF2=F.2. Gæld til kommuner, FGF3=F.3. Gæld til inddrivelse (mangler fra 2017-2019), FGF4=F.4. Øvrig gæld til det offentlige]
- enhed: values [200=Median, faste priser (seneste dataårs prisniveau), 205=Nedre kvartil, faste priser (seneste dataårs prisniveau), 210=Øvre kvartil, faste priser (seneste dataårs prisniveau), 215=Gennemsnit, faste priser (seneste dataårs prisniveau), 220=Median (nominelle priser), 225=Nedre kvartil (nominelle priser), 230=Øvre kvartil (nominelle priser), 235=Gennemsnit (nominelle priser), 240=Personer i befolkningen d. 31.12 (antal)]
- alder: values [1802=18 år og derover, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5069=50-69 år, 7099=70 år og derover]
- herkomst: join dim.herkomst on herkomst=kode::text [approx]; levels [1]
- popu: values [5005=Alle uanset om de har formuetypen, 5025=Kun personer med formuetypen]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/herkomst.md

notes:
- herkomst does NOT match dim.herkomst (only 1 of 6 codes aligns). This table uses a finer west/non-west breakdown not in the standard dim. Use inline codes directly without a dim join: TOT=I alt, 1=dansk oprindelse, 24=indvandrere fra vestlige lande, 25=indvandrere fra ikke-vestlige lande, 34=efterkommere fra vestlige lande, 35=efterkommere fra ikke-vestlige lande. Verify with ColumnValues("formue14", "herkomst").
- Same three mandatory selectors: form1 (pick one wealth type), enhed (pick one unit), popu (5005=alle or 5025=kun med).
- enhed=240 is antal personer (count), not a kr. value.
