import rasterio, glob, os
import numpy as np
from rasterio.enums import Resampling

input_dir = "data/raw/sentinel1/"
output_dir = "data/interim/sentinel1/"
os.makedirs(output_dir, exist_ok=True)

for file in glob.glob(input_dir + "*.tif"):
    with rasterio.open(file) as src:
        profile = src.profile
        profile.update(driver="GTiff", dtype="float32")

        # Read VV, VH bands
        data = src.read(out_dtype="float32", resampling=Resampling.bilinear)

        # Normalize (optional: log-scale SAR)
        data[data <= 0] = 1e-6
        data = 10 * np.log10(data)

        out_file = os.path.join(output_dir, os.path.basename(file).replace(".tif", "_std.tif"))
        with rasterio.open(out_file, "w", **profile) as dst:
            dst.write(data)

        print(f"[OK] Preprocessed S1 → {out_file}")
