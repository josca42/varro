Generelt
Forespørgsler sendes til den ønskede funktions url og de nødvendige informationer POST’es som et JSON-objekt.

Al kommunikation skal som udgangspunkt foregå i UTF-8.

API’et kan svare i hhv. JSON eller XML. For DATA-kaldet gælder andre og flere returformater.

Det er muligt at angive parametre i url’en, men det anbefales at POST’e data. Ved angivelse af indstillinger i URL’en (GET), skal oplysningerne url-encodes. Se eksempler i konsollen.

API’ets grundlæggende adresse er https://api.statbank.dk 

Funktion
Der skal altid angives versionsnummer samt navnet på den ønskede funktion:

https://api.statbank.dk/v1/subjects
https://api.statbank.dk/v1/tables
https://api.statbank.dk/v1/tableinfo
https://api.statbank.dk/v1/data

Kommunikation via TLS 1.2 
Alle forespørgsler til Statistikbankens API skal ske via TLS 1.2 (Transport Layer Security version 1.2).

Dette kan de fleste nyere browsere og programmeringssprog håndtere. Dog skal man muligvis opgradere ældre programmer til en nyere kodebase.

Fx understøtter .NET Framework 4.5 ikke TLS 1.2 som standard, og der skal man indsætte følgende kodelinje før forespørgslen: 

ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
Bruger man .NET Framework 4.0, er det muligt, at det er nødvendigt at skrive det som ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;
ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072
Nogle brugere anvender Visual Studio sammen med SQL Server Integration Services, og der kan godt være problemer, selv om man anvender .NET 4.7. Der skal man indsætte et "script task" i den pågældende Integration Services-pakke i Visual Studio (fx Sql Server Data Tools) med ovenstående linje før eksekveringen af et "Data Flow Task".

Bruger man Delphi/Pascal, kan løsningen være noget i denne stil:

uses IdHTTP, IdGlobal, IdSSLOpenSSL;
...
begin
  FHTTP := TIdHTTP.Create;
  FIOHandler := TIdSSLIOHandlerSocketOpenSSL.Create;
  FIOHandler.SSLOptions.SSLVersions := [sslvTLSv1_2];
  FHTTP.IOHandler := FIOHandler;
...
end;
Sprog
Som udgangspunkt svarer API’et på dansk. Sproget kan for alle kald angives med en parameter:

{
   "lang": "en"
}
Der kan angives enten "da" for dansk eller "en" for engelsk.

API’et vil i visse tilfælde returnere fejlmeddelelser på både dansk og engelsk, hvis fejlen har resulteret i manglende bestemmelse af sprog.

Format
For alle andre funktioner end DATA, kan formaterne JSON eller XML angives:

{
   "format": "JSON"
}
Tabeller og emner
Der er to måder at finde frem til tabeller via API’et.  Funktionerne SUBJECTS og TABLES.

SUBJECTS
Funktionen SUBJECTS tilgår det hierarki af emner, hvori alle tabeller er placeret. Hierarkiet kan tilgås ét eller flere niveauer ad gangen.

Hvis funktionen kaldes uden angivelse af parametre, returneres øverste niveau i hierarkiet. Herefter kan disse emners underemner findes ved igen at kalde SUBJECTS med angivelse af de ønskede emner og så fremdeles.

Der kan angives flg. funktionsspecifikke parametre:

{
   "subjects": [
      "02",
      "2401"
   ],
   "includeTables": true,
   "recursive": true,
   "omitInactiveSubjects": true
}
subjects: Emner for hvilke, der ønskes underemner.

includeTables: Hvorvidt resultatet skal indeholde tabeller. I modsat fald returneres kun emner, og tabeller kan efterfølgende hentes med funktionen TABLES.

recursive: Hvorvidt emners underemner/tabeller skal hentes hele vejen ned gennem hierarkiet. I modsat fald hentes kun nærmeste niveau under de angivne emner.

omitInactiveSubjects: Hvorvidt emner skal undlades, hvis de eller andre emner i det pågældende hierarki ikke længere opdateres.

TABLES
Funktionen TABLES returnerer tabeller filtreret efter bestemte kriterier. Hvis der ikke angives nogle kriterier, returneres alle tabeller.

Der kan angives flg. funktionsspecifikke parametre:

{
   "subjects": [
      "02",
      "2401"
   ],
   "pastdays": 1,
   "includeinactive": true
}
subjects: Emner fra hvilke der skal returneres tabeller. Emnekoder hentes med funktionen SUBJECTS.

pastdays: Antal af dage indenfor hvilke returnerede tabeller skal være opdateret.

includeInactive: Hvorvidt der skal returneres tabeller, som ikke længere opdateres.

Metadata og data
En tabel består af metadata og data.

Metadata er informationer om bl.a. tabellens titel samt enheden for data. For visse data-formater, fx CSV, er disse informationer kun tilgængelige i metadata, hvorfor disse bør læses i forbindelse med hver læsning fra tabellens data.

For andre formater, fx Excel eller graf (PNG), indeholder selve data også information om fx titel og enhed. Det kan dog stadig være en god idé at læse metadata, for fx at se en eventuel note til data.

TABLEINFO
Funktionen TABLEINFO returnerer metadata for en tabel. Svaret indeholder information om variable og disses koder i tabellen. Det er disse koder, der skal anvendes, når data efterspørges med funktionen DATA.

Der skal altid angives tabel:

{
   "table": "folk1c"
}
DATA
Funktionen DATA returnerer data fra en tabel.

API’et forsøger at eliminere de af variablene, der ikke er valgt værdier for. Hvis der fx ikke vælges område i tabellen FOLK1C, returneres data for hele landet.

For de variable, der ikke ønskes elimineret, angives variablen ved dennes kode samt koderne for de værdier, der ønskes. Koder for variable og værdier findes via funktionen TABLEINFO.

Fx har tabellen FOLK1C’s variabel ”oprindelsesland” koden ”ieland”, og værdien ”Danmark” for denne variabel har koden ”5100”. Hvis der ønskes data for de observationer, hvor oprindelsesland er Danmark, angives:

{
   "table": "folk1c",
   "format": "CSV",
   "variables": [
      {
         "code": "ieland",
         "values": [
            "5100"
         ]
      }
   ]
}
For værdier kan angives ”*” som jokertegn, sådan at ”*” betyder alle værdier, og fx ”*K1” betyder alle koder, der ender med ”K1”.

Nogle tabeller indeholder variable, som ikke kan elimineres automatisk. Der skal altid vælges værdier for disse. Dataformater, der streames, tillader slet ikke elimination af variable.

En sum angives som fx "sum(0-4;5-9;10-14;15-19;20-24)", hvilket returnerer en sum af de angivne koder. Summen kan tilføjes en tekst: "sum(0-24 år=0-4;5-9;10-14;15-19;20-24)" og en kode: "sum(0_24|0-24 år=0-4;5-9;10-14;15-19;20-24)". Hvis samme forespørgsel bruges til at trække data i forskellige sprog, kan det være nyttigt at tilføje specifikke tekster for hvert sprog: "sum(0_24|[da 0-24 år][en 0-24 years]=0-4;5-9;10-14;15-19;20-24)".

Ud over sum kan man også anvende metoderne multiply (gange), divide (dividere) og subtract (minus) på samme måde som sum med undtagelse af, at det er nødvendigt at vælge præcis to koder. Fx "subtract(15-19;10-14)", hvilket for tabellen folk1c returnerer antallet af 15-19-årige fratrukket antallet af 10-14-årige. De øvrige metoder virker på samme måde. 

Dataformater der streames, tillader ikke ovenstående type beregninger.

Der kan angives sekvenser af koder ved en før/lig/efter-betingelse. Perioden 1. kvt. 2010 til 4. kvt. 2015 kan fx angives ved ">=2010K1<=2015K4". Betingelsen kan angives med eller uden "=" og kan kombineres med andre valg for samme variabel. Bemærk at de enkelte valg ikke har indflydelse på hinanden. Derfor vil ">=2010K1" og "<=2015K4" angivet hver for sig give hhv. alle værdier fra og med 2010K1 samt alle værdier til og med 2015K4, hvilket i praksis er alle variablens værdier.

Perioder returneres sorteret (enten stigende eller som angivet i timeOrder) uanset i hvilken rækkefølge, de er angivet i forespørgslen, ligesom dubletter automatisk frasorteres. Perioder kan, ligesom andre variables værdier, angives ved deres kode inkl. evt. brug af joker-tegnet "*". Der kan derudover anvendes nth-regler til angivelse af perioder. Nth-regler skal altid omkranses af parentes. Foranstillet +/- eller first/last bestemmer fra hvilken ende af perioderne, der tælles. Seneste tre perioder kan fx angives (-n+3). Ældste tre perioder -(-n+3), nyeste periode (1), næst-nyeste periode (2), næstældste periode -(2) etc. Koder og regler kan blandes i en kommasepareret liste. Nth-reglen fungerer ligesom css-selectoren beskrevet på http://www.w3.org/TR/2011/REC-css3-selectors-20110929/#nth-child-pseudo.

Hvis der ikke angives en ønsket periode, returneres data for seneste periode i tabellen svarende til at angive "(1)".

Der er flg. funktionsspecifikke parametre, hvoraf table og format altid skal angives.

{
   "table": "folk1c",
   "format": "CSV"
   "valuePresentation": "Default",
   "timeOrder": "Ascending",
   "variables": [
      {
         "code": "OMRÅDE",
         "placement": "stub",
         "values": [
            "000",
            "185",
            "791",
            "787"
         ]
      },
      {
         "code": "KØN",
         "values": [
            "*"
         ]
      },
      {
         "code": "Tid",
         "values": [
            "2010k2",
            "(1)"
         ]
      }
   ]
}
table: Tabel der skal hentes data fra.

format: Format data ønskes returneret i. Se afsnittet Data-formater.

valuePresentation: Hvordan tekster skal vises. Parameteren kan udelades, eller der kan angives en af flg. værdier:
Default, Code, Value, CodeAndValue eller ValueAndCode

timeOrder: Rækkefølge for perioder angivet som ascending eller descending.

variables: Samling af variabel-objekter med angivelse af dennes kode samt koderne for de ønskede værdier. I eksemplet hentes data for områderne Hele landet (000), Tårnby (185), Viborg (791) og Thisted (787), for alle køn (*) for perioden 2. kvartal 2010 (2010K2) samt nyeste periode ((1)). Det er desuden angivet, at variablen område skal placeres i tabellens forspalte (angives som hoved (head) eller forspalte (stub)).

Særlige beregninger
Der kan foretages nogle udvalgte særlige beregninger. På nuværende tidspunkt understøttes procent- og promilleberegning. Funktionaliteten skal tilvælges via en række indstillinger, der er beskrevet i det følgende:

Operation er FRIVILLIG. Den er default sat til Percent og kan ellers sættes til Permille.
SelectedVariableCode er SEMI-OBLIGATORISK. Den SKAL angives, hvis der er valgt mere end én variabel i det selvstændige indstillingsfelt Variables. Der skal angives koden for den variabel, der tages udgangspunkt i, fx KØN.
AddAsNewValue er FRIVILLIG. Den er default sat til False. Hvis den bliver sat til True, tilføjes en ekstra variabel med indholdstypen (fx om det er antal eller pct., som et tal vedrører)
Nedenstående anvendes kun, hvis AddAsNewValue er angivet til True:
NewValueName er FRIVILLIG. Hvis intet er angivet, angives "Procent" eller "Promille" på dansk og "Percent" "Per Mille" på engelsk. Dette er så indholdet i den nye indholdstypevariabel. Hvis angivet, bruges den angivne værdi for indholdstypen. Den oprindelige værdi bliver automatisk defineret (fx antal).
NewValuePlacement er FRIVILLIG. Hvis intet er angivet, kommer indholdstype-variablen i hovedet (Head) - den anden variant er Stub. Har ingen konsekvens for fx CSV-filer, men kan være afgørende at definere i fx HTML.
ContentTypeCode er FRIVILLIG. Hvis intet er angivet, bliver koden for indholdstype-variablen "IndholdsType" på dansk og "ContentType" på engelsk.
BasisValueForCalculation er FRIVILLIG. Hvis intet er angivet, bliver procent (eller promille) fordelt på alle valgte værdier. Hvis der angives en værdi, bliver beregningen baseret på den valgte værdi, der sættes til 100 (ved pct.) eller 1000 (ved promille).
Dataformater, der streames, tillader ikke særlige beregninger.

Eksempel på alle indstillinger i brug (se valueTransformationSettings):

{
   "table": "FOLK1A",
   "format": "CSV",
   "variables": [
      {
         "code": "KØN",
         "values": [
            "*"
         ]
      },
      {
         "code": "CIVILSTAND",
         "values": [
            "*"
         ]
      }
   ],
   "valueTransformationSettings": {
      "operation": "percent",
      "selectedVariableCode": "KØN",
      "addAsNewValue": "true",
      "newValueName": "Procent",
      "newValuePlacement": "Head",
      "contentTypeCode": "Indholdstype",
      "basisValueForCalculation": "TOT"
   }
}
Data-formater

For DATA-funktionen kan flg. data-formater vælges:

PX : PC-Axis (ANSI)
CSV: Semikolonsepareret
JSONSTAT: JSON-stat
DSTML: Statistikbankens XML-format
PNG: Graf som billede (se beskrivelse nedenfor)
AREMOS: AREMOS

Flg. er streaming-formater, som beskrives nedenfor:
BULK: Semikolonsepareret fil
SDMXCOMPACT: SDMX-ML Compact
SDMXGENERIC: SDMX-ML Generic

Flg. er præsentationsformater, for hvilke det gælder, at der kan laves småændringer i produktionsmiljøet, selvom systemet ikke skifter versionsnummer:
XLSX: Excel
HTML: HTML

Særlige dataformater
PNG
Data kan returneres som en graf. For dette format kan der angives en række parametre, der angiver, hvordan grafen præsenteres i den returnerede billedfil.

{
   "table": "folk1c",
   "format": "PNG",
   "variables": [
      {
         "code": "køn",
         "values": [
            "1",
            "2"
         ]
      }
   ],
   "chartsettings": {
      "type": "column",
      "width": "900",
      "height": "400",
      "showlegend": "true",
      "showtitle": "true",
      "fontsize": "13",
      "sort": "false",
      "autopivot": "true",
      "labelsangle": "0",
      "titlecolor": "ff000000",
      "seriescolors": [
         "00ff00",
         "0000ff"
      ],
      "valuecolors": [
         "2ff0000"
      ]
   }
}
I eksemplet trækkes data fra tabellen FOLK1C. Værdierne Mænd (1) og Kvinder (2) vælges for variablen Køn. Der angives endvidere en række indstillinger vedrørende grafens præsentation:

type: Graf-type i hvilken data ønsket præsenteret. Der kan angives flg. værdier:
Line, Column, StackedColumn, StackColumn100, Bar, StackedBar,
StackedBar100, Area, StackedArea, StackedArea100, Pie, ColumnAndLines, Population.

width: Billedets bredde i pixels.

height: Billedets højde i pixels.

Ved ændring af størrelsen skaleres billedet ikke blot. Selve grafens udformning bestemmes af den til rådighed værende plads.

showlegend: Hvorvidt billedet skal indeholde en boks med angivelse af serie-tekster.

showtitle: Hvorvidt billedet skal indeholde tabellens titel og undertitel.

fontsize: Skriftstørrelse.

sort: Hvorvidt observationerne skal sorteres.

autopivot: Hvorvidt variablen med flest værdier skal flyttes til label-aksen.

labelsangle: Vinkel på tekster på label-aksen.

seriescolors: Samling af farver til serier. Farver angives som fx ”ff0000” for rød. I ovenstående eksempel angives grøn og blå som de første farver, der skal anvendes til serier

valuecolors: Samling af farver til specifikke værdier. Angives ved kode efterfulgt af farve. I ovenstående eksempel angives, at koden 2 (Kvinder) skal vises med farven rød.

STREAMINGFORMATER
Hvis der vælges mange værdier fra en tabel, kan nogle udtræk blive for store at håndtere på serveren. Nogle udtræk kan komme op på flere milliarder celler. Der er indlagt en grænse for maksimalt antal observationer for almindelige dataformater. Grænsen kan variere fra tid til anden, men det vil fremgå af opdateringsoversigten, hvad den aktuelle er. Bruger man derimod streaming-formater, gælder denne grænse ikke.

Da datasæt af denne størrelse sagtens kan anvendes i fx databaser, har vi valgt at stille denne output-type til rådighed.

Resultatet adskiller sig fra de øvrige formater på en række vigtige områder:

- Nogle observationer udelades. Hvis en kombination af værdier mangler, er observationen for denne kombination 0 (tallet nul). Hvis kombinationen er repræsenteret, men tallet mangler, betyder det, at observationen mangler, er diskretioneret eller er for usikker til at kunne angives.

- Variable kan ikke udelades (elimineres) og rækkerne (værdierne) er ikke nødvendigvis sorteret i samme rækkefølge som angivet i forespørgslen.

CATALOGUE
Denne metode leverer metadata om tabeller ud i et såkaldt DCAT-AP katalog, der er en xml-fil med data om tabeller, distributioner og kontakter linket sammen på forskellig vis. Dette format anvendes blandt andet af Digitaliseringsstyrelsens Datavejviser.

Brugen af metoden kræver en API-nøgle, der kan ansøges om ved henvendelse til Danmarks Statistik (se bunden af siden). 
Begrænsninger på udtræk
Gennem årene er brugen af API'et steget kraftigt. Det har betydet, at der er indført en grænse på antallet af hentede celler for almindelige hentningsformater, hvor alt indhold er hentet på én gang. Begrænsningen gælder ikke for de såkaldte "bulk"-formater, hvor data bliver streamet i mindre portioner uden øvre grænse.

Antallet af celler, der maksimalt kan hentes via "non-bulk" (fx CSV, px m.fl.) er p.t. sat til 1.000.000 celler, men kan ændres i fremtiden, blandt andet baseret på brugernes behov og tilbagemeldinger.

Antallet af celler er beregnet ud fra en simpel formel: Det maksimale antal udtrukne rækker ganget med antallet af valgte felter, hvor tid og observationens værdi begge er obligatoriske felter. En observation består foruden selve værdien af en række variable, såsom tidsperioden og andre beskrivende dele (fx område eller køn). Hver del bliver til en enkeltstående celle. 

Nedenfor er et tilfældigt eksempel med fem variable, inklusive den obligatoriske tidsvariabel, der altid hentes, og feltet med selve værdien, altså 5.825.337. Denne ene række med seks kolonner giver derfor i alt seks celler, når en række ganges med seks kolonner.

OMRÅDE 

KØN

ALDER

CIVILSTAND

TID

INDHOLD

Hele landet

I alt

I alt

I alt 

2020K3

5.825.337

 

For nogle udtræk vil der reelt set være færre udtrukne rækker og celler, da der kan mangle observationer for forskellige variable og/eller tidsperioder. Dette tages der ikke højde for ved beregningen, der går på det maksimalt udtrukne antal celler.

Denne simple algoritme vil forventeligt løbende blive justeret.