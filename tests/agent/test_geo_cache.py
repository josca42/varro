from __future__ import annotations

import importlib

import geopandas as gpd

from varro.config import GEO_DIR


def _geo_cache_module():
    module = importlib.import_module("varro.agent.utils")
    module._load_geo.cache_clear()
    return module


def test_get_geo_caches_by_layer_and_reads_from_geo_dir(monkeypatch):
    module = _geo_cache_module()
    read_paths = []
    cached = gpd.GeoDataFrame({"dim_kode": [1], "navn": ["A"]}).set_index("dim_kode")

    def fake_read_parquet(path):
        read_paths.append(path)
        return cached

    monkeypatch.setattr(module.gpd, "read_parquet", fake_read_parquet)

    first = module.get_geo("kommuner")
    second = module.get_geo("kommuner")

    assert read_paths == [GEO_DIR / "kommuner.parquet"]
    assert first.equals(cached)
    assert second.equals(cached)
    assert first is not cached
    assert second is not cached


def test_get_geo_returns_new_wrapper_to_protect_cached_object(monkeypatch):
    module = _geo_cache_module()
    cached = gpd.GeoDataFrame({"dim_kode": [1], "navn": ["A"]}).set_index("dim_kode")

    monkeypatch.setattr(module.gpd, "read_parquet", lambda _: cached)

    first = module.get_geo("regioner")
    first["extra"] = 1
    second = module.get_geo("regioner")

    assert "extra" not in second.columns
    assert "extra" not in module._load_geo("regioner").columns
