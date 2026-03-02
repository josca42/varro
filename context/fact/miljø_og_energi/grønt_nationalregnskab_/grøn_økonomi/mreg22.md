table: fact.mreg22
description: Offentlig miljøbeskyttelse efter miljøformål, udgifter/indtægter, sektor og tid
measure: indhold (unit 1.000 kr.)
columns:
- kategori: join dim.cepa on kategori=kode::text [approx]
- ui: values [U2=1.1. Aflønning af ansatte, U3=1.2. Forbrug i produktionen, U31=1.3. Andre produktionsskatter, U4=1.4. Renter, U41=1.5. Subsidier, U5=1.6. Løbende overførsler, U1=1.7. Driftsudgifter i alt (1+2+3+4+5+6), U121=1.8. Faste bruttoinvesteringer, U122=1.9. Andre kapitaludgifter, U120=1.10. Kapitaludgifter i alt (8+9), U=1.11. Drifts- og kapitaludgifter i alt (7+10), I12=2.1. Salg af varer og tjenester, I13=2.2. Renter mv., I14=2.3. Andre løbende overførsler, I1=2.4. Driftsindtægter i alt (1+2+3), I2=2.5. Kapitalindtægter i alt, I=2.6. Drifts- og kapitalindtægter i alt (4+5)]
- sektor: values [A0=A. Den offentlige sektor i alt, B=B. Offentlige virksomheder, C=C. Offentlig forvaltning og service, C1=C.1 Stat, C2=C.2 Regioner/amter, C3=C.3 Kommuner]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/cepa.md

notes:
- kategori uses CEPA-prefixed codes (CEPA1–CEPA9 + TOT) but dim.cepa uses plain numeric codes (1–9). The documented join won't work as-is. Correct join: JOIN dim.cepa d ON REPLACE(f.kategori, 'CEPA', '') = d.kode::text AND d.niveau = 1. TOT has no dim match (it's the grand total row).
- dim.cepa has 3 levels (niveau 1–3). mreg22.kategori only uses niveau 1 (9 CEPA categories + TOT) — no sub-level detail in this table.
- ui is a hierarchical expenditure/revenue breakdown: U = total drifts- og kapitaludgifter, U1 = driftsudgifter i alt, I = total drifts- og kapitalindtægter, I1 = driftsindtægter i alt. Filter to one ui value. To get net cost: U minus I. For simple total spending: WHERE ui = 'U'.
- sektor is hierarchical: A0 = den offentlige sektor i alt, B = offentlige virksomheder, C = offentlig forvaltning og service (C1=Stat, C2=Regioner, C3=Kommuner). A0 includes B and C. Don't sum A0 + C or B + C1 etc.
- indhold is in 1.000 kr. (divide by 1000 for Mio. kr. or 1.000.000 for Mia. kr.).