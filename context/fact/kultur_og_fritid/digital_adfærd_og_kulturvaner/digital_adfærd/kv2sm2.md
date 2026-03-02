table: fact.kv2sm2
description: Forbrug af sociale medier efter indholdstype, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- indtyp: values [42760=Opslag om arrangementer, fester og aftaler, 42770=Danske nyheder, 42780=Udenlandske nyheder, 42790=Opslag fra danske politikere, 42800=Opslag fra udenlandske politikere, 42810=Konkurrencer og giveaways, 42820=Opslag eller stories fra familie og venner, 42830=Indhold fra influencere eller profiler med mange følgere, 42840=Opslag og videoer fra virksomheder, 42850=Køb og salg, 42860=Opslag om gaming, 42870=Pengeindsamlinger, 42880=Opslag fra interessefællesskaber eller i grupper, 42890=Andre indholdstyper]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- indtyp (content type) values are NOT mutually exclusive — users can engage with multiple content types on social media. Never sum across indtyp values.
- 2024 data only.
