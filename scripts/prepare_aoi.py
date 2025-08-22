import geopandas as gpd

# Load India states shapefile
gdf = gpd.read_file("data/raw/shapefiles/gadm41_IND_1.shp")

# Extract Maharashtra
maha = gdf[gdf["NAME_1"] == "Maharashtra"]

# Save as GeoJSON for Earth Engine
output_path = "data/raw/shapefiles/maharashtra.geojson"
maha.to_file(output_path, driver="GeoJSON")

print(f"[INFO] Saved Maharashtra AOI as {output_path}")
