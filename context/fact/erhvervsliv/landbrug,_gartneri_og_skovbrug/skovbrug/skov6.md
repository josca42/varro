table: fact.skov6
description: Hugsten i skove og plantager i Danmark efter område, træsort, areal og tid
measure: indhold (unit 1.000 m3)
columns:
- omrade: values [000=Hele landet, L4=Øerne, L3=Jylland]
- traesort: values [00010=Hugst i alt, 00020=Gavntræ i alt, 00030=Brænde i alt, 00040=Skovflis i alt, 00090=Energitræ som flis i alt ... 00088=Nåletræ - Andet gavntræ, NALBRAEND=Nåletræ - Brænde, NALFLIS=Nåletræ - Skovflis, 00170=Nåletræ - Energitræ som flis, 00180=Nåletræ - Energitræ som rundtræ]
- areal1: values [4=Alle bedrifter, 1=Bedrifter med 0-49,9 ha skov, 2=Bedrifter med 50-249,9 ha skov, 3=Bedrifter med 250 ha skov eller mere, 5=Bedrifter med 0-99,9 ha skov, 6=Bedrifter med 100-999,9 ha skov, 7=Bedrifter med 1000 ha skov eller mere]
- tid: date range 1990-01-01 to 2023-01-01

notes:
- omrade uses the same 3 codes as skov55a: 000=Hele landet, L3=Jylland, L4=Øerne. No regional breakdown beyond this.
- areal1 contains two overlapping farm-size grouping schemes that must not be summed together. Scheme A: 1=(0–49.9 ha), 2=(50–249.9 ha), 3=(250+ ha). Scheme B: 5=(0–99.9 ha), 6=(100–999.9 ha), 7=(1000+ ha). Code 4=Alle bedrifter is the total. Use code 4 for the national total, and pick either [1,2,3] or [5,6,7] for a complete breakdown — never sum all seven.
- Annual data 1990–2023 with no gaps. This makes skov6 the only table with continuous hugst data for 1990–2005 (skov55 only starts 2006, skov55a ends 1989).
- traesort hierarchy is the same as skov55 — see skov55 notes. Use 00010 for total hugst across all tree species and product types.