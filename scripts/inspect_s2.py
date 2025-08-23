import rasterio
import numpy as np

check_file = "data/interim/sentinel2/S2_tile_1_std.tif"

with rasterio.open(check_file) as src:
    print(f"File: {check_file}")
    print(f"Bands: {src.count}")
    print(f"CRS: {src.crs}")
    print(f"Shape (H, W): {src.height}, {src.width}")

    for i in range(1, src.count + 1):
        band = src.read(i)
        print(f" Band {i} → min: {band.min()}, max: {band.max()}, mean: {band.mean()}")
