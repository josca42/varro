table: fact.jord9
description: Energiforbrug for heltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- brugstype: values [1=Landbrug, 2=Konventionelt landbrug, 3=Økologisk landbrug, 4=Gartneri, 538=Væksthusgartneri, 540=Prydplanter, 545=Prydplanter, mindre end 7.500 m2 væksthusareal, 550=Prydplanter, 7.500-14.999 m2 væksthusareal, 552=Prydplanter, mindre end 15.000 m2 væksthusareal (2020-), 555=Prydplanter, 15.000 m2 eller mere væksthusareal, 560=Væksthusgrøntsager, 563=Frilandsgartneri, 565=Frilandsgrøntsager, 570=Frugt og bær, 575=Planteskole]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [4500=ENERGIFORBRUG I ALT, GIGAJOULE, 4505=OPVARMNING AF VÆKSTHUSE I ALT (ENERGIFORBRUG), GIGAJOULE, 4510=Opvarmning af væksthuse med naturgas, gigajoule, 4515=Opvarmning af væksthuse med fjernvarme, gigajoule, 4520=Opvarmning af væksthuse med let olie, gigajoule ... 4620=Opvarmning af staldbygninger mv., 1000 kr., 4625=GRØNNE AFGIFTER, 1000 KR., 4630=Grønne afgifter, CO2 og NOx-afgift, 1000 kr., 4635=Grønne afgifter, SO2 afgift, 1000 kr., 4640=Grønne afgifter, energiafgift, 1000 kr.]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- CRITICAL: regnskposter availability differs by brugstype. brugstype 1/2/3 (Landbrug/Konventionelt/Økologisk) only have 11 regnskposter — agricultural energy items starting from 4545 (maskin- og redskabsdrift). The greenhouse heating items (4500–4535) and the ENERGIFORBRUG I ALT total (4500) are NOT available for these farm types.
- Only brugstype 4 (Gartneri) and detailed gartneri subtypes (538–575) have all 27 regnskposter including 4500 (ENERGIFORBRUG I ALT) and greenhouse heating breakdowns.
- For organic farming (brugstype=3) energy: available items include fuel for machinery/vehicles (4545–4560), building heating (4605–4620), and green taxes (4625–4640). There is no single total energy row; you must sum the relevant sub-items.
- brugstype 552 (Prydplanter < 15.000 m2) starts from 2020 — new category that replaced 545/550 split.
- indhold values are per-farm averages. kvartil=1000 for all-farm average.