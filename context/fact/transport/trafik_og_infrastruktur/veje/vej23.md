table: fact.vej23
description: Trafikarbejdet med danske køretøjer på danske veje efter transportmiddel og tid
measure: indhold (unit Mio. køretøjskm)
columns:
- transmid: values [0=KØRETØJER I ALT, 5=Cykler/knallert-30, 10=Motorkøretøjer i alt, 15=Personbiler i alt, 151=Personbiler, benzindrevne, i alt ... 46=Lastbiler i alt, 95=Sættevognstrækkere i alt, 105=Busser i alt, 106=Offentlig buskørsel, 107=Anden buskørsel]
- tid: date range 2000-01-01 to 2024-01-01

notes:
- transmid is hierarchical — DO NOT sum across all codes. The hierarchy is: 0 (all vehicles) = 5 (cycles) + 10 (motor vehicles); 10 includes 15 (all cars) + 46 (trucks) + 95 (semi-trailers) + 105 (buses); 15 (all cars) includes 151 (petrol) and other subtypes. Summing all 19 transmid values massively overcounts.
- To get total road traffic, filter transmid='0'. To split by major vehicle class use transmid IN ('5','10') or ('5','15','46','95','105'). Use ColumnValues("vej23", "transmid") to see all codes with labels.
- Annual data from 2000, measure is Mio. køretøjskm (million vehicle-kilometres).