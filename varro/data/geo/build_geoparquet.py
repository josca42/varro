"""Build simplified GeoParquet files from raw GeoJSON admin regions.

Run once:  python -m varro.data.geo.build_geoparquet
"""

import geopandas as gpd
from pathlib import Path

from varro.config import GEO_DIR, DATA_DIR

RAW_DIR = DATA_DIR / "admin_regions"

LANDSDELE_NUTS3_TO_DIM_KODE = {
    "DK011": 1, "DK012": 2, "DK013": 3, "DK014": 4,
    "DK021": 5, "DK022": 6, "DK031": 7, "DK032": 8,
    "DK041": 10, "DK042": 9, "DK050": 11,
}

LAYERS = [
    {
        "name": "kommuner",
        "file": "kommuner.geojson",
        "dim_kode": lambda gdf: gdf["kode"].astype(int),
        "tolerance": 100,
    },
    {
        "name": "regioner",
        "file": "regioner.geojson",
        "dim_kode": lambda gdf: gdf["kode"].astype(int) - 1000,
        "tolerance": 200,
    },
    {
        "name": "landsdele",
        "file": "landsdele.geojson",
        "dim_kode": lambda gdf: gdf["nuts3"].map(LANDSDELE_NUTS3_TO_DIM_KODE),
        "tolerance": 150,
    },
    {
        "name": "politikredse",
        "file": "politikredse.geojson",
        "dim_kode": lambda gdf: gdf["kode"].astype(int) - 1459,
        "tolerance": 200,
    },
    {
        "name": "retskredse",
        "file": "retskredse.geojson",
        "dim_kode": lambda gdf: gdf["kode"].astype(int),
        "tolerance": 150,
    },
    {
        "name": "sogne",
        "file": "sogne.geojson",
        "dim_kode": lambda gdf: gdf["kode"].astype(int),
        "tolerance": 50,
    },
    {
        "name": "postnumre",
        "file": "postnumre.geojson",
        "dim_kode": lambda gdf: gdf["nr"].astype(int),
        "tolerance": 50,
    },
    {
        "name": "storkredse",
        "file": "storkredse.geojson",
        "dim_kode": lambda gdf: gdf["nummer"].astype(int),
        "tolerance": 200,
    },
    {
        "name": "valgkredse",
        "file": "valgkredse.geojson",
        "dim_kode": lambda gdf: gdf["kode"].astype(int),
        "tolerance": 100,
    },
    {
        "name": "afstemningsomraader",
        "file": "afstemningsomraader.geojson",
        "dim_kode": lambda gdf: gdf["dagi_id"].astype(int),
        "tolerance": 30,
    },
]


def build_layer(layer: dict) -> Path:
    gdf = gpd.read_file(RAW_DIR / layer["file"])

    gdf["dim_kode"] = layer["dim_kode"](gdf)
    gdf = gdf[["dim_kode", "navn", "geometry"]]

    gdf = gdf.to_crs(epsg=25832)
    gdf["geometry"] = gdf.geometry.simplify(tolerance=layer["tolerance"])
    gdf = gdf.to_crs(epsg=4326)

    gdf = gdf.set_index("dim_kode")

    out = GEO_DIR / f"{layer['name']}.parquet"
    gdf.to_parquet(out)
    size_mb = out.stat().st_size / 1024 / 1024
    print(f"  {out.name}: {len(gdf)} rows, {size_mb:.1f} MB")
    return out


def main():
    GEO_DIR.mkdir(parents=True, exist_ok=True)
    print("Building GeoParquet files...")
    for layer in LAYERS:
        build_layer(layer)
    print("Done.")


if __name__ == "__main__":
    main()
