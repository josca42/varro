table: fact.formue12
description: Formue efter formuetype, enhed, område, alder, population og tid
measure: indhold (unit -)
columns:
- form1: values [FGNF2020=Nettoformue I alt (2020-definition A+B+CX-D-E-F), FGNF2014=Nettoformue I alt (2014-definition A+B-B6+CX-D-E-F+F3), FGAK2020=Aktiver I alt (2020-definition A+B+CX), FGAK2014=Aktiver I alt (2014-definition A+B+CX-B6), FGA=A. Reale aktiver i alt ... FGF2014=F. Gæld til det offentlige (2014-definition ekskl. F3), FGF1=F.1. Studielån, FGF2=F.2. Gæld til kommuner, FGF3=F.3. Gæld til inddrivelse (mangler fra 2017-2019), FGF4=F.4. Øvrig gæld til det offentlige]
- enhed: values [200=Median, faste priser (seneste dataårs prisniveau), 205=Nedre kvartil, faste priser (seneste dataårs prisniveau), 210=Øvre kvartil, faste priser (seneste dataårs prisniveau), 215=Gennemsnit, faste priser (seneste dataårs prisniveau), 220=Median (nominelle priser), 225=Nedre kvartil (nominelle priser), 230=Øvre kvartil (nominelle priser), 235=Gennemsnit (nominelle priser), 240=Personer i befolkningen d. 31.12 (antal)]
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- alder: values [1802=18 år og derover, 1829=18-29 år, 3049=30-49 år, 5069=50-69 år, 7099=70 år og derover]
- popu: values [5005=Alle uanset om de har formuetypen, 5025=Kun personer med formuetypen]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Two levels present: niveau=1 (5 regioner, kode 81-85) and niveau=3 (99 kommuner). omrade=0 is the national aggregate — not in dim. Use ColumnValues("nuts", "titel", for_table="formue12") to see the 103 matchable codes.
- Same three mandatory selectors as all formue tables: form1 (pick one wealth type), enhed (pick one unit), popu (5005=alle or 5025=kun med). Omitting any of these multiplies row counts.
- alder here is coarser than formue11: only 5 broad groups (1802=total, 1829, 3049, 5069, 7099). Cannot do 5-year age bands with this table.
- enhed=240 is antal personer (count), not a kr. value — don't mix with the financial enhed values.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
