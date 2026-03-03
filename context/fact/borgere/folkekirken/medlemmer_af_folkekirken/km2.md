table: fact.km2
description: Ind- og udmeldelser af folkekirken efter sogn, alder, folkekirkemedlemsskab og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- alder: values [0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år ... 80-84=80-84 år, 85-89=85-89 år, 90-94=90-94 år, 95-99=95-99 år, 100OV=100 år og derover]
- fkmed: values [F=Indmeldt i Folkekirken, U=Udmeldt af Folkekirken]
- tid: date range 2007-01-01 to 2025-04-01

notes:
- This table counts MOVEMENTS (joinings and leavings) NOT membership stock. fkmed here means F=Indmeldt (joined/enrolled), U=Udmeldt (left/withdrawn). This is different from km1/km5/km6 where F=current member.
- Quarterly data (tid: Jan, Apr, Jul, Oct). indhold = number of people who joined or left during that quarter. Sum across multiple quarters for annual totals.
- alder uses 5-year bands like km5 ('[0,5)', '[5,10)', ..., '[100,)'). No IALT total — sum all bands for aggregate.
- To find net change: SUM(CASE WHEN fkmed='F' THEN indhold ELSE -indhold END) groups by sogns/tid.
- F and U rows are independent counts and should NOT be summed together.
- Map: /geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
