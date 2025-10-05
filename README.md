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
