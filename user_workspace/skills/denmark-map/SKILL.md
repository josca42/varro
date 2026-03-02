---
name: denmark-map
description: Create plotly choropleth maps of Danish administrative regions. Use when visualizing geographic data on a map.
---

# Denmark Map Plots

Create choropleth maps using GeoParquet boundary files at `/geo/`.

## Available Files

| File | Level | Count | dim_kode source |
|------|-------|-------|-----------------|
| `kommuner.parquet` | Kommuner | 99 | kode → dim.nuts.kode |
| `regioner.parquet` | Regioner | 5 | kode → dim.nuts.kode |
| `landsdele.parquet` | Landsdele | 11 | nuts3 → dim.nuts.kode |
| `politikredse.parquet` | Politikredse | 12 | kode → dim.politikredse.kode |
| `retskredse.parquet` | Retskredse | 24 | kode |
| `sogne.parquet` | Sogne | 2,097 | kode |
| `postnumre.parquet` | Postnumre | 1,089 | nr (postal code) |
| `storkredse.parquet` | Storkredse | 10 | nummer |
| `valgkredse.parquet` | Valgkredse | 92 | kode |
| `afstemningsomraader.parquet` | Afstemningsområder | 1,315 | dagi_id |

## Schema

Each file is a GeoParquet with:
- **Index**: `dim_kode` (int) — for kommuner/regioner/landsdele this matches `dim.nuts.kode`; other layers use their native ID (see table above)
- **navn**: Region/kommune name (str)
- **geometry**: Polygon boundaries in WGS84 (EPSG:4326)

## Add geo data

```python
import geopandas as gpd
geo = gpd.read_parquet("/geo/kommuner.parquet")
df = df[df["omrade"] != 0]  # drop whole-country aggregate
merged = geo.merge(df, left_index=True, right_on="omrade")
```

After merge, use `merged.index` for `locations` and `merged.geometry` for `geojson`.

## Plot map

Use `px.choropleth_map` with a tile basemap:

```python
fig = px.choropleth_map(
    merged,
    geojson=merged.geometry,
    locations=merged.index,
    color="indhold",
    hover_name="navn",
    map_style="carto-positron",
    center={"lat": 56.0, "lon": 10.5},
    zoom=5.5,
)
```

Denmark center: `lat=56.0, lon=10.5`, zoom `5.5` fits the mainland and islands. Bornholm (far east) may appear small — zoom `5.0` if it matters.