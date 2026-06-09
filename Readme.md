# Data Automation & Preprocessing Pipeline

An small scale automated data pipeline designed to take, clean, and standardize messy or unordered datasets for machine learning applications. 

## Project Overview
Raw data is rarely ready for machine learning models. This project is a Python utility that automatically handles missing values, removes duplicates, and mitigates extreme outliers using statistical methods (IQR). It ensures datasets are structurally sound and statistically clean before they hit a predictive model.

## Key Features
* **Schema Validation:** Automatically verifies the structural integrity of incoming datasets to prevent downstream crashes.
* **Intelligent Imputation:** Fills missing categorical data with mode values and numerical data with medians to resist outlier skewing.
* **Vectorized Outlier Handling:** Utilizes `numpy.clip()` to cap extreme values using the Interquartile Range (IQR) method for maximum execution speed.
* **Production Logging:** Generates real-time execution logs for easy debugging and monitoring.

## Tech Stack
* **Language:** Python 3.14.0
* **Libraries:** `polars` (Data manipulation), `numpy` (Vectorized mathematical operations), `logging` (Execution tracking)

## Installation & Usage

1. **Clone the repository** and navigate to the project root.
2. **Prepare the folders:** Ensure your local directory structure includes the data folders:
```bash
mkdir -p data/raw data/processed

```
3. **Add your data:** Place your target dataset inside the `data/raw/` directory and rename it exactly to `raw_data.csv`.
4. **Execute the pipeline:** Run the automation script via your terminal:
5. 
```bash
python src/pipeline.py

```
5. **View results:** The fully cleaned dataset with handled missing values and clipped outliers will be exported directly to `data/processed/clean_data.csv`.
---
