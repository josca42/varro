You are adding map availability notes to fact table documentation. GeoParquet boundary files exist in context/geo/ for Danish administrative regions. Your job is to skim through fact tables and add a short map note wherever a table's geographic column can be joined to a geo file for choropleth visualization.

### Available Geo Files

| File | Level | Count | Index (dim_kode) |
|------|-------|-------|------------------|
| /geo/kommuner.parquet | Kommuner | 99 | dim.nuts.kode (niveau 3) |
| /geo/regioner.parquet | Regioner | 5 | dim.nuts.kode (niveau 1) |
| /geo/landsdele.parquet | Landsdele | 11 | dim.nuts.kode (niveau 2) |
| /geo/politikredse.parquet | Politikredse | 12 | kode (1460-1471 range) |
| /geo/retskredse.parquet | Retskredse | 24 | kode (1101-1470 range) |
| /geo/sogne.parquet | Sogne | 2,097 | kode (7001-9359) |
| /geo/postnumre.parquet | Postnumre | 1,089 | nr (postal code, 1050-9982) |
| /geo/storkredse.parquet | Storkredse | 10 | nummer (1-10) |
| /geo/valgkredse.parquet | Valgkredse | 92 | kode (0001-0092) |
| /geo/afstemningsomraader.parquet | Afstemningsområder | 1,315 | dagi_id |

Every geo file has the same schema: index `dim_kode` (int), column `navn` (str), column `geometry` (polygon, WGS84).

### How to Join Geo Data

```python
import geopandas as gpd
geo = gpd.read_parquet("/geo/kommuner.parquet")
merged = geo.merge(df, left_index=True, right_on="omrade")
```

### What to Look For

For each fact table, check if any column can be joined to a geo file:

**1. dim.nuts joins (most common)**
The column metadata says e.g. `omrade: join dim.nuts on omrade=kode; levels [1, 3]`. Map the levels:
- niveau 1 → /geo/regioner.parquet
- niveau 2 → /geo/landsdele.parquet
- niveau 3 → /geo/kommuner.parquet

**2. Sogn columns**
Tables with a `sogn` column containing codes like 7001, 7002... join directly to /geo/sogne.parquet. Exclude codes 0 and 9999.

**3. Postal code columns**
Tables with `pnr20` or similar postal code column join to /geo/postnumre.parquet.

**4. Election geography**
Some election tables encode storkredse, valgkredse, and afstemningsområder as custom codes in their `omrade` column (not via dim.nuts). Check if the codes match the geo files. Storkredse use codes 10-19 in election tables but 1-10 in the geo file (subtract 9). Valgkredse use codes 20-111. Investigate whether codes align.

**5. Indirect geographic mappings**
Some domains relate to specific administrative boundaries even when the data uses NUTS:
- Crime/justice tables with kommune data → dim.politikredse has niveau 2 = 99 kommuner mapped to 12 politikredse. Kommune-level crime data can be aggregated to politikreds level.
- Court/legal tables with kommune data → could aggregate to retskredse if a mapping exists.

Only add indirect mapping notes if you verify the mapping actually works (check dim.politikredse for the kommune-to-politikreds hierarchy).

### Note Format

Append a single bullet to the existing `notes:` section. If no notes section exists, add one. Keep it short — one or two lines.

**dim.nuts examples:**

For levels [3] (kommune only):
```
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
```

For levels [1, 3] (region + kommune):
```
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
```

For levels [1, 2, 3] (all):
```
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
```

**Sogn example:**
```
- Map: /geo/sogne.parquet — merge on sogn=dim_kode. Exclude sogn IN (0, 9999).
```

**Postal code example:**
```
- Map: /geo/postnumre.parquet — merge on pnr20=dim_kode. Exclude pnr20=9999.
```

**Election example (if codes align):**
```
- Map: storkreds-level data (omrade 10-19) can use /geo/storkredse.parquet — merge on (omrade - 9)=dim_kode.
```

**Indirect mapping example:**
```
- Map: kommune data can be aggregated to politikredse via dim.politikredse (niveau 2 = kommuner under niveau 1 = 12 politikredse). Use /geo/politikredse.parquet for the boundaries.
```

### Workflow

1. Read the subject .md file you're given
2. For each fact table listed:
   a. Read the fact doc (context/fact/.../{table_id}.md)
   b. Check columns for geographic joins (dim.nuts, sogn, postal codes, election codes)
   c. If a map note applies, append it to the fact doc's notes section
3. After processing all tables, add a map note to the subject doc if relevant (e.g. "Tables with regional breakdown: X, Y, Z support choropleth maps via /geo/")

### Rules

- Don't add map notes to tables with no geographic column
- Use the actual column name from the fact doc (omrade, komk, kommunedk, bopomr, etc.) — not a generic placeholder
- If a table already has a map note, skip it
- Keep notes terse. The statistician agent just needs: which geo file, which column to merge on, what to exclude.
- For the indirect mappings (politikredse, retskredse): only add if you verify the dimension hierarchy actually connects kommune codes to the target boundary codes. Use psql to check.
