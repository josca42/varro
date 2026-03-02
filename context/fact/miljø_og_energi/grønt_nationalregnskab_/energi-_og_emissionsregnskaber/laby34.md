table: fact.laby34
description: Nøgletalstabel for udledning af drivhusgasser efter kommunegruppe, indikator, emissionstype, enhed og tid
measure: indhold (unit -)
columns:
- komgrp: values [000=Hele landet, LAND_EKSKL_IKFOR=Hele landet, ekskl. ikke fordelt til kommuner, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner, IKFOR=Ikke fordelt til kommuner]
- indikator: values [GHGHUSH_IKTR=Husholdningernes udledning af drivhusgasser (energirelateret) ekskl. fra individuel transport, GHGHUSH_TR=Husholdningernes udledning af drivhusgasser fra individuel transport, GHGBEF=Udledning af drivhusgasser (knyttet til bruttoenergiforbrug) fra brancher og husholdninger]
- emtype8: values [GHGEXBIO=Drivhusgasser i alt, ekskl. CO2 fra afbrænding af biomasse, GHGBIO=Drivhusgasser i alt, inkl. CO2 fra afbrænding af biomasse]
- enhed: values [TON_CO2=Ton CO2-ækvivalenter, KG_CO2=Kg CO2-ækvivalenter pr. indbygger]
- tid: date range 2020-01-01 to 2022-01-01

notes:
- enhed is a unit selector — TON_CO2 (absolute) vs. KG_CO2 (per inhabitant). Always filter to one enhed; values are not comparable across units.
- emtype8 has two values (GHGEXBIO excl. biomass CO2, GHGBIO incl. biomass CO2). These are not additive — filter to one.
- indikator values are not additive (household energy-related, household transport, all sectors+households). Filter to the indicator of interest.
- Short series (2020–2022), kommunegruppe-level only (5 groups + national totals). For longer GHG series by sector, use drivhus.