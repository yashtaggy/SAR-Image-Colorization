# scripts/normalize_final.py
import rasterio
import numpy as np

infile = "data/processed/Collocated_S1_S2.tif"
outfile = "data/processed/Collocated_clean.tif"

with rasterio.open(infile) as src:
    profile = src.profile
    data = src.read().astype(np.float32)

    # Drop band 5 (mask)
    data = data[:4]

    # SAR bands (1, 2) → log transform to dB, then normalize
    for i in [0, 1]:
        data[i] = 10 * np.log10(data[i] + 1e-6)  # dB
        band_min, band_max = np.nanpercentile(data[i], [2, 98])  # robust scaling
        data[i] = np.clip((data[i] - band_min) / (band_max - band_min), 0, 1)

    # Optical bands (3, 4) → scale to 0–1
    for i in [2, 3]:
        band_min, band_max = np.nanpercentile(data[i], [2, 98])
        data[i] = np.clip((data[i] - band_min) / (band_max - band_min), 0, 1)

    profile.update(count=4, dtype=rasterio.float32)

    with rasterio.open(outfile, "w", **profile) as dst:
        dst.write(data)

print("✅ Cleaned & normalized GeoTIFF saved:", outfile)
