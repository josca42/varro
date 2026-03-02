table: fact.kv2fr3
description: Foreningsmedlemskab efter foreningstype, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- forentyp: values [43100=Patient- eller pårørendeforening, 43110=Naturforening eller miljø-interesseorganisation, 43120=Politisk parti eller -forening, 43130=Idrætsforening eller idrætsklub, 43140=Velgørende, social eller humanitær forening, 43150=Kulturel forening, 43160=Fagforening, faglig forening eller brancheforening, 43170=Fritids- eller hobbyforening, 43180=Bolig- eller borgerforening, 43190=Anden type forening]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Each forentyp row gives the percentage of people who are members of that association type. A person can be a member of multiple types, so forentyp categories are NOT mutually exclusive — DO NOT sum across forentyp values.
- For the national rate per association type: filter kon='10' AND alder='TOT'. Single 2024 annual observation.
