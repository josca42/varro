table: fact.abst1
description: Arbejdsstandsninger efter branche, enhed og tid
measure: indhold (unit Antal)
columns:
- branche: values [0=I alt, 2=Landbrug, fiskeri og råstofudvinding, 4=Industri i alt, 6=Føde-, drikke- og tobaksvareindustri, 8=Tekstil- og læderindustri, 10=Træ-, papir- og grafisk industri, 12=Kemisk industri og plastindustri, 14=Sten-, ler- og glasindustri, 16=Jern- og metalindustri, 18=Møbelindustri og anden industri, 20=Energi- og vandforsyning, 22=Bygge- og anlægsvirksomhed, 24=Handel, 26=Hotel- og restaurationsvirksomhed, 28=Transport, post og tele, 30=Stat, regioner og kommuner, 32=Øvrige, 34=Uoplyst]
- enhed: values [100=Antal arbejdsstandsninger, 200=Antal berørte ansatte, 300=Antal tabte arbejdsdage]
- tid: date range 1996-01-01 to 2024-01-01

notes:
- enhed is a measurement selector: 100=Antal arbejdsstandsninger, 200=Antal berørte ansatte, 300=Antal tabte arbejdsdage. Every (branche, tid) row appears 3 times — once per measure. Always filter to a single enhed value, e.g. WHERE enhed=100. Summing across enhed values mixes incompatible units.
- branche=0 ("I alt") is the total across all sectors. branche=4 ("Industri i alt") is the aggregate of sub-industries 6, 8, 10, 12, 14, 16, 18. To avoid double-counting when summing across sectors, exclude the aggregates: WHERE branche NOT IN (0, 4).
- tid is annual (one row per year, stored as YYYY-01-01).
- branche=34 ("Uoplyst") only has data for some years; it may be absent in recent years.
- Example — tabte arbejdsdage per sektor i 2024 (without aggregates): SELECT branche, indhold FROM fact.abst1 WHERE tid='2024-01-01' AND enhed=300 AND branche NOT IN (0, 4) ORDER BY indhold DESC;