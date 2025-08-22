# scripts/prepare_aoi.py
import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon

IN_PATH = "data/raw/shapefiles/maharashtra_natural.shp"  # <-- adjust if needed
OUT_PATH = "data/processed/maharashtra.geojson"

def fix_invalid(gdf):
    """Make geometries valid (Shapely 2.0 make_valid if available, else buffer(0))."""
    try:
        from shapely.validation import make_valid  # Shapely >= 2.0
        gdf["geometry"] = gdf.geometry.apply(make_valid)
    except Exception:
        # Fallback: zero-width buffer often fixes self-intersections
        gdf["geometry"] = gdf.buffer(0)
    return gdf

def main():
    gdf = gpd.read_file(IN_PATH)
    print("Columns:", list(gdf.columns))
    print("CRS before:", gdf.crs)

    # Ensure we have a CRS; use WGS84 (EPSG:4326) for GEE
    if gdf.crs is None:
        gdf = gdf.set_crs(epsg=4326)
    else:
        gdf = gdf.to_crs(epsg=4326)

    # Fix invalid geoms
    invalid_before = (~gdf.is_valid).sum()
    print("Invalid geometries before fix:", invalid_before)
    gdf = fix_invalid(gdf)
    invalid_after = (~gdf.is_valid).sum()
    print("Invalid geometries after fix:", invalid_after)

    # (Optional) explode in case of mixed multi-geom types
    gdf = gdf.explode(index_parts=False, ignore_index=True)

    # Dissolve all into a single boundary
    merged = gdf.geometry.unary_union  # shapely geometry

    # Safety: wrap into a GeoDataFrame
    if isinstance(merged, (Polygon, MultiPolygon)):
        aoi = gpd.GeoDataFrame({"name": ["Maharashtra"]}, geometry=[merged], crs="EPSG:4326")
    else:
        raise ValueError("Unexpected merged geometry type.")

    # Final light topology clean
    aoi["geometry"] = aoi.buffer(0)

    # Save as GeoJSON for Earth Engine
    aoi.to_file(OUT_PATH, driver="GeoJSON")
    print(f"[INFO] Maharashtra AOI saved to {OUT_PATH}")

if __name__ == "__main__":
    main()
