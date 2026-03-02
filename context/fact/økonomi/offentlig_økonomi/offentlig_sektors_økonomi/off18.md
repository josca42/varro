table: fact.off18
description: Offentlig forvaltning og service, renter efter indtægt/udgift og tid
measure: indhold (unit Mio. kr.)
columns:
- indtudg: values [1=1. Renteudgifter mv. i alt, 11=1.1. Nominelle renter mv. i alt, 111=1.1.1. Nominelle renter til indland, 112=1.1.2. Nominelle renter til udland, 12=1.2. Fordelte emissionskurstab i alt, 121=1.2.1. Fordelte emissionskurstab til indland, 122=1.2.2. Fordelte emissionskurstab til udland, 130=1.3. Renteudgifter til indland i alt (1.1.1.+1.2.1.), 140=1.4. Renteudgifter til udland i alt (1.1.2.+1.2.2.), 2=2. Renteindtægter samt aktieudbytte og dividende mv. i alt, 21=2.1. Aktieudbytte og dividende mv., 22=2.2. Nominelle renter i alt, 221=2.2.1. Nominelle renter fra indland, 222=2.2.2. Nominelle renter fra udland, 23=2.3. Fordelte udtræksgevinster i alt (kursgevin. på det offentliges beholdning af obligationer), 231=2.3.1. Fordelte udtræksgevinster fra indland, 232=2.3.2. Fordelte udtræksgevinster fra udland, 240=2.4. Renteindtægter fra indland i alt (2.1.+2.2.1.+2.3.1.), 250=2.5. Renteindtægter fra udland i alt (2.2.2.+2.3.2.)]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- indtudg: two top-level branches — 1=Renteudgifter i alt, 2=Renteindtægter+aktieudbytte i alt. Sub-codes (11, 12, 130, 140 under branch 1; 21, 22, 221, 231, 240, 250 under branch 2) are components. Code 1 = 11+12, code 130=renteudgifter til indland, 140=til udland. Don't sum parent and child codes together.
- Simple net interest can be computed as indhold WHERE indtudg='2' minus indhold WHERE indtudg='1' for the same year.