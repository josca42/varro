table: fact.pest2
description: Det samlede pesticidsalg efter pesticidtype, måleenhed og tid
measure: indhold (unit -)
columns:
- pesticidtype: values [TOT=I alt, HERB=Herbicider, FUNG=Fungicider, ALGE=Midler mod algevækst, INSEKT=Insekticider, SLIM=Midler mod slimdannende organismer i papirmasse, UTØJ=Midler mod utøj på husdyr mv, INSEKT1=Insekticider inkl. midler mod utøj på husdyr mv, VÆKST=Vækstregulatorer, FUIN=Kombinerede fungi- og insekticider, JORD=Jorddesinfektionsmidler, GNAV=Gnavermidler, SKRÆK=Afskrækningsmidler, TRÆ=Midler til behandling af træværk]
- maleenhed: values [PRODV=Produktvægt (tons), VIRKS=Virksomt stof (tons)]
- tid: date range 1981-01-01 to 2023-01-01

notes:
- maleenhed is a measurement selector: PRODV=Produktvægt (tons product weight) vs VIRKS=Virksomt stof (tons active substance). Every pesticidtype×tid pair appears twice. Filter to exactly one.
- pesticidtype: TOT=I alt is the grand total. Do not sum TOT with individual types.
- Several types changed over time — do not try to sum detailed types for a long historical series: INSEKT+UTØJ were used up to 2015, replaced by INSEKT1 (INSEKT incl. UTØJ) from 2015. JORD discontinued after 2017, FUIN after 2018, SLIM after 2005. Use TOT for consistent long-run series.
- This table covers ALL sectors (agriculture, forestry, non-agricultural). Use pest1 if you specifically want agricultural crop production with treatment frequency index.