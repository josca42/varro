table: fact.bil11
description: Bestanden af personbiler pr. 1. januar efter anvendelse, egenvægt og tid
measure: indhold (unit Antal)
columns:
- anvendelse: values [20000=Anvendelse i alt, 20100=Taxier, 20105=Udlejning, 20110=Skolekørsel, 20112=Sygetransport, 20115=Autocampere, 20125=Autocampere/udlejning, 20130=Brand- og redningskørsel, 20135=Anden anvendelse, 20140=Privatkørsel]
- egen: values [0=I alt, 600=0-600 kg, 601=601-700 kg, 701=701-800 kg, 801=801-900 kg, 901=901-1.000 kg, 1001=1.001-1.100 kg, 1101=1.101-1.200 kg, 1201=1.201-1.300 kg, 1301=1.301-1.400 kg, 1401=1.401-1.500 kg, 1501=1.501-1.600 kg, 1601=1.601-1.700 kg, 1701=1.701-1.800 kg, 1801=1.801-1.900 kg, 1901=1.901-2.000 kg, 2001=Over 2.000 kg, 2005=Uoplyst]
- tid: date range 1993-01-01 to 2025-01-01