import ee, geojson

# Your registered GCP project ID
PROJECT = "eighth-parity-455109-a1"

ee.Initialize(project=PROJECT)

# Load Maharashtra AOI
# Load Maharashtra AOI
with open("data/raw/shapefiles/maharashtra.geojson") as f:
    geo = geojson.load(f)

aoi = ee.Geometry(geo['features'][0]['geometry'])


# Sentinel-2 optical (2023, <20% clouds)
s2 = (ee.ImageCollection("COPERNICUS/S2")
      .filterBounds(aoi)
      .filterDate("2023-01-01", "2023-12-31")
      .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20)))

# Median composite
s2_img = s2.median().clip(aoi)

# Export to Google Drive
task = ee.batch.Export.image.toDrive(
    image=s2_img.select(["B2","B3","B4"]),
    description="S2_Maharashtra_2023",
    folder="SAR_project",
    fileNamePrefix="s2_maha_2023",
    scale=10,
    region=aoi,    
    maxPixels=1e13
)
task.start()


print("[INFO] Export started → Check Google Drive (SAR_project folder).")
