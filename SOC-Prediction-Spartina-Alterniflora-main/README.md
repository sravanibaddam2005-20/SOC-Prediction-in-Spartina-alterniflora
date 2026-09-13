# 🌿 Prediction of Soil Organic Carbon Content in Spartina Alterniflora Using Multispectral & LiDAR Data

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![ML](https://img.shields.io/badge/ML-Ensemble%20Model-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Project Overview

Soil Organic Carbon (SOC) is a critical indicator of soil health, carbon sequestration, and ecosystem productivity in coastal wetlands. This project presents a machine learning-based web application that predicts SOC content in **Spartina Alterniflora** (smooth cordgrass) wetlands using **multispectral remote sensing** and **LiDAR (Light Detection and Ranging)** data.

The system combines advanced ensemble learning with **Particle Swarm Optimization (PSO)** for intelligent feature selection, achieving high prediction accuracy across varying SOC levels.

---

## 🎯 Objectives

- Extract meaningful spectral and terrain features from multispectral and LiDAR data
- Apply PSO-based feature selection to identify the most relevant predictors
- Build and compare multiple regression models for SOC prediction
- Deploy a user-friendly Flask web application for real-time SOC prediction
- Visualize SOC distribution using an interactive geospatial heatmap

---

## 🧠 Machine Learning Pipeline

### 1. Feature Selection — Particle Swarm Optimization (PSO)
PSO is a bio-inspired optimization algorithm that simulates the social behavior of birds flocking. It was used to select the optimal subset of features by minimizing the RMSE of an XGBoost model across 5 iterations with 10 particles.

### 2. Models Compared

| Model | Description |
|---|---|
| XGBoost | Gradient boosted trees with regularization |
| Support Vector Machine (SVR) | Linear SVR for regression |
| Random Forest | Bagging ensemble of decision trees |
| **Voting Regressor** ⭐ | Weighted ensemble of XGBoost + GBR + LightGBM + CatBoost |

### 3. Final Model — Voting Regressor (Ensemble)

The best performing model is a **weighted Voting Regressor** combining:

| Base Model | Weight |
|---|---|
| XGBoost | 3 |
| GradientBoostingRegressor | 1 |
| LightGBM | 3 |
| CatBoost | 2 |

**Hyperparameters:**
- `n_estimators`: 1200
- `learning_rate`: 0.03
- `max_depth`: 6
- `subsample`: 0.8
- `colsample_bytree`: 0.8

---

## 📊 Input Features

### Multispectral Features

| Feature | Full Name | Description |
|---|---|---|
| Green | Green Band | Reflectance in green spectrum |
| RedEdge | Red Edge Band | Transition between red and NIR |
| NDVI | Normalized Difference Vegetation Index | Vegetation health indicator |
| GNDVI | Green NDVI | Chlorophyll content estimator |
| NDRE | Normalized Difference Red Edge | Canopy chlorophyll content |
| EVI | Enhanced Vegetation Index | Improved vegetation sensitivity |
| SAVI | Soil Adjusted Vegetation Index | Minimizes soil background effects |
| DVI | Difference Vegetation Index | Simple vegetation measure |
| MSAVI | Modified SAVI | Further reduces soil noise |
| SOS | Start of Season | Phenological timing indicator |

### LiDAR-Derived Terrain Features

| Feature | Description |
|---|---|
| Altitude | Elevation above sea level (m) |
| Slope | Rate of elevation change (degrees) |
| Aspect | Direction of slope face (degrees) |
| Relief | Local elevation difference (m) |

---

## 🌱 SOC Level Classification

| SOC Value (%) | Level | Interpretation |
|---|---|---|
| < 2 | 🔴 Low SOC | Poor soil carbon, degraded ecosystem |
| 2 – 5 | 🟡 Medium SOC | Moderate carbon storage |
| > 5 | 🟢 High SOC | Rich carbon storage, healthy wetland |

---

## 🖥️ Web Application

The Flask web app provides:
- Input form for all 14 features
- Real-time SOC prediction with confidence score
- SOC level classification with color-coded alerts
- Prediction history tracking
- Interactive geospatial heatmap of SOC distribution

### Screenshots

> Enter feature values → Get SOC prediction → View heatmap visualization

---

## 🗂️ Project Structure

```
SOC-Prediction-Spartina-Alterniflora/
│
├── app.py                  # Flask web application (routes, prediction logic)
├── model.sav               # Trained Voting Regressor ensemble model
├── Notebook.ipynb          # Full training pipeline (EDA, PSO, modeling, evaluation)
├── retrain.py              # Script to retrain and resave model.sav
├── SOC_dataset.csv         # Raw input dataset
├── processed.csv           # PSO-selected features dataset
├── report.log              # Training logs
│
├── templates/
│   └── index.html          # Frontend UI (HTML + CSS + JS)
│
└── catboost_info/          # CatBoost training metadata (auto-generated)
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Step 1 — Clone the repository
```bash
git clone https://github.com/Yashwanth26122005/SOC-Prediction-Spartina-Alterniflora.git
cd SOC-Prediction-Spartina-Alterniflora
```

### Step 2 — Install dependencies
```bash
pip install flask numpy joblib xgboost lightgbm catboost scikit-learn pyswarms
```

### Step 3 — Run the app
```bash
python app.py
```

### Step 4 — Open in browser
```
http://127.0.0.1:5000
```

---

## 🔁 Retrain the Model

If you need to retrain the model with updated data or a newer scikit-learn version:

```bash
python retrain.py
```

This will regenerate `model.sav` using `processed.csv`.

---

## 📈 Model Evaluation Metrics

The models were evaluated using:

| Metric | Description |
|---|---|
| MAPE | Mean Absolute Percentage Error |
| RMSE | Root Mean Squared Error |
| MAE | Mean Absolute Error |
| R² Score | Coefficient of Determination |

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| ML Models | XGBoost, LightGBM, CatBoost, Scikit-learn |
| Feature Selection | PySwarms (PSO) |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Frontend | HTML, CSS, JavaScript |

---

## 📚 References

- Spartina Alterniflora wetland carbon dynamics
- PSO for feature selection in remote sensing
- Ensemble learning for regression tasks
- LiDAR-based terrain analysis for SOC estimation

---

## 👨‍💻 Author

**Yashwanth** — [GitHub](https://github.com/Yashwanth26122005)

---

## 📄 License

This project is licensed under the MIT License.
