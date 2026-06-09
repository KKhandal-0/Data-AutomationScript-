# ⚙️ Data Automation & Preprocessing Pipeline

An small scale automated data pipeline designed to take, clean, and standardize messy or unordered datasets for machine learning applications. 

## 📌 Project Overview
Raw data is rarely ready for machine learning models. This project is a Python utility that automatically handles missing values, removes duplicates, and mitigates extreme outliers using statistical methods (IQR). It ensures datasets are structurally sound and statistically clean before they hit a predictive model.

## 🚀 Key Features
* **Schema Validation:** Automatically verifies the structural integrity of incoming datasets to prevent downstream crashes.
* **Intelligent Imputation:** Fills missing categorical data with mode values and numerical data with medians to resist outlier skewing.
* **Vectorized Outlier Handling:** Utilizes `numpy.clip()` to cap extreme values using the Interquartile Range (IQR) method for maximum execution speed.
* **Production Logging:** Generates real-time execution logs for easy debugging and monitoring.

## 🛠️ Tech Stack
* **Language:** Python 3.14.0
* **Libraries:** `polars` (Data manipulation), `numpy` (Vectorized mathematical operations), `logging` (Execution tracking)

## 📂 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/data-automation-pipeline.git](https://github.com/YourUsername/data-automation-pipeline.git)
   cd data-automation-pipeline

2. Install dependencies:
  pip install polars
  Run the pipeline:

3.Place your raw dataset in the data/raw/ directory and execute:
  python src/pipeline.py
