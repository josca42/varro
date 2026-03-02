table: fact.formue17
description: Formue efter formuetype, enhed, alder, familietype, population og tid
measure: indhold (unit -)
columns:
- form1: values [FGNF2020=Nettoformue I alt (2020-definition A+B+CX-D-E-F), FGNF2014=Nettoformue I alt (2014-definition A+B-B6+CX-D-E-F+F3), FGAK2020=Aktiver I alt (2020-definition A+B+CX), FGAK2014=Aktiver I alt (2014-definition A+B+CX-B6), FGA=A. Reale aktiver i alt ... FGF2014=F. Gæld til det offentlige (2014-definition ekskl. F3), FGF1=F.1. Studielån, FGF2=F.2. Gæld til kommuner, FGF3=F.3. Gæld til inddrivelse (mangler fra 2017-2019), FGF4=F.4. Øvrig gæld til det offentlige]
- enhed: values [200=Median, faste priser (seneste dataårs prisniveau), 205=Nedre kvartil, faste priser (seneste dataårs prisniveau), 210=Øvre kvartil, faste priser (seneste dataårs prisniveau), 215=Gennemsnit, faste priser (seneste dataårs prisniveau), 220=Median (nominelle priser), 225=Nedre kvartil (nominelle priser), 230=Øvre kvartil (nominelle priser), 235=Gennemsnit (nominelle priser), 245=Familier i befolkningen d. 31.12 (antal)]
- alder: values [1802=18 år og derover, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 9099=90 år og derover]
- famtyp: values [FAIA=Familier i alt, PAUB=Par uden børn, PAMB=Par med børn, ENUB=Enlige uden børn, ENMB=Enlige med børn]
- popu: values [5005=Alle uanset om de har formuetypen, 5025=Kun personer med formuetypen]
- tid: date range 2014-01-01 to 2023-01-01

notes:
- Same three mandatory selectors as formue11-14: form1 (pick one wealth type), enhed (pick one unit), popu (5005=alle or 5025=kun med). Filter famtyp to a single value too unless breaking out by family type.
- enhed=245 is antal familier (count), not a kr. value — different code than formue11's enhed=240 (which was antal personer).
- famtyp='FAIA' is the total across all family types. The four subtypes (PAUB, PAMB, ENUB, ENMB) are mutually exclusive and exhaustive.
- This table measures wealth per family unit (not per person). Comparable to formue11 but family-level rather than individual-level.
