table: fact.flyv3
description: Aktivitet på offentlige betjente lufthavne efter lufthavn, enhed og tid
measure: indhold (unit -)
columns:
- lufthavn: values [10010=LUFTHAVNE IALT, 10015=København, 10020=Billund, 10025=Aarhus, 10030=Aalborg, 10035=Midtjyllands Lufthavn (tidligere Karup), 10040=Esbjerg, 10045=Bornholm, 10050=Sønderborg, 10055=Roskilde, 10060=Thisted, 10065=Hans Christian Andersen Airport (Odense), 10070=Øvrige lufthavne]
- maengde4: values [150=1000 passagerer, 151=Gods, 100 ton, 152=Flyoperationer, 1000]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- maengde4 is a measurement-type selector with 3 incompatible units: 150=1000 passagerer, 151=Gods 100 ton, 152=Flyoperationer 1000. Each (lufthavn, tid) pair has 3 rows. Always filter to a single maengde4 value — summing across them mixes units and triples counts.
- lufthavn=10010 (LUFTHAVNE IALT) is the national aggregate. When summing individual airports, exclude it. When you want a single national total, use lufthavn=10010 directly.
- To get passenger totals by airport: WHERE maengde4=150 AND lufthavn != 10010.
- flyv3 covers all 13 airport codes including 10070=Øvrige lufthavne (other airports); flyv21 does not include 10070.