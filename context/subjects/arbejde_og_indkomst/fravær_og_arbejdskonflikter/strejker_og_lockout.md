<fact tables>
<table>
id: abst1
description: Arbejdsstandsninger efter branche, enhed og tid
columns: branche, enhed, tid (time), indhold (unit Antal)
tid range: 1996-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- abst1 is the only table — annual strikes/lockouts 1996–2024, broken down by sector (branche) and measure type (enhed).
- enhed must always be filtered to one value: 100=antal arbejdsstandsninger, 200=antal berørte ansatte, 300=antal tabte arbejdsdage. All three appear for every row; summing them together is meaningless.
- branche has two aggregate rows that cause double-counting: 0="I alt" (all sectors) and 4="Industri i alt" (sub-industries 6–18). Exclude both when summing across sectors: WHERE branche NOT IN (0, 4).
- No dimension table joins — branche codes and enhed codes are inline with labels in the fact doc.