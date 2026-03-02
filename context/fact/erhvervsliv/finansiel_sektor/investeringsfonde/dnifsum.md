table: fact.dnifsum
description: Investeringsfonde og investorernes formue efter investeringsfondstype, hovedkategori, forvaltningstype, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- investfond: values [XX=Total, AIF=Kapitalforeninger (AIF), UCITS=Investeringsforeninger (UCITS)]
- hovedkat: values [XX=Total, AK=Aktieafdeling, OB=Obligationsafdeling, BL=Blandet afdeling, HE=Hedgeafdeling, EJ=Ejendomsafdeling, PM=Pengemarkedsafdeling, PE=Private equity-afdeling, AN=Anden afdeling]
- forvalt: values [XX=Total, A=Aktiv forvaltning, P=Passiv forvaltning, N=Ikke relevant]
- data: values [1=Investorernes formue ultimo (Mio. kr.), 7=Investeringsfonde (Antal)]
- tid: date range 2018-01-01 to 2025-09-01

notes:
- data is a measurement selector: data='1' = investorernes formue ultimo (Mio. kr.), data='7' = antal investeringsfonde. Always filter to exactly one value — mixing them returns meaningless sums.
- investfond, hovedkat, and forvalt each have XX totals. Filter all three to avoid 8x overcounting. For a simple total, use investfond='XX', hovedkat='XX', forvalt='XX'.
- forvalt='N' (Ikke relevant) appears only for AIF (Kapitalforeninger), not UCITS. The forvalt='XX' total for AIF includes these N rows. When filtering forvalt='A' or forvalt='P', you silently miss the N category for AIF — use forvalt='XX' unless you specifically want active/passive split.
- For number of funds by category: data='7', then group by investfond/hovedkat as needed. For assets under management: data='1'.