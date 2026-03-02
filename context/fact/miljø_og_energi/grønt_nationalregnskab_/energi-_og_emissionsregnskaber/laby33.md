table: fact.laby33
description: Nøgletalstabel for energiforbrug og -produktion efter kommunegruppe, indikator, enhed og tid
measure: indhold (unit -)
columns:
- komgrp: values [000=Hele landet, LAND_EKSKL_IKFOR=Hele landet, ekskl. ikke fordelt til kommuner, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner, IKFOR=Ikke fordelt til kommuner]
- indikator: values [ENEHUSH_IKTR=Husholdningernes energiforbrug ekskl. individuel transport, ENEHUSH_TR=Husholdningernes energiforbrug til individuel transport, ENEBEF=Bruttoenergiforbrug af brancher og husholdninger, ENEPROD=Produktion af primær energi]
- enhed: values [GJ=GJ (gigajoule), MJ_IND=MJ (megajoule) pr. indbygger, MJ_HEK=MJ (megajoule) pr. hektar]
- tid: date range 2020-01-01 to 2022-01-01

notes:
- enhed is a measurement-unit selector — each komgrp × indikator combination appears up to 3× (GJ, MJ/inhabitant, MJ/hectare). Always filter enhed to one value. Note: MJ_HEK (per hectare) is only available for kommunegrupper 1–5, not for 000/LAND_EKSKL_IKFOR.
- indikator values are not additive to each other (ENEHUSH_IKTR + ENEHUSH_TR ≈ household total; ENEBEF covers all sectors+households). Filter to the indicator you need.
- Very short time series (2020–2022). Only 5 kommunegruppe types (no individual municipality breakdown).
- For longer energy series or more detail, use ene3h or ene2ha.