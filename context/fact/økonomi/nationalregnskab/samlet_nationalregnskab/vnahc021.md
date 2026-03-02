table: fact.vnahc021
description: Versionstabel NAHC021 - Husholdningers forbrug på dansk område (15 grp) efter version, formål, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2024_MAR=Martsversion 2024, V2024_FEB=Februarversion 2024, V2023_JUN=Juniversion 1966-2023 (Hovedrevision 2024)]
- formaaal: values [CPT=I alt, CPA=Fødevarer mv., CPB=Drikkevarer og tobak mv., CPC=Beklædning og fodtøj, CPD=Boligbenyttelse, CPE=Elektricitet, fjernvarme og andet brændsel, CPF=Boligudstyr, husholdningstjenester mv., CPG=Medicin, lægeudgifter o.l., CPH=Køb af køretøjer, CPI=Drift af køretøjer og transporttjenester, CPJ=Information og kommunikation, CPK=Fritid, sport og kultur, CPL=Undervisning, CPM=Restauranter og hoteller, CPN=Forsikring og finansielle tjenester, CPO=Andre varer og tjenester]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- version is a selector for different publication vintages: V2024_JUN=Juniversion 2021-2024 (most recent), V2024_MAR=Martsversion 2024, V2024_FEB=Februarversion 2024, V2023_JUN=Juniversion 1966-2023 (Hovedrevision 2024). Always filter to one version — typically V2024_JUN for the latest data.
- This is a version comparison table (versionstabel). Use nahc021 for the current official series. This table is for studying revisions between publication rounds.
- Also has prisenhed and formaaal selectors — same as nahc021: filter prisenhed to one value, and formaaal='CPT' for total.
