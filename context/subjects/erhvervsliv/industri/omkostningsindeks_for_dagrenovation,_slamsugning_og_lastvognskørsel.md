<fact tables>
<table>
id: byg91
description: Omkostningsindeks for dagrenovation, slamsugning og lastvognskørsel efter indekstype, enhed og tid
columns: indekstype, tal, tid (time), indhold (unit Indeks)
tid range: 1997-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- Only one table (byg91). Quarterly cost indices for three waste/transport services: dagrenovation, slamsugning, lastvognskørsel — each available as index level, QoQ change (%), or YoY change (%).
- Always filter `tal`: `100`=index, `210`=QoQ%, `310`=YoY%. Omitting this silently mixes incompatible measure types.
- Time coverage varies by series: DAG/SLAM from 1997, LAST from 2021, fuel-excluded ("UB") variants from 2022K2, road-tax-excluded variants ("UV"/"UBV") only from 2025K1.