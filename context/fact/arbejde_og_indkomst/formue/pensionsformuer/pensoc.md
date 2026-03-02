table: fact.pensoc
description: Husholdningernes pensionsrettigheder i socialforsikringsordninger efter pensionsordninger, konto og tid
measure: indhold (unit Mio. kr.)
columns:
- pensord: values [TPS=Pensionsordninger i alt, TGG=Offentlige pensionsordninger i alt, TJP=Tjenestemandspension, TJPIF=Tjenestemandspension: Ikke-fondsbaseret, TJPF=Tjenestemandspension: Fondsbaseret, EFT=Efterløn, TNGG=Ikke-offentlige pensionsordninger i alt, DCS=Bidragsdefinerede ordninger, DBS=Ydelsesdefinerede ordninger og andre ikke-bidragsdefinerede ordninger, TRH=Pensionsordninger i alt: Danske husholdninger bosat i Danmark, TNRH=Pensionsordninger i alt: Danske husholdninger bosat i udlandet]
- konto: values [LS=Primo: Pensionsrettigheder, D61=D61: Stigning i pensionsrettigheder forårsaget af sociale bidrag (D6111+D6121+D6131+D6141-D61SC), D6111=D6111: Faktiske arbejdsgiverbidrag til sociale ordninger, D6121=D6121: Imputerede arbejdsgiverbidrag til sociale ordninger, D6131=D6131: Husholdningernes faktiske bidrag til sociale ordninger, D6141=D6141: Husholdningernes supplerende bidrag til sociale ordninger, D61SC=D61SC: Gebyrer til pensionsordninger, D619=D619: Anden (aktuarmæssig) i pensionsrettigheder i socialsikringspensioner, D62=D62: Reduktion i pensionsrettigheder forårsaget af udbetaling af pensionsydelser, D8=D8: Ændringer i pensionsrettigheder forårsaget af bidrag til sociale ordninger (D61+D619-D62), K7=K7: Ændringer i rettigheder forårsaget af omvurderinger, K5=K5: Ændringer i rettigheder forårsaget af andre mængdeændringer, LE=Ultimo: Pensionsrettigheder (Primo+D8+K7+K5)]
- tid: date range 2015-01-01 to 2023-01-01

notes:
- pensord has a two-level hierarchy: TPS=total = TGG (offentlige) + TNGG (ikke-offentlige). TGG = TJP + EFT; TJP = TJPIF + TJPF. Never sum across pensord without filtering to leaf codes. TRH and TNRH are special sub-populations (husholdninger i Danmark vs. i udlandet) that also sum to TPS.
- konto encodes national accounts stocks and flows — these cannot be summed across entries. LS=primo (opening stock), LE=ultimo (closing stock) = LS + D8 + K7 + K5. D8 = D61 + D619 - D62. Always filter to exactly one konto. For "total pension wealth at end of year" use konto='LE'.
- indhold is in Mio. kr. (millions of DKK).
- This is a macro-level national accounts table (husholdningssektoren som helhed) — no breakdown by individual, age or geography.