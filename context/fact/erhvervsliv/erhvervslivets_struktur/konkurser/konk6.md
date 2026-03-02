table: fact.konk6
description: Erklærede konkurser efter omsætning og tid
measure: indhold (unit Antal)
columns:
- omsaetning: values [000=Konkurser i alt, OMS1=Ingen momspligtig aktivitet, OMS2=Omsætning under 1 mio. kr., OMS3=Omsætning 1-15 mio. kr., OMS4=Omsætning over 15 mio. kr.]
- tid: date range 2009-01-01 to 2025-09-01

notes:
- omsaetning='000' is the national total. OMS1–OMS4 sum to it, so exclude '000' when breaking down by size.
- OMS1 (ingen momspligtig aktivitet) and OMS2 (under 1 mio.) together correspond to the nulvirksomheder + small active companies. OMS3/OMS4 are the clearly active businesses. The omsætning threshold is based on the year before bankruptcy.