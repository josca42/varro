table: fact.flyv11
description: Dansk registrerede fly pr. 1. januar efter type, enhed og tid
measure: indhold (unit Antal)
columns:
- type: values [20010=Fly i alt, 20015=Jet, 2 motorer, 20020=Jet, 3-4 motorer, 20025=Turbo-propel, 2 motorer, 20030=Turbo-propel, 4 motorer, 20035=Propel, 1 motor, 20040=Propel, 2 motor, 20045=Helikopter, 20050=Fly med 1-2 pladser, 20055=Fly med 3-5  pladser, 20060=Fly med 6-9  pladser, 20065=Fly med 10-99  pladser, 20070=Fly med 100 pladser eller mere]
- maengde4: values [155=Fly, 158=Pladser]
- tid: date range 1990-01-01 to 2025-01-01

notes:
- maengde4 is a unit selector: 155=Fly (aircraft count), 158=Pladser (total seat capacity). Always filter to one — they cannot be summed together.
- type=20010 (Fly i alt) is the grand total. Individual type codes cover both propulsion type (jet/turbo-propel/propel) AND size category (by seats). These two classification schemes overlap — a jet with 2 motors may also appear in a seat-count band.
- For a simple total aircraft count: WHERE type=20010 AND maengde4=155.