table: fact.jord9
description: Energiforbrug for heltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- brugstype: values [1=Landbrug, 2=Konventionelt landbrug, 3=Økologisk landbrug, 4=Gartneri, 538=Væksthusgartneri, 540=Prydplanter, 545=Prydplanter, mindre end 7.500 m2 væksthusareal, 550=Prydplanter, 7.500-14.999 m2 væksthusareal, 552=Prydplanter, mindre end 15.000 m2 væksthusareal (2020-), 555=Prydplanter, 15.000 m2 eller mere væksthusareal, 560=Væksthusgrøntsager, 563=Frilandsgartneri, 565=Frilandsgrøntsager, 570=Frugt og bær, 575=Planteskole]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [4500=ENERGIFORBRUG I ALT, GIGAJOULE, 4505=OPVARMNING AF VÆKSTHUSE I ALT (ENERGIFORBRUG), GIGAJOULE, 4510=Opvarmning af væksthuse med naturgas, gigajoule, 4515=Opvarmning af væksthuse med fjernvarme, gigajoule, 4520=Opvarmning af væksthuse med let olie, gigajoule ... 4620=Opvarmning af staldbygninger mv., 1000 kr., 4625=GRØNNE AFGIFTER, 1000 KR., 4630=Grønne afgifter, CO2 og NOx-afgift, 1000 kr., 4635=Grønne afgifter, SO2 afgift, 1000 kr., 4640=Grønne afgifter, energiafgift, 1000 kr.]
- tid: date range 2008-01-01 to 2024-01-01
notes:
- brugstype focuses on gartneri subtypes (Væksthusgartneri, Prydplanter with greenhouse size brackets, Frilandsgartneri, etc.) plus aggregate codes 1–4. Greenhouse size splits (e.g., 545/550 vs 552/555) reflect pre-2020 vs post-2020 classification changes — don't mix them.
- regnskposter covers energy consumption items (4500–4640) in Gigajoule (physical) and 1000 kr. (cost). Units differ by code — always check the label before interpreting indhold.
- Same kvartil structure as other jord tables.
