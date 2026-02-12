# Plan: GeoJSON Map Visualization Integration

## Research Findings

### GeoJSON Files Available (`mnt/admin_regions/`)

| File | Features | Coord Points | Useful for Stats? |
|---|---|---|---|
| `kommuner.geojson` | 99 | 1,620,777 | **High** — matches dim.nuts niveau 3 |
| `regioner.geojson` | 5 | 1,153,940 | **High** — matches dim.nuts niveau 1 |
| `landsdele.geojson` | 11 | 1,191,655 | **High** — matches dim.nuts niveau 2 |
| `politikredse.geojson` | 12 | ~90MB | Medium — matches dim.politikredse |
| Others (postnumre, sogne, valgkredse, etc.) | — | — | Low/None — no matching dim tables |

### ID Mapping: GeoJSON → dim.nuts

`dim.nuts.kode` is `smallint`. The GeoJSON files use different ID schemes:

**Kommuner** (niveau 3): GeoJSON `properties.kode` = `"0101"` → dim.nuts kode = `101`
- Transform: `int(geojson_kode)` — strip leading zero

**Regioner** (niveau 1): GeoJSON `properties.kode` = `"1081"` → dim.nuts kode = `81`
- Transform: `int(geojson_kode) - 1000`

**Landsdele** (niveau 2): GeoJSON `properties.nuts3` = `"DK011"` → dim.nuts kode = `1`
- No arithmetic transform possible. Requires a name-based lookup:

| GeoJSON nuts3 | Name | dim.nuts kode |
|---|---|---|
| DK011 | Byen København | 1 |
| DK012 | Københavns omegn | 2 |
| DK013 | Nordsjælland | 3 |
| DK014 | Bornholm | 4 |
| DK021 | Østsjælland | 5 |
| DK022 | Vest- og Sydsjælland | 6 |
| DK031 | Fyn | 7 |
| DK032 | Sydjylland | 8 |
| DK041 | Vestjylland | 10 |
| DK042 | Østjylland | 9 |
| DK050 | Nordjylland | 11 |

### Fact Table Coverage

| Column | Fact Tables | Joins To | Levels |
|---|---|---|---|
| `omrade` | **344** | dim.nuts | 1, 2, 3 (varies) |
| `kommunedk` | 27 | dim.nuts | 3 |
| `region` | 22 | dim.nuts | 1 |
| `komk` | 20 | dim.nuts | 1, 3 |
| `bopomr` | 19 | dim.nuts | 1, 2, 3 |
| `landdel` | 8 | dim.nuts | 2 |
| `regi07` | 7 | dim.nuts | 1 |

**~450+ fact tables** have geographic breakdowns that could be visualized on a map.

### Current Viz Stack
- Plotly is the primary charting library (already installed)
- Plotly has built-in `px.choropleth_mapbox` for GeoJSON choropleth maps
- No additional geo libraries needed
- Figures: PNG in chat, interactive HTML in dashboards

### Problem: File Size
The raw GeoJSON files are 73–223 MB each (~1M+ coordinate points) due to high-resolution coastlines. They must be simplified for web rendering.

---

## Implementation Plan

### Step 1: Pre-process GeoJSON files

Create a script (`scripts/simplify_geojson.py` or similar) that:

1. **Simplifies geometries** using `shapely.simplify()` (with `preserve_topology=True`). Target ~30-50x reduction in coordinate count to bring files to ~2-5 MB.

2. **Adds a `dim_kode` integer property** to each feature that directly matches `dim.nuts.kode`:
   - kommuner: `dim_kode = int(properties["kode"])`
   - regioner: `dim_kode = int(properties["kode"]) - 1000`
   - landsdele: `dim_kode = NUTS3_TO_KODE[properties["nuts3"]]`

3. **Strips unnecessary properties** — only keep `dim_kode` and `navn`.

4. **Outputs to `mnt/admin_regions/simplified/`**:
   - `kommuner.geojson` (~2-5 MB)
   - `regioner.geojson` (~0.5 MB)
   - `landsdele.geojson` (~1 MB)

**Deps:** `geopandas`, `shapely` (likely already available, otherwise add to pyproject.toml)

### Step 2: Symlink into agent sandbox

In `varro/agent/workspace.py` (`ensure_user_workspace`), add a symlink so the simplified GeoJSON is available at `/geo/` in the sandbox:

```
/geo/
├── kommuner.geojson
├── regioner.geojson
└── landsdele.geojson
```

Follows the existing pattern for symlinking read-only shared data.

### Step 3: Pre-load GeoJSON in Jupyter kernel

In `varro/agent/ipython_shell.py` initialization, pre-load the data:

```python
import json as _json
_geo = {}
for _name in ["kommuner", "regioner", "landsdele"]:
    with open(f"/geo/{_name}.geojson") as _f:
        _geo[_name] = _json.load(_f)
```

Makes `_geo["kommuner"]` etc. immediately available without file I/O during analysis.

### Step 4: Add map skill documentation

Create `/skills/maps/SKILL.md` with:

1. **When to use maps** — data broken down by kommune/region/landsdel
2. **Available GeoJSON** — the three files and their feature counts
3. **Choropleth pattern**:
```python
fig = px.choropleth_mapbox(
    df,
    geojson=_geo["kommuner"],
    locations="omrade",
    featureidkey="properties.dim_kode",
    color="indhold",
    hover_name="titel",
    mapbox_style="carto-positron",
    center={"lat": 56.0, "lon": 10.5},
    zoom=5.5,
)
```
4. **Which GeoJSON for which level** — kommuner for niveau 3, landsdele for niveau 2, regioner for niveau 1
5. **Common patterns** — joining dim.nuts for hover labels, handling the `0` (all Denmark) aggregate row

### Step 5: Update agent system prompt

Add to the `<environment>` file tree in `rigsstatistiker.j2`:

```
├── geo/               # Simplified GeoJSON for map visualizations
│   ├── kommuner.geojson
│   ├── regioner.geojson
│   └── landsdele.geojson
```

And a brief note:

```
**geo/** — Pre-simplified GeoJSON for choropleth maps. Pre-loaded as `_geo["kommuner"]`,
`_geo["regioner"]`, `_geo["landsdele"]`. Each feature has `dim_kode` matching `dim.nuts.kode`.
Read `/skills/maps/SKILL.md` before creating map visualizations.
```

---

## What This Enables

After implementation, the agent can create choropleth maps like this in ~3 lines:

```python
# Query data by municipality
df = Sql("SELECT f.omrade, f.indhold, d.titel FROM fact.folk1c f JOIN dim.nuts d ON f.omrade = d.kode WHERE d.niveau = 3 AND f.tid = '2024-01-01' AND f.kon = 'TOT'", "pop")

# Visualize on map
fig = px.choropleth_mapbox(pop, geojson=_geo["kommuner"], locations="omrade",
    featureidkey="properties.dim_kode", color="indhold", hover_name="titel",
    mapbox_style="carto-positron", center={"lat": 56.0, "lon": 10.5}, zoom=5.5,
    title="Population by Municipality")
```

This works for any of the ~450 fact tables with geographic columns.
