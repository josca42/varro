table: fact.scene08a
description: Statsstøttede teatres økonomi efter teaterkategori, enhed og tid
measure: indhold (unit -)
columns:
- teattyp: values [100=Teatre i alt, 115=Det Kgl. Teater, 120=Teatre i Det Københavnske Teatersamarbejde, 122=Landsdelscener, nationale turnéteatre mv., 130=Små storbyteatre, 135=Egnsteatre, 140=Teatre støttet af Statens Kunstfond]
- enhed: values [1=Indtægter i alt (1.000 kr.), 2=Statslige tilskud (1.000 kr.), 3=Kommunale tilskud (1.000 kr.), 4=Egne indtægter (1.000 kr.), 40=Resultat, overskud (2021/2022-) (antal teatre), 45=Resultat, underskud (2021/2022-) (antal teatre)]
- tid: date range 2015/2016 to 2023/2024

notes:
- enhed is a critical measurement selector mixing incompatible units: enhed 1–4 are financial figures in 1.000 kr. (indtægter, statslige tilskud, kommunale tilskud, egne indtægter); enhed 40 and 45 are counts of theatres (antal). Never sum across enhed values.
- enhed 40 (overskud) and 45 (underskud) are only available from 2021/2022 onwards, despite the table going back to 2015/2016.
- teattyp here is narrower than other scene tables: only 100,115,120,122,130,135,140 — no 142 (refusions-/formidlingsordning) or 144 (øvrige). teattyp 100=alle teatre is the aggregate.
- This is the only table with financial/økonomi data. Longer series than other scene tables (from 2015/2016).