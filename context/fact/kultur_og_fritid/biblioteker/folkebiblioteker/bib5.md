table: fact.bib5
description: Folkebibliotekernes interurbanind- og udlån fordelt efter område, opgørelse, materialetype og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- opgoer1: values [150=I ALT, INTERURBANINDLÅN , 151=Interurbanindlån fra danske folkebiblioteker, 152=Interurbanindlån fra danske forskningsbiblioteker, 153=Interurbanindlån fra udenlandske biblioteker, 154=I ALT, INTERURBANUDLÅN, 155=Interurbanudlån til danske folkebiblioteker, 156=Interurbanudlån til danske skolebiblioteker, 157=Interurbanudlån til danske forskningsbiblioteker, 158=Interurbanudlån til udenlandske biblioteker, 159=Interurbanudlån til folkebiblioteker i CB-området, 160=I ALT, INTERURBANUDLÅNSFORNYELSER, 161=Interurbanudlånsfornyelser til danske folkebiblioteker, 162=Interurbanudlånsfornyelser til danske skolebiblioteker, 163=Interurbanudlånsfornyelser til danske forskningsbiblioteker, 164=Interurbanudlånsfornyelser til udenlandske biblioteker, 165=Interurbanudlånsfornyelser til folkebiblioteker i CB-området]
- mater: values [500=Alle materialetyper, 560=I ALT, MONOGRAFIER, 503=Bøger, 506=Noder (trykte), 509=Kartografiske materiale (trykt) ... 548=Andet lyd (digital), 551=Genstande, 554=Sammensat materiale, 557=Andre materialer, 563=Seriepublikationer]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (97 kommuner). omrade=0 = Hele landet.
- opgoer1 contains 3 aggregate totals (150=I ALT INTERURBANINDLÅN, 154=I ALT INTERURBANUDLÅN, 160=I ALT INTERURBANUDLÅNSFORNYELSER) and their subtypes. Don't sum opgoer1 — pick either the total or individual subtypes.
- mater contains the same material type hierarchy as bib3: 500=Alle materialetyper (total), 560=I ALT MONOGRAFIER (subtotal). Filter to one level.
- Interurbanlending = interlibrary loans between library systems. These are library-to-library transfers, not loans to end users.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
