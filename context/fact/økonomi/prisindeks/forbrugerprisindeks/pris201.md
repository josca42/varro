table: fact.pris201
description: Husstandsopdelte forbrugerprisindeks efter varegruppe, husstandsgrupper, enhed og tid
measure: indhold (unit -)
columns:
- varegr: join dim.ecoicop_dst on varegr=kode [approx]
- husgrp: values [2010=Enlige under 60 år uden børn, 2020=Enlig 60 år og over uden børn, 2030=Enlige med børn, 2040=2 voksne, hovedperson under 60 år uden børn, 2050=2 voksne, hovedperson 60 år og over uden børn, 2060=2 voksne med børn, 2070=Husstande med mindst 3 voksne, 3010=Selvstændig, 3020=Lønmodtager på højeste niveau, 3030=Lønmodtager på mellemniveau, 3040=Lønmodtager på grundniveau, 3050=Arbejdsløs, 3060=Uddannelsessøgende, 3070=Pensionist,efterlønmodtager, 3080=Ude af erhverv i øvrigt, 4015=Under 250.000 kr., 4025=250.000 - 449.999 kr., 4035=450.000 - 699.999 kr., 4045=700.000 - 999.999 kr., 4055=1.000.000 kr. og derover]
- tal: values [100=Indeks, 200=Ændring i forhold til måneden før (pct.), 300=Ændring i forhold til samme måned året før (pct.)]
- tid: date range 2006-01-01 to 2025-08-01
dim docs: /dim/ecoicop_dst.md

notes:
- **Two measurement selectors** — tal (100=Indeks, 200=månedlig ændring pct., 300=årsændring pct.) and husgrp (21 household groups) are both selectors. Every varegr×tid combination appears 21×3 = 63×. Always filter to exactly one tal AND one husgrp.
- husgrp has three grouping schemes encoded in the same column: 2010–2070 = husholdningstype (family composition), 3010–3080 = socioøkonomisk gruppe, 4015–4055 = indkomstkvintil. These schemes overlap — a household can appear in all three. Do NOT sum across husgrp unless restricted to one scheme at a time.
- varegr uses the same 5-or-6 digit ECOICOP coding as pris111, but only covers niveau 1–2 (53 codes total). 100% join to dim.ecoicop_dst using the modulo join pattern (see pris111 notes). varegr=0 = total for all groups.
  ```sql
  JOIN dim.ecoicop_dst d ON d.kode = (f.varegr / POWER(10,
    CASE WHEN f.varegr % 10000 = 0 THEN 4 WHEN f.varegr % 1000 = 0 THEN 3
         WHEN f.varegr % 100  = 0 THEN 2 WHEN f.varegr % 10   = 0 THEN 1 ELSE 0 END)::int)
    AND d.niveau = (5 - CASE WHEN f.varegr % 10000 = 0 THEN 4 WHEN f.varegr % 1000 = 0 THEN 3
         WHEN f.varegr % 100  = 0 THEN 2 WHEN f.varegr % 10   = 0 THEN 1 ELSE 0 END)
  ```
- Use ColumnValues("pris201", "varegr") to browse the 53 ECOICOP codes; ColumnValues("pris201", "husgrp") for household group labels.