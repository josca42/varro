table: fact.kys02
description: Kontanthjælp (sæsonkorrigeret) efter ydelsestype, sæsonkorrigering og tid
measure: indhold (unit Antal)
columns:
- ydelsestype: values [10000=Ydelser i alt, 10050=Kontanthjælp i alt, 10025=Uddannelseshjælp i alt, 10060=Løntilskud vedrørende kontant- og uddannelseshjælpsmodtagere m. fl. I alt, 10070=Kontant- og uddannelseshjælp under forrevalidering i alt, 10020=Kontanthjælp og integrationsydelse til udlændinge m.fl. i alt, 10040=Revalideringsydelse i alt, 10036=Kontant- arbejdsmarkeds- og uddannelsesydelse, i alt]
- saeson: values [10=Sæsonkorrigeret, 20=Faktiske tal]
- tid: date range 2007-01-01 to 2025-06-01
notes:
- saeson is a measurement selector: 10=Sæsonkorrigeret, 20=Faktiske tal. Every dimension combination appears twice. Always filter to one value.
- ydelsestype codes are hierarchical: 10000=Ydelser i alt is the grand total; 10050/10025/10060/etc. are sub-categories. Do not sum all ydelsestype values — pick the level you need.
- Simplest table for total monthly recipients: WHERE saeson='20' AND ydelsestype='10000'.
