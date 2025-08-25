# scripts/tile_dataset.py
import rasterio
import numpy as np
import os
from rasterio.windows import Window

infile = "data/processed/Collocated_clean.tif"
out_dir = "data/tiles"
os.makedirs(out_dir, exist_ok=True)

tile_size = 256

with rasterio.open(infile) as src:
    for i in range(0, src.height, tile_size):
        for j in range(0, src.width, tile_size):
            window = Window(j, i, tile_size, tile_size)
            transform = src.window_transform(window)
            data = src.read(window=window)

            if data.shape[1] == tile_size and data.shape[2] == tile_size:
                out_path = os.path.join(out_dir, f"tile_{i}_{j}.tif")
                profile = src.profile
                profile.update({
                    "height": tile_size,
                    "width": tile_size,
                    "transform": transform
                })
                with rasterio.open(out_path, "w", **profile) as dst:
                    dst.write(data)
