table: fact.kv2brn1
description: Kulturvaner i barndomshjemmet efter kulturvane, omfang, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- kultvane2: values [43400=Der var mindst én voksen, der jævnligt læste, lyttede til eller så nyheder, 43410=Der var mindst én voksen, som jævnligt læste eller lyttede til bøger, 43420=Jeg blev jævnligt taget med på museum, i teatret eller til koncerter, 43430=Da jeg var lille blev der jævnligt læst bøger højt for mig derhjemme, 43440=Der blev jævnligt sunget, spillet på musikinstrumenter eller lignende, 43450=Der blev jævnligt dyrket sport og motion]
- bogtype: values [43460=Passer helt, 43470=Passer nogenlunde, 43480=Passer ikke]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Measures how well 6 childhood cultural habits applied to the respondent, using a 3-point agreement scale (bogtype: passer helt/nogenlunde/passer ikke). For each kultvane2+kon+alder, bogtype values are mutually exclusive and sum to ~100%.
- kultvane2 habits are NOT mutually exclusive — a person can agree with multiple. Do not sum across kultvane2.
- To see "% where habit fully applied": filter bogtype='43460' (Passer helt). For "% where it applied at all": sum bogtype 43460 and 43470.
- Single 2024 annual observation.
