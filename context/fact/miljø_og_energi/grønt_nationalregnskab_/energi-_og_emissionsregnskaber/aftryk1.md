table: fact.aftryk1
description: Klimaaftryk (eksperimentel statistik) efter anvendelsestyper, udledende brancher, udledende lande og tid
measure: indhold (unit Ton CO2-ækvivalenter)
columns:
- anvendtype: values [IEA=INDENLANDSK ENDELIG ANVENDELSE I ALT (KLIMAAFTRYKKET), CPT=HUSHOLDNINGERNES FORBRUG I ALT, CPA=A Fødevarer, CPB=B Drikkevarer og tobak mv., CPC=C Beklædning og fodtøj, CPD=D Boligbenyttelse, CPE=E Elektricitet, gas og andet brændsel, CPF=F Boligudstyr, husholdningsudstyr og vedligholdelse heraf, CPG=G Medicin, lægeudgifter o.l., CPH=H Anskaffelse af køretøjer, CPI=I Anden transport og kommunikation, CPJ=J Fritidsudstyr, underholdning og rejser, CPK=K Andre varer og tjenester, NPISH=NON-PROFIT INSTITUTIONER RETTET MOD HUSHOLDNINGER (NPISH), CO=OFFENTLIGT FORBRUG, BI=BRUTTOINVESTERINGER MV., E6000=EKSPORT (Ikke med i KLIMAAFTRYKKET)]
- udledbranche: join dim.nr_branche on udledbranche=kode [approx]
- udledland: join dim.lande_uhv on udledland=kode [approx]; levels [4]
- tid: date range 1990-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md, /dim/nr_branche.md

notes:
- Experimental statistics — climate footprint attributed to Danish final demand, including embedded emissions from imports. Very different concept from drivhus (which uses the production/economy principle).
- udledbranche joins dim.nr_branche using: REPLACE(REPLACE(f.udledbranche, 'V', ''), '_', '-') = TRIM(d.kode). MTOT, MHUSHOLD are special aggregates not in dim.
- udledland joins dim.lande_uhv at niveau=4 (individual countries). Unmatched codes are aggregate groups not in the dim: DK=Denmark, ROW=rest of world, T=total, WA/WE/WL/WM/WF=world region aggregates. Use ColumnValues("lande_uhv", "titel") to browse available countries.
- anvendtype is the Danish demand category driving the footprint. IEA=total domestic final demand (the "climate footprint"); E6000=exports (excluded from footprint). CPT=total household consumption; CPA...CPK are COICOP sub-categories — don't mix with CPT.
- For total climate footprint: WHERE anvendtype='IEA' AND udledbranche='MTOT' AND udledland='T' — all emissions from Danish final demand regardless of where they occur.
- indhold is in Ton CO2-equivalents (not 1.000 ton like drivhus). Ends at 2023.