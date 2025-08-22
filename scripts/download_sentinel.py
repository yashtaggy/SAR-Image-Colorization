# scripts/download_sentinel.py
import ee
import json
import argparse

# ---------------------------
# Initialize Earth Engine
# ---------------------------
ee.Initialize(project="eighth-parity-455109-a1")   # <-- replace with your GCP project ID

# ---------------------------
# CLI Arguments
# ---------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--dataset", type=str, choices=["sentinel1", "sentinel2"], required=True,
                    help="Which dataset to download: sentinel1 (SAR) or sentinel2 (Optical)")
parser.add_argument("--start", type=str, default="2023-01-01", help="Start date (YYYY-MM-DD)")
parser.add_argument("--end", type=str, default="2023-12-31", help="End date (YYYY-MM-DD)")
parser.add_argument("--scale", type=int, default=30, help="Pixel size in meters")
args = parser.parse_args()

# ---------------------------
# Load AOI from GeoJSON
# ---------------------------
with open("data/processed/maharashtra.geojson") as f:
    geo = json.load(f)

fc = ee.FeatureCollection(geo)
aoi = fc.geometry()

# ---------------------------
# Select Dataset
# ---------------------------
if args.dataset == "sentinel2":
    # Optical: RGB bands only, harmonized collection
    img = (ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
           .filterBounds(aoi)
           .filterDate(args.start, args.end)
           .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10))
           .select(["B2", "B3", "B4"])   # RGB
           .median()
           .clip(aoi))
    description = "S2_Maharashtra"

elif args.dataset == "sentinel1":
    # SAR: VV + VH polarizations
    img = (ee.ImageCollection("COPERNICUS/S1_GRD")
           .filterBounds(aoi)
           .filterDate(args.start, args.end)
           .filter(ee.Filter.eq("instrumentMode", "IW"))
           .filter(ee.Filter.listContains("transmitterReceiverPolarisation", "VV"))
           .filter(ee.Filter.listContains("transmitterReceiverPolarisation", "VH"))
           .select(["VV", "VH"])
           .median()
           .clip(aoi))
    description = "S1_Maharashtra"

# ---------------------------
# Export to Google Drive
# ---------------------------
task = ee.batch.Export.image.toDrive(
    image=img,
    description=description,
    folder="SAR_project",
    fileNamePrefix=description,
    region=aoi,
    scale=args.scale,
    crs="EPSG:4326",
    maxPixels=1e13
)
task.start()

print(f"[INFO] Export started → Google Drive/SAR_project/{description}")
