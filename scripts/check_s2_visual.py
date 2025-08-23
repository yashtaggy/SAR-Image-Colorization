import rasterio
import matplotlib.pyplot as plt
import numpy as np
import os

check_file = "data/interim/sentinel2/S2_tile_2_std.tif"  # pick one file

with rasterio.open(check_file) as src:
    print(f"File: {check_file}, Bands: {src.count}")
    img = src.read([1, 2, 3])  # R,G,B
    img = np.transpose(img, (1, 2, 0))  # reshape to HWC

# Stretch contrast a bit for display
img = (img - img.min()) / (img.max() - img.min())

plt.imshow(img)
plt.title("Sentinel-2 RGB Check")
plt.axis("off")
plt.show()
