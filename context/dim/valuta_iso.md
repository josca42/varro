# Valutaer (ISO) (valuta_iso)

[ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) er den internationale standard for valutakoder. Formålet med ISO 4217 er at definere internationalt anerkendte koder af bogstaver og/eller tal, som kan anvendes til repræsentation af valutaer, fx ved internationale overførsler eller veksling. Standarden er udgivet første gang i 1978, men mange valutakoder har været anvendt før det.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Valuta | 163

## Niveau 1 — Valuta

kode | titel
--- | ---
AED | UAE dirham
AFN | Afganske afghani
ALL | Albanske lek
AMD | Armenske dram
ANG | Nederlandske Antiller-gylden
AOA | Angolansk kwanza
ARS | Argentinske peso convertible
AUD | Australske dollar
AWG | Arubanske florin
AZN | Aserbajdsjanske manat
BAM | Bosnien-Hercegovina konvertible mark
BBD | Barbadisk dollar
BDT | Bangladeshiske taka
BGN | Bulgariske lev
BHD | Bahrainske dinarer
BIF | Burundiske francs
BMD | Bermudianske dollar
BND | Bruneiske dollar
BOB | Bolivianske boliviano
BRL | Brasilianske real
BSD | Bahamanske dollar
BTN | Bhutanesiske ngultrum
BWP | Botswanske pula
BYN | Hviderussiske rubler
BZD | Beliziske dollar
CAD | Canadiske dollar
CDF | Congolesiske francs
CHF | Schweizerfranc
CLP | Chilenske peso
CNY | Kinesiske yuan renminbi
COP | Colombiansk peso
CRC | Costaricanske colón
CUC | Cubanske konvertible peso
CUP | Cubanske peso national
CVE | Kapverdiske escudo
CZK | Tjekkiske koruna
DJF | Djiboutiske francs
DKK | Danske kroner
DOP | Dominikanske peso
DZD | Algeriske dinarer
EGP | Egyptiske pund
ERN | Eritreanske nakfa
ETB | Etiopiske birr
EUR | Euro
FJD | Fijianske dollar
FKP | Falklandsøerne-pund
GBP | Pund sterling
GEL | Georgianske lari
GHS | Ghanesisk cedi
GIP | Gibraltar-pund
GMD | Gambianske dalasi
GNF | Guineanske francs
GTQ | Guatemalanske quetzal
GYD | Guyanske dollar
HKD | Hong Kong-dollar
HNL | Hondurasiske lempira
HRK | Kroatiske kuna
HTG | Haitianske gourde
HUF | Ungarske forint
IDR | Indonesiske rupiah
ILS | Israelske ny shekel
INR | Indiske rupee
IQD | Irakiske dinarer
IRR | Iranske rial
ISK | Islandske krona
JMD | Jamaicanske dollar
JOD | Jordanske dinar
JPY | Japanske yen
KES | Kenyanske shilling
KGS | Kirgisiske som
KHR | Cambodianske riel
KMF | Comoriske francs
KPW | Nordkoreanske won
KRW | Sydkoreanske won
KWD | Kuwaitiske dinarer
KYD | Cayman-øerne-dollar
KZT | Kasakhstanske tenge
LAK | Lao kip
LBP | Libanesiske pund
LKR | Srilankanske rupee
LRD | Liberiansk dollar
LSL | Lesotho loti
LYD | Libyske dinarer
MAD | Marokkanske dirham
MDL | Moldoviske leu
MGA | Madagaskiske ariary
MKD | Makedonske denar
MMK | Myanmar kyat
MNT | Mongolske tugrik
MOP | Macau pataca
MRU | Mauretanske ouguiya
MUR | Mauritiske rupee
MVR | Maldiviske rufiya
MWK | Malawiske kwacha
MXN | Mexicanske peso
MYR | Malaysiske ringgit
MZN | Mozambisk metical
NAD | Namibiske dollar
NGN | Nigerianske naira
NIO | Nicaraguanske cordoba oro
NOK | Norske kroner
NPR | Nepalesiske rupee
NZD | New Zealand-dollar
OMR | Omanske rial
PAB | Panamanske balboa
PEN | Peruvianske nuevo sol
PGK | Papua New Guineanske kina
PHP | Filippinske peso
PKR | Pakistanske rupee
PLN | Polske zloty
PYG | Paraguayanske guarani
QAR | Qatar rial
RON | Rumænske leu
RSD | Serbiske dinarer
RUB | Russiske rubler
RWF | Rwandiske francs
SAR | Saudiarabiske riyal
SBD | Salomonøerne-dollar
SCR | Seychellisk rupee
SDG | Sudaniske pund
SEK | Svenske kronar
SGD | Singaporeanske dollar
SHP | Sankt Helena-pund
SLL | Sierraleonske leone
SOS | Somalisk shilling
SRD | Surinamesiske dollar
SSP | Sydsudanske pound
STN | Sao Tome og Principe dobra
SVC | Salvadoranske colon
SYP | Syriske pund
SZL | Swazi lilangeni
THB | Thailandske baht
TJS | Tadsjikistansk somoni
TMT | Turkmenistanske manat
TND | Tunesiske dinar
TOP | Tongansk pa'anga
TRY | Tyrkiske lira
TTD | Trinidad og Tobago-dollar
TWD | Nytaiwanske dollar
TZS | Tanzanisk shilling
UAH | Ukrainsk hryvnia
UGX | Ugandiske shilling
USD | Amerikanske dollar
UYU | Uruguayske peso
UZS | Usbekiske sum
VES | Venezuelanske bolivar soberano
VND | Vietnamesiske dong
VUV | Vanuatu vatu
WST | Samoanske tala
XAF | Centralafrikanske CFA franc BEAC
XAG | Sølv
XAU | Guld
XCD | Østcaribiske dollar
XOF | Vestafrikanske CFA franc BCEAO
XPD | Palladium
XPF | CFP franc
XPT | Platinum
XTS | Valukode til test
XXX | Ingen valutaenhed
YER | Yeminitiske rial
ZAR | Sydafrikanske rand
ZMW | Zambianske kwacha
ZWL | Zimbabwe dollar

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.valuta_iso d ON f.valuta_iso = d.kode
WHERE d.niveau = 1
```
