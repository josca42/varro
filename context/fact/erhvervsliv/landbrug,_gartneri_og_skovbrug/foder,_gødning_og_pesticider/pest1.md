table: fact.pest1
description: Salget af pesticider til anvendelse i landbrugets planteavl samt behandlingshyppighed efter pesticidgruppe, måleenhed og tid
measure: indhold (unit -)
columns:
- pesticidgr: values [TOT=I alt, HERB=Herbicider, FUNG=Fungicider, INSEKT=Insekticider, VÆKST=Vækstregulatorer]
- maleenhed: values [BEHHYP=Behandlingshyppighed, PRHA=Virksomt stof pr. ha (kg), VIRKS=Virksomt stof (tons), STOFPRHA=Kg virksomt stof pr. ha pr. behandling]
- tid: date range 1981-01-01 to 2023-01-01

notes:
- maleenhed is a measurement selector with 4 fundamentally different metrics — every pesticidgr×tid combination appears 4 times. Always filter to exactly one: VIRKS=Virksomt stof (tons active substance), PRHA=kg active substance per ha, BEHHYP=Behandlingshyppighed (treatment frequency index, dimensionless), STOFPRHA=kg active substance per ha per treatment.
- pesticidgr: TOT=I alt is the aggregate of HERB, FUNG, INSEKT, VÆKST. Do not sum TOT with any of the four groups.
- This table covers only agricultural crop production (planteavl). For total pesticide sales across all sectors use pest2.
- Treatment frequency index (BEHHYP) is the most-cited indicator of pesticide load — it measures how many full-dose treatments the sold/used amount corresponds to per ha.