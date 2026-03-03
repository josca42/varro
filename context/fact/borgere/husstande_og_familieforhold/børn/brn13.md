table: fact.brn13
description: Børn efter område, voksne i bopælsfamilien , bopælsfamilietype, voksne i samværsfamilien  , samværsfamilietype, alder og tid
measure: indhold (unit Antal)
columns:
- omr20: join dim.nuts on omr20=kode; levels [1, 3]
- voksbofam: values [0=Udeboende, 1=Begge forældre, 2=Enlig mor, 3=Mor og partner, 4=Enlig far, 5=Far og partner]
- bofamtyp: values [1=Ægtepar med forskelligt køn, 6=Ægtepar med samme køn, 2=Registreret partnerskab, 3=Samlevende par, 4=Samboende par, 5=Enlig]
- voksamfam: values [1=Begge forældre, 2=Enlig mor, 3=Mor og partner, 4=Enlig far, 5=Far og partner, 99=Ingen samværsfamilie]
- samfamtyp: values [1=Ægtepar med forskelligt køn, 6=Ægtepar med samme køn, 2=Registreret partnerskab, 3=Samlevende par, 4=Samboende par, 5=Enlig, 99=Ingen samværsfamilie]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år, 5=5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år, 15=15 år, 16=16 år, 17=17 år]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/nuts.md
notes:
- omr20 has three groups of values: '0' (national total, not in dim.nuts — query directly with omr20='0'), niveau 1 (5 regioner), and niveau 3 (99 kommuner). When joining dim.nuts, filter to one niveau to avoid double-counting.
- This table tracks both the home address family (bopælsfamilien) and the custody/access family (samværsfamilien) for each child. It is the richest source for questions about custody arrangements.
- voksbofam=0 means "Udeboende" — the child is not registered as living with any family (e.g., in care). voksamfam=99 / samfamtyp=99 means no custody family at all.
- bofamtyp describes the couple type of the home family; samfamtyp describes the couple type of the custody family. These are independent of voksbofam/voksamfam (which describe the adult arrangement).
- alder covers only 0–17.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omr20=dim_kode. Exclude omr20=0.
