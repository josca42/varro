table: fact.enebr
description: Industriens energiforbrug efter branche (DB07), enhed og tid
measure: indhold (unit -)
columns:
- branche07: values [RIN=BC Råstofindvinding og industri, VB=B Råstofindvinding, VCA=CA Føde-, drikke- og tobaksvareindustri, VCB=CB Tekstil- og læderindustri, VCC=CC Træ- og papirindustri, trykkerier, VCD=CD Olieraffinaderier mv., VCE=CE Kemisk industri, VCF=CF Medicinalindustri, VCG=CG Plast-, glas- og betonindustri, VCH=CH Metalindustri, VCI=CI Elektronikindustri, VCJ=CJ Fremst. af elektrisk udstyr, VCK=CK Maskinindustri, VCL=CL Transportmiddelindustri, VCM=CM Møbel- og anden industri mv.]
- enhed: values [GJFAK=Faktisk forbrug (1.000 GJ (gigajoule)), PCTAEND=Ændring i forhold til for to år siden (pct.)]
- tid: date range 2012-01-01 to 2024-01-01

notes:
- enhed is a measurement selector — every branche/tid combination appears twice: GJFAK (faktisk forbrug i 1.000 GJ) and PCTAEND (ændring ift. for to år siden i pct.). Always filter to one: WHERE enhed = 'GJFAK' for energy amounts, WHERE enhed = 'PCTAEND' for growth rates. Never sum across both.
- branche07=RIN is the aggregate for all of BC (Råstofindvinding og industri). Filter it out when summing individual branches to avoid double-counting: WHERE branche07 != 'RIN'.
- Data covers 2012-2024 in 2-year intervals (biennial survey), so tid has values 2012, 2014, 2016…