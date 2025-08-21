# 🌍 SAR Image Colorization using Deep Learning (SIH1733)

## 📌 Problem Statement
Synthetic Aperture Radar (SAR) imagery is rich in structural and textural information but lacks the intuitive appeal of color, which can provide more comprehensive insights for space-borne applications.  
This project aims to build a **Deep Learning model** that colorizes grayscale SAR images using paired SAR–Optical datasets, enhancing interpretability and usability for applications like geological studies, disaster management, and environmental monitoring.

## 🎯 Objectives
- Develop a **novel DL model (U-Net, Pix2Pix)** for SAR → Optical image colorization.
- Improve SAR data usability with **intuitive visual outputs**.
- Achieve measurable quality using **PSNR, SSIM, Perceptual Loss**.
- Deploy as a **user-friendly software tool** (CLI + Web UI).

## 🏗️ Architecture (High-Level)
1. **Data Preprocessing**  
   - SAR + Optical pairs aligned and tiled (256×256).  
   - Normalization, augmentation.  

2. **Model Development**  
   - Baseline: **U-Net** (supervised).  
   - Advanced: **Pix2Pix GAN** (adversarial training).  

3. **Training & Evaluation**  
   - Losses: L1, SSIM, Perceptual.  
   - Metrics: PSNR, SSIM, visual inspection.  

4. **Deployment**  
   - CLI tool for analysts.  
   - Web app (FastAPI / Streamlit).  

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Deep Learning Framework:** PyTorch
- **Data Handling:** GDAL, Rasterio, OpenCV, NumPy, Pandas
- **Experiment Tracking:** Weights & Biases (W&B) / MLflow
- **Deployment:** FastAPI, Streamlit, Docker
- **Version Control:** GitHub + Git LFS / DVC for large files

## 📂 Repo Structure
   SAR-Colorization/
   ├── app/ # Deployment (API/UI)
   ├── checkpoints/ # Saved models (gitignored)
   ├── configs/ # Config files for training/eval
   ├── data/ # Preprocessed data (gitignored)
   ├── models/ # Model definitions (U-Net, Pix2Pix)
   ├── notebooks/ # Jupyter notebooks for experiments
   ├── reports/ # Evaluation reports, results
   ├── scripts/ # Preprocessing, metrics, utils
   ├── train.py # Training entrypoint
   ├── evaluate.py # Evaluation script
   ├── infer.py # Inference script
   ├── requirements.txt # Python dependencies
   ├── LICENSE
   └── README.md

## 🚀 Getting Started
1. Clone this repo:
   ```bash
   git clone https://github.com/<org>/<repo>.git
   cd SAR-Colorization
   ```

2. Create environment:

```bash
   conda create -n sarcolor python=3.10 -y
   conda activate sarcolor
   pip install -r requirements.txt
   ```
3. Run preprocessing:

```bash
   python scripts/preprocess.py --input data/raw --output data/tiles
   ```

4. Train model:

```
python train.py --config configs/unet.yaml
```

5. Run inference:

```
python infer.py --ckpt checkpoints/unet_best.pt --input samples/sar.tif --out outputs/colorized.png
```
