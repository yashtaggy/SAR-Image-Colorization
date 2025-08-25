import rasterio, glob, os
from rasterio.enums import Resampling

input_dir = "data/raw/sentinel2/"
output_dir = "data/interim/sentinel2/"
os.makedirs(output_dir, exist_ok=True)

for file in glob.glob(input_dir + "*.tif"):
    with rasterio.open(file) as src:
        profile = src.profile
        profile.update(count=3, dtype="uint16")

        # Read RGB bands only
        data = src.read([1, 2, 3], out_dtype="uint16", resampling=Resampling.bilinear)

        out_file = os.path.join(output_dir, os.path.basename(file).replace(".tif", "_std.tif"))
        with rasterio.open(out_file, "w", **profile) as dst:
            dst.write(data)

        print(f"[OK] Preprocessed S2 → {out_file}")
