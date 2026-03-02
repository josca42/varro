table: fact.bebrit09
description: Brug af internet til private formål - procent af befolkningen (16-74 år) efter type, formål og tid
measure: indhold (unit Pct.)
columns:
- type: values [10=I alt, 40=Alder: 16-19 år, 50=Alder: 20-39 år, 60=Alder: 40-59 år, 70=Alder: 60-74 år ... 210=Indkomst: 0-49.999 kr., 220=Indkomst: 50.000-99.999 kr., 230=Indkomst: 100.000-199.999 kr., 240=Indkomst: 200.000-299.999 kr., 250=Indkomst: 300.000 og derover]
- formaal: values [10=Sende/modtage e-mail, 20=Søge infomation om varer mv., 30=Services ifm. rejser mv, 40=Downloade software, 50=Læse/downloade nyheder ... 460=Søgt sundhedsrelaterede oplysninger, 470=Bestilt tid hos sundhedsfagligt personale via hjemmeside eller app, 480=Set egne eller familiemedlemmers sundhedsdata, 490=Spillet eller oddset for at vinde penge, 500=Brugt AI]
- tid: date range 2008-01-01 to 2025-01-01
notes:
- type is a demographic selector: type='10' = national total. Never sum across type values.
- formaal values are NOT mutually exclusive — respondents tick all internet purposes used in the past year. Values for top activities reach 90-98% each. Never sum across formaal values; each row is an independent % of population who used the internet for that purpose.
- All values are percentages of the 16-74 year old population.
