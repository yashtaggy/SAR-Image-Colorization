import os
import glob
import rasterio
from rasterio.enums import Resampling

# Input & output folders
s1_folder = "data/interim/sentinel1/"
s2_folder = "data/interim/sentinel2/"
output_folder = "data/processed/pairs/"
os.makedirs(output_folder, exist_ok=True)

def coregister_pair(s1_path, s2_path, output_prefix):
    with rasterio.open(s1_path) as s1, rasterio.open(s2_path) as s2:
        # Find intersection bounds
        bounds = (
            max(s1.bounds.left, s2.bounds.left),
            max(s1.bounds.bottom, s2.bounds.bottom),
            min(s1.bounds.right, s2.bounds.right),
            min(s1.bounds.top, s2.bounds.top)
        )
        
        if bounds[0] >= bounds[2] or bounds[1] >= bounds[3]:
            print(f"[SKIP] No overlap between {s1_path} and {s2_path}")
            return
        
        # Read & clip both
        s1_window = s1.window(*bounds)
        s2_window = s2.window(*bounds)
        
        s1_data = s1.read(
            window=s1_window,
            out_shape=(s1.count, int(s1_window.height), int(s1_window.width)),
            resampling=Resampling.bilinear
        )
        s2_data = s2.read(
            window=s2_window,
            out_shape=(s2.count, int(s2_window.height), int(s2_window.width)),
            resampling=Resampling.bilinear
        )

        # Match shapes
        min_h = min(s1_data.shape[1], s2_data.shape[1])
        min_w = min(s1_data.shape[2], s2_data.shape[2])

        if min_h <= 0 or min_w <= 0:
            print(f"[SKIP] Overlap too small between {s1_path} and {s2_path}")
            return

        s1_data = s1_data[:, :min_h, :min_w]
        s2_data = s2_data[:, :min_h, :min_w]
        
        # --- Save SAR ---
        meta_s1 = s1.meta.copy()
        meta_s1.update({
            "count": s1_data.shape[0],  # 1 band
            "height": min_h,
            "width": min_w,
            "transform": s1.window_transform(s1_window)
        })
        s1_out = os.path.join(output_folder, f"{output_prefix}_SAR.tif")
        with rasterio.open(s1_out, "w", **meta_s1) as dst1:
            dst1.write(s1_data)
        
        # --- Save Optical ---
        meta_s2 = s2.meta.copy()
        meta_s2.update({
            "count": s2_data.shape[0],  # usually 3 bands (RGB)
            "height": min_h,
            "width": min_w,
            "transform": s2.window_transform(s2_window)
        })
        s2_out = os.path.join(output_folder, f"{output_prefix}_OPT.tif")
        with rasterio.open(s2_out, "w", **meta_s2) as dst2:
            dst2.write(s2_data)
        
        print(f"[OK] Coregistered pair saved: {s1_out}, {s2_out}")

if __name__ == "__main__":
    s1_files = sorted(glob.glob(os.path.join(s1_folder, "*.tif")))
    s2_files = sorted(glob.glob(os.path.join(s2_folder, "*.tif")))

    for i, (s1_file, s2_file) in enumerate(zip(s1_files, s2_files)):
        coregister_pair(s1_file, s2_file, f"pair_{i+1}")
