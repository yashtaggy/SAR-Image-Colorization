import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import numpy as np
import os

input_dir = "data/raw/sentinel1"
output_dir = "data/interim/sentinel1"
os.makedirs(output_dir, exist_ok=True)

for fname in os.listdir(input_dir):
    if fname.endswith(".tif"):
        in_fp = os.path.join(input_dir, fname)
        out_fp = os.path.join(output_dir, fname.replace(".tif", "_std.tif"))

        with rasterio.open(in_fp) as src:
            transform, width, height = calculate_default_transform(
                src.crs, "EPSG:4326", src.width, src.height, *src.bounds, resolution=10
            )
            kwargs = src.meta.copy()
            kwargs.update({
                "crs": "EPSG:4326",
                "transform": transform,
                "width": width,
                "height": height
            })

            data = src.read()  # all bands (VV, VH)
            data = data.astype("float32")
            data = (data - data.min()) / (data.max() - data.min() + 1e-6)  # normalize

            with rasterio.open(out_fp, "w", **kwargs) as dst:
                dst.write(data)

        print(f"[OK] Preprocessed {fname} → {out_fp}")
