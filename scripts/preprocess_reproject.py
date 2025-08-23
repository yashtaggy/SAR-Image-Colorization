import os
import glob
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

# Input & Output folders
input_folder = "data/raw/sentinel2/"
output_folder = "data/interim/sentinel2/"
os.makedirs(output_folder, exist_ok=True)

# Target CRS & resolution
target_crs = "EPSG:4326"   # WGS84, you can change to UTM zone if needed
target_resolution = 10     # meters per pixel (matches Sentinel-1 GRD)

def reproject_resample(input_tif, output_tif, target_crs, target_resolution):
    with rasterio.open(input_tif) as src:
        transform, width, height = calculate_default_transform(
            src.crs, target_crs, src.width, src.height, *src.bounds, resolution=target_resolution
        )
        
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': target_crs,
            'transform': transform,
            'width': width,
            'height': height
        })
        
        with rasterio.open(output_tif, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=target_crs,
                    resampling=Resampling.bilinear
                )
    print(f"[OK] Reprojected & resampled → {output_tif}")

if __name__ == "__main__":
    tifs = glob.glob(os.path.join(input_folder, "*.tif"))
    if not tifs:
        print("[WARN] No .tif files found in", input_folder)
    else:
        for tif in tifs:
            filename = os.path.basename(tif)
            output_path = os.path.join(output_folder, filename.replace(".tif", "_std.tif"))
            reproject_resample(tif, output_path, target_crs, target_resolution)
