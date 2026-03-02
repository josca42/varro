<fact tables>
<table>
id: hnr1
description: Syntetisk forhistorie for det aktuelle nationalregnskabs tal efter version, transaktion, prisenhed og tid
columns: version, transakt, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1930-01-01 to 2024-01-01
</table>
<table>
id: hnrb
description: Syntetisk forhistorie til aktuelle nationalregnskabstals befolkningstal efter version, population og tid
columns: version, popu, tid (time), indhold (unit 1.000)
tid range: 1870-01-01 to 2024-01-01
</table>
<table>
id: vhnr
description: Historiske nationalregnskabstal efter regime, transaktion, prisenhed og tid
columns: regime, transakt, prisenhed, tid (time), indhold (unit -)
tid range: 1870-01-01 to 1992-01-01
</table>
<table>
id: vhnrb
description: Historisk nationalregnskabs middelfolketal efter regime, population og tid
columns: regime, popu, tid (time), indhold (unit 1.000)
tid range: 1870-01-01 to 2019-01-01
</table>
</fact tables>

notes:
- Two conceptually distinct datasets live here: **synthetic unified history** (hnr1/hnrb) and **original historical regimes** (vhnr/vhnrb).
- Use **hnr1** when you want a single consistent time series applying current national accounts methodology back to 1930. It has no regime variation — one version, one prisenhed (løbende priser). BNP (transakt=101) is the only series going back to 1930; all others start 1966.
- Use **hnrb** for the population/employment counterpart to hnr1 (per-capita calculations). Coverage: POP from 1870, EMPM_DC from 1903, EMPM_NC only from 1971.
- Use **vhnr** when you need the original published figures from a specific historical accounting regime (e.g. the figures Denmark actually reported in 1960). Each regime has løbende priser (401) and growth rate pct (450) — these must never be mixed. The table covers 1870–1992.
- Use **vhnrb** for population figures matching a specific vhnr regime. Only 3 regimes are present: 218 (NR2014), 250 (Bjerke/Ussing 1958), 251 (Svend Aage Hansen 1983).
- hnr1/vhnr values diverge for overlapping years — this is expected and correct. They answer different questions: "what does current methodology say happened in 1950?" vs "what did Denmark officially report in 1950?"
- All tables: always filter to a single combination of (version/regime, transakt/popu, prisenhed) to get one time series.