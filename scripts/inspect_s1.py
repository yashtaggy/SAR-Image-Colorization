import rasterio, glob, os
import numpy as np

input_dir = "data/interim/sentinel1/"

for file in glob.glob(os.path.join(input_dir, "*.tif")):
    with rasterio.open(file) as src:
        print(f"\nFile: {file}")
        print(f" Bands: {src.count}")
        print(f" CRS: {src.crs}")
        print(f" Shape (H, W): {src.height}, {src.width}")

        for b in range(1, src.count + 1):
            band = src.read(b, masked=True)
            print(f"  Band {b} → min: {np.nanmin(band)}, max: {np.nanmax(band)}, mean: {np.nanmean(band)}")
