table: fact.kv2brn2
description: Forbrug af kulturaktiviteter efter dine aktiviteter, kulturvaner i barndomshjemmet, omfang, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- dinakt: values [10100=Har set film, 10200=Har set serier, 10300=Har lyttet til musik, 10400=Har læst eller lyttet til bøger, 10500=Har læst, lyttet til eller set nyheder, 10600=Har brugt sociale medier, 10700=Har spillet digitale spil, 10800=Har dyrket sport eller motion, 20100=Har været i biografen, 20200=Har været til koncert eller musikfestival, 20300=Har set scenekunst eller sceneforestillinger live, på internettet eller i TV, 20400=Har opsøgt billedkunst fysisk eller digitalt, 20500=Har været fysisk på biblioteket, 20600=Har benyttet bibliotekernes digitale tjenester, 20700=Har overværet sportsbegivenhed som tilskuer, 20800=Har været på museum, 20900=Har besøgt dansk kulturarv]
- kultvane: values [43400=Der var mindst én voksen, der jævnligt læste, lyttede til eller så nyheder, 43410=Der var mindst én voksen, som jævnligt læste eller lyttede til bøger, 43420=Jeg blev jævnligt taget med på museum, i teatret eller til koncerter, 43430=Da jeg var lille blev der jævnligt læst bøger højt for mig derhjemme, 43440=Der blev jævnligt sunget, spillet på musikinstrumenter eller lignende, 43450=Der blev jævnligt dyrket sport og motion]
- bogtype: values [43460=Passer helt, 43470=Passer nogenlunde, 43480=Passer ikke]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- This is a correlation table: for people who currently do activity X (dinakt), what % grew up with childhood cultural habit Y (kultvane) at agreement level Z (bogtype)?
- Five dimensions (dinakt, kultvane, bogtype, kon, alder) — very large table. Always filter all non-target dimensions. To get national figures: kon='10' AND alder='TOT'. To isolate one childhood habit: pick one kultvane and one bogtype.
- dinakt and kultvane are both independent categories — do not sum across them. bogtype is mutually exclusive within each dinakt+kultvane+kon+alder combination.
- Use kv2brn1 for simpler childhood habit questions without the current-activity cross-tabulation.
- Single 2024 annual observation.
