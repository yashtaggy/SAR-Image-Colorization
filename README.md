# 🌈 SAR Image Colorization using Deep Learning

> **Transforming Monochromatic SAR Imagery into Intuitive, Colorized Visuals for Enhanced Remote Sensing Analysis**

---

## 📘 Project Overview

Synthetic Aperture Radar (**SAR**) imagery provides invaluable structural and textural information about the Earth’s surface, but it lacks the intuitive appeal of color. This project aims to bridge that gap by **colorizing grayscale SAR images using Deep Learning (DL)** models trained on paired **SAR and Optical (Sentinel-1 & Sentinel-2)** data.

By learning the complex mapping between radar backscatter and optical reflectance, this project produces colorized SAR images that significantly enhance the **interpretability and usability of remote sensing data** for applications such as **geological studies, urban mapping, and environmental monitoring**.

---

## 🎯 Objectives

* Develop a **Deep Learning-based SAR image colorization model** for robust image-to-image translation.
* Enhance the **visual interpretability** and information density of SAR imagery.
* Create a **scalable pipeline** for preprocessing, collocating, and preparing Sentinel-1 & Sentinel-2 imagery for training.
* Design a **user-ready colorization software** (future work) for remote sensing analysts.

---

## ⚙️ Key Features

✅ **Data Preprocessing Pipeline:** Robust scripts for processing Sentinel-1 (SAR) and Sentinel-2 (Optical) data.
✅ **Automatic Co-registration:** Automated co-registration and tiling of paired SAR/Optical data for dataset creation.
✅ **Custom DL Model:** Implementation of a custom **U-Net** (or **GAN**) for SAR-to-RGB translation.
✅ **Configurable Training:** Modular training pipeline built with **PyTorch**.
✅ **Evaluation & Visualization:** Scripts for model evaluation, metrics tracking, and result visualization.
✅ **Modular Structure:** Clean and reproducible project layout.

---

## 🗂️ Project Structure

The project is structured for clear separation of concerns, ensuring reproducibility and easy extension:

```yaml
EXPLORER-SAR-IMAGE-COLORIZATION/
├── app/                  # Application code (future GUI or API)
├── checkpoints/          # Model checkpoints during training
├── config/               # Configuration files for data and model parameters
├── data/
│ ├── raw/                # Original raw Sentinel data
│ ├── processed/          # Preprocessed & collocated GeoTIFFs
│ ├── tiles/              # Training-ready dataset (SAR + RGB tiles)
│ ├── maharashtra.geojson # AOI shapefile
│ └── collocated_s1_s2.tif# Main dataset (SAR + Optical pairs)
├── models/               # Trained DL models
├── notebooks/            # Jupyter notebooks for experiments and data exploration
├── outputs/              # Predictions, metrics, and visualizations
├── scripts/              # All preprocessing and training scripts
│ ├── preprocess_s1.py
│ ├── preprocess_s2.py
│ ├── coregister_pairs.py
│ ├── tile_dataset.py
│ ├── inspect_final_geotiff.py
│ └── train_unet.py       # Main training script
├── venv/                 # Virtual environment (ignored by Git)
├── Dockerfile            # For containerization
├── LICENSE
├── .gitignore
├── requirements.txt
└── README.md

```

## 🧠 Dataset Information

The model is trained on carefully **coregistered** pairs of Sentinel-1 and Sentinel-2 imagery.

| Source | Satellite | Type | Description |
| :--- | :--- | :--- | :--- |
| **Sentinel-1** | SAR (VV, VH) | **Input** | Grayscale radar backscatter imagery (Dual-polarization: Vertical-Vertical, Vertical-Horizontal). |
| **Sentinel-2** | Optical (R, G, B) | **Target** | True color optical reference imagery (Red, Green, Blue bands). |

* The dataset was **coregistered and resampled** to the same resolution and coordinate reference system (`EPSG:32643`).
* **Example file:** `data/processed/collocated_s1_s2.tif`
    * **Bands:** 6 (SAR + RGB)
    * **Resolution:** 10m
    * **Shape:** $10980 \times 10980$ pixels

---

## 🧩 Model Architecture

The baseline model is a **U-Net** designed for robust image-to-image translation, specifically SAR-to-RGB.

* **Model Type:** U-Net (Encoder-Decoder)
* **Input:** 2-channel SAR image (VV, VH)
* **Output:** 3-channel RGB image
* **Loss Function:** Mean Squared Error (MSE) / Perceptual Loss (Initial experiments use MSE)
* **Framework:** **PyTorch**
* **Optimizer:** Adam ($\text{lr} = 1e-4$)

### Advanced Versions
Future iterations may explore more sophisticated models for enhanced realism and detail:
* GAN-based colorization (**Pix2Pix / CycleGAN**)
* Transformer-augmented U-Net (**Swin-UNet**)
* Multi-scale perceptual learning

---

## 🚀 Getting Started

Follow these steps to set up the environment and run the training pipeline.

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/yashtaggy/SAR-Image-Colorization.git](https://github.com/yashtaggy/SAR-Image-Colorization.git)
cd SAR-Image-Colorization
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # for Linux/Mac
# venv\Scripts\activate     # for Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Prepare Data
```bash
# This script reads the main GeoTIFF and creates smaller tiles in data/tiles/
python scripts/make_training_tiles.py
```

### 5️⃣ Train the Model
```bash
python scripts/train_unet.py
```

### 6️⃣ Visualize Results
```bash
python scripts/visualize_results.py
```

## 📈 Evaluation Metrics

* MSE (Mean Squared Error)
* PSNR (Peak Signal-to-Noise Ratio)
* SSIM (Structural Similarity Index)
* Perceptual Similarity (LPIPS)
  
## 🧪 Future Enhancements

* Integrate perceptual loss (VGG16 feature loss) for more visually pleasing results.
* Add conditional GAN for realistic, high-fidelity colorization.
* Deploy model as a user-friendly web app (Streamlit / FastAPI).
* Extend dataset for multiple regions and seasons for better generalization.
* Optimize the pipeline for efficient GPU/TPU training.

## 🌍 Acknowledgements
### We extend our gratitude to the following for providing data and essential tools:

* European Space Agency (ESA) — Sentinel-1 & Sentinel-2 Open Data
* Google Earth Engine (GEE)
* SNAP Toolbox by ESA
* PyTorch & Rasterio Communities

> “Turning radar signals into meaningful colors — one pixel at a time.”
