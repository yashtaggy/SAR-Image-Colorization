import ee, json
ee.Initialize(project="eighth-parity-455109-a1")

# Load AOI
with open("data/processed/maharashtra.geojson") as f:
    geo = json.load(f)
aoi = ee.Geometry(geo['features'][0]['geometry'])

# Split into smaller tiles (2x2 grid)
tiles = aoi.coveringGrid(ee.Projection("EPSG:4326"), 200000)

collection = (ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
              .filterBounds(aoi)
              .filterDate("2023-01-01", "2023-12-31")
              .select(["B2","B3","B4"]))  # Only RGB bands

image = collection.median().clip(aoi)

# Export each tile separately
task_list = []
for i in range(tiles.size().getInfo()):
    tile = ee.Feature(tiles.toList(tiles.size()).get(i)).geometry()
    task = ee.batch.Export.image.toDrive(
        image=image.clip(tile),
        description=f"S2_tile_{i+1}",
        folder="SAR_project",
        fileNamePrefix=f"S2_tile_{i+1}",
        region=tile.coordinates().getInfo(),
        scale=10,   # 10m resolution for RGB
        crs="EPSG:4326",
        maxPixels=1e13
    )
    task.start()
    task_list.append(f"Started task for S2_tile_{i+1}")

print("\n".join(task_list))
