table: fact.penfor12
description: Personers pensionsformue efter familietype, alder, køn, prisenhed, pensionsformue og tid
measure: indhold (unit Antal)
columns:
- famtyp: values [ALL=Alle familetyper, EUB=Enlig uden hjemmeboende børn, EMB=Enlig med hjemmeboende børn, PUB=Par uden hjemmeboende børn, PMB=Par med hjemmeboende børn]
- alder: values [TOT18=Alder i alt (18 år og derover), 18-24=18-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-89=85-89 år, 9000=90 år og derover]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- penformue: values [0=Ingen pensionsformue, 1=0-100.000 kr, 100000=100.000-200.000 kr, 200000=200.000-400.000 kr, 400000=400.000-600.000 kr, 600000=600.000-800.000 kr, 800000=800.000-1.000.000 kr, 1000000=1.000.000-1.200.000 kr, 1200000=1.200.000-1.400.000 kr, 1400000=1.400.000-1.600.000 kr, 1600000=1.600.000-1.800.000 kr, 1800000=1.800.000-2.000.000 kr, 2000000=2.000.000-2.200.000 kr, 2200000=2.200.000-2.400.000 kr, 2400000=2.400.000-2.600.000 kr, 2600000=2.600.000-2.800.000 kr, 2800000=2.800.000-3.000.000 kr, 3000000=3.000.000-4.000.000 kr, 4000000=4.000.000-5.000.000 kr, 5000000=Over 5.000.000 kr]
- tid: date range 2014-01-01 to 2024-01-01

notes:
- prisenhed is a measurement selector for price base: 5=faste priser (seneste dataårs prisniveau), 6=nominelle priser. Always filter to one. Row counts differ slightly (40243 vs 39635) so some combinations are only available in one price unit.
- indhold is Antal (count of persons in each wealth bracket). To get the distribution of persons by wealth level, sum indhold across penformue brackets for a fixed prisenhed/famtyp/alder/koen/tid.
- penformue=0 means "ingen pensionsformue" — this is not a bracket but a flag. Brackets start from kode=1 (0-100.000 kr.) up to kode=5000000 (over 5 mio. kr.). Summing all 20 penformue codes gives the total person count.
- famtyp=ALL is the total; EUB/EMB/PUB/PMB are the four family types. koen=MOK and alder=TOT18 are totals.
- This table gives the wealth distribution (histogram) by family type — useful for inequality analysis. For mean/median use penfor11 instead.