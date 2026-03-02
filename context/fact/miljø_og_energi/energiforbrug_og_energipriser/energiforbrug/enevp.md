table: fact.enevp
description: Varmepumper i råstofindvinding og industri efter branche (DB07), nøgletal og tid
measure: indhold (unit -)
columns:
- branche07: values [RIN=BC Råstofindvinding og industri, VB=B Råstofindvinding, VCA=CA Føde-, drikke- og tobaksvareindustri, VCB=CB Tekstil- og læderindustri, VCC=CC Træ- og papirindustri, trykkerier, VCD=CD Olieraffinaderier mv., VCE=CE Kemisk industri, VCF=CF Medicinalindustri, VCG=CG Plast-, glas- og betonindustri, VCH=CH Metalindustri, VCI=CI Elektronikindustri, VCJ=CJ Fremst. af elektrisk udstyr, VCK=CK Maskinindustri, VCL=CL Transportmiddelindustri, VCM=CM Møbel- og anden industri mv.]
- bnogle: values [PNR=Arbejdssteder med varmepumpe (antal), SAML=Samlet kapacitet (kW), PROC=Kapactitet anvendt til proces (kW), RUMV=Kapacitet anvendt til rumvarme (kW), PLUD=Kapacitet efter placering - udendørs (kW), PLIN=Kapacitet efter placering - indendørs (kW), VPEL=Elforbrug til varmepumper (MWh)]
- tid: date range 2020-01-01 to 2024-01-01

notes:
- bnogle encodes 7 fundamentally different metrics with incompatible units. Never sum across bnogle values. Pick the metric you need: PNR (antal arbejdssteder, count), SAML (samlet kapacitet kW), PROC (proceskapacitet kW), RUMV (rumvarmekap. kW), PLUD (udendørs kapac. kW), PLIN (indendørs kapac. kW), VPEL (elforbrug MWh).
- branche07=RIN is the industry-wide aggregate. Filter it out when summing across individual branches: WHERE branche07 != 'RIN'.
- Coverage is sparse: PLIN/PLUD only have 1 row per branch (single year), PNR/SAML/PROC/RUMV have 3, VPEL has 2. Not all metrics are available for all years.