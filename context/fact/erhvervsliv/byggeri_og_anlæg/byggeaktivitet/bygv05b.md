table: fact.bygv05b
description: Det samlede boligbyggeri (historisk oversigt) efter byggefase, bygherreforhold og tid
measure: indhold (unit Antal)
columns:
- bygfase: values [20=Tilladt boliger (1981 -), 22=Påbegyndt boliger (1938 - ), 24=Fuldført boliger (1917 - ), 26=Boliger under opførelse (1981 - )]
- bygherre: join dim.bygherre on bygherre=kode::text [approx]; levels [2]
- tid: date range 1917-01-01 to 2024-01-01
dim docs: /dim/bygherre.md
notes:
- Historical series from 1917 by bygherre. National totals only. Same bygfase coding as bygv05a (20=Tilladt, 22=Påbegyndt, 24=Fuldført, 26=Under opførelse).
- bygherre does NOT join cleanly to dim.bygherre. Only code '20' (alment boligselskab) matches. Codes '00' and '09' are legacy total/aggregate codes; 'SK' = stat og kommuner (public). Use inline values.
- The modern equivalent with clean bygherre coding is bygv33 (regional, from 2006) or bygv03 (national, from 1981). Those have different bygherre groupings but more consistent coding.
