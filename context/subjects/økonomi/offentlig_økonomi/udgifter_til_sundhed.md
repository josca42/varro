<fact tables>
<table>
id: sha1
description: Udgifter til sundhed efter funktion, aktør, finansieringskilde, prisenhed og tid
columns: funktion, aktoer, finanskilde1, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 2010-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Only one table (sha1) covering annual health expenditure 2010–2024 in mio. kr. (current prices only).
- sha1 has five dimensions: funktion (ICHA-HC health function), aktoer (ICHA-HP health provider), finanskilde1 (financing source), prisenhed (price unit — only ENH1), tid.
- The dim joins for funktion and aktoer require dot-stripping: the fact table codes drop dots (HC.1.3 → HC13). Use REPLACE(d.kode, '.', '') in all joins against dim.icha and dim.icha_hp.
- Both funktion and aktoer are 3-level hierarchies; always filter d.niveau to avoid double-counting. HCTOT and HPTOT are the grand-total rows for each.
- finanskilde1 is an inline 2-level hierarchy (HFTOT > HF1/HF2/HF3/HF4 > sub-codes like HF11/HF21/HF22). Filter to one level to avoid overcounting.
- A safe baseline filter for any single-dimension analysis: funktion='HCTOT' OR aktoer='HPTOT' OR finanskilde1='HFTOT' — hold the other three constant while breaking out the one you care about.