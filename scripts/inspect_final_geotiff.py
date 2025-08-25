# scripts/inspect_final_geotiff.py
import rasterio

with rasterio.open("data/processed/Collocated_S1_S2.tif") as src:
    print("Bands:", src.count)
    print("Shape:", src.height, src.width)
    print("CRS:", src.crs)
    print("Transform:", src.transform)
    for i in range(1, src.count + 1):
        band = src.read(i)
        print(f" Band {i} min={band.min()} max={band.max()} mean={band.mean()}")
