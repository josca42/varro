table: fact.formue13
description: Formue efter formuetype, enhed, socioøkonomisk status, population og tid
measure: indhold (unit -)
columns:
- form1: values [FGNF2020=Nettoformue I alt (2020-definition A+B+CX-D-E-F), FGNF2014=Nettoformue I alt (2014-definition A+B-B6+CX-D-E-F+F3), FGAK2020=Aktiver I alt (2020-definition A+B+CX), FGAK2014=Aktiver I alt (2014-definition A+B+CX-B6), FGA=A. Reale aktiver i alt ... FGF2014=F. Gæld til det offentlige (2014-definition ekskl. F3), FGF1=F.1. Studielån, FGF2=F.2. Gæld til kommuner, FGF3=F.3. Gæld til inddrivelse (mangler fra 2017-2019), FGF4=F.4. Øvrig gæld til det offentlige]
- enhed: values [200=Median, faste priser (seneste dataårs prisniveau), 205=Nedre kvartil, faste priser (seneste dataårs prisniveau), 210=Øvre kvartil, faste priser (seneste dataårs prisniveau), 215=Gennemsnit, faste priser (seneste dataårs prisniveau), 220=Median (nominelle priser), 225=Nedre kvartil (nominelle priser), 230=Øvre kvartil (nominelle priser), 235=Gennemsnit (nominelle priser), 240=Personer i befolkningen d. 31.12 (antal)]
- socio: join dim.socio on socio=kode [approx]; levels [3]
- popu: values [5005=Alle uanset om de har formuetypen, 5025=Kun personer med formuetypen]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/socio.md

notes:
- socio has 19 distinct codes but only 16 match dim.socio (all at niveau=3). Three extra aggregate codes exist only in this table: 100="Alle", 115="Selvstændige med ansatte", 130="Lønmodtagere i alt". Do not rely on a plain JOIN to dim.socio — use ColumnValues("formue13", "socio") to see all 19 labels, or use inline filtering without a join.
- Same three mandatory selectors: form1 (pick one wealth type), enhed (pick one unit), popu (5005=alle or 5025=kun med).
- enhed=240 is antal personer (count), not a kr. value.
