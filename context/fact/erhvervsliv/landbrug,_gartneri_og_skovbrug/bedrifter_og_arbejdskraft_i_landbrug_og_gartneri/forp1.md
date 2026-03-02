table: fact.forp1
description: Bedrifter med forpagtning efter enhed, areal, forpagtning og tid
measure: indhold (unit -)
columns:
- enhed: values [ANTAL=Bedrifter (antal), AFP=Forpagtet areal (ha), AREAL=Samlet dyrket areal (ha)]
- areal1: values [AIALT=I alt, A1=Under 10,0 ha, A19=10,0 - 19,9 ha, A29=20,0 - 29,9 ha, A49=30,0 - 49,9 ha, A62=50,0 - 74,9 ha, A100=75,0 - 99,9 ha, A210=100,0 - 199,9 ha, A220=200,0 ha og derover]
- forp: values [4000=Alle bedrifter, 4010=Ingen forpagtning, 4015=Forpagtning 0,1-9,9 pct., 4020=Forpagtning 10,0-24,9 pct., 4025=Forpagtning 25,0-49,9 pct., 4030=Forpagtning 50,0-74,9 pct., 4035=Forpagtning 75,0-99,9 pct., 4040=Forpagtning 100 pct.]
- tid: date range 1982-01-01 to 2024-01-01

notes:
- enhed is a measure-type selector with 3 values: ANTAL (farm count), AFP (forpagtet areal in ha), AREAL (samlet dyrket areal in ha). Each dimension combination appears 3 times — always filter to exactly one enhed.
- forp: 4000=Alle bedrifter is the grand total. 4010=Ingen forpagtning includes farms with no leased land. 4015-4040 are pct-brackets of how much of the farm is leased. The brackets (4010-4040) sum to 4000; don't sum them AND 4000 together.
- areal1: AIALT = all sizes. Filter to AIALT unless you need size breakdown.
- Longest forpagtning series (back to 1982). No regional breakdown — national only. Use bdf207 for regional forpagtning data.