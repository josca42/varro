table: fact.kv2mus4
description: Brug af museers digitale tjenester efter tjeneste, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- tjen: values [30030=Museernes samlinger, 30040=Museernes sociale medier, 30050=Podcast udgivet af museerne, 30060=Foredrag, 30070=Oplysninger om åbningstider og pris, 30080=Nyheder om museet, 30090=Andre tjenester]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is % of respondents who used that digital museum service. tjen values are independent — a person uses multiple services. Never sum across tjen.
- Overall usage levels are low (sums ~35-38% per gender/age group), meaning most respondents use few or no digital museum services. Each individual percentage is already a small share of the population.
- Filter kon=10 and alder='TOT' for national results. Single year only (2024 survey).