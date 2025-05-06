
# AIS Trajectory Prediction and Visualization

This project builds a real-time ship tracking and prediction tool using AIS (Automatic Identification System) data, machine learning, and web-based visualization. It was developed as part of an AI & Data Engineering course project at TUAS.

## 🔍 Features

- ✅ Real-time AIS data fetching from Digitraffic.fi
- ✅ Ship trajectory prediction (5 minutes ahead) using a trained Random Forest model
- ✅ Basic map visualization of current and predicted ship positions
- ✅ Python-based implementation using scikit-learn and plotting tools
- ✅ Notebook and scripts modularized by stages: fetching, preprocessing, training, and querying

## 📊 Tech Stack

- Python, Pandas, Scikit-learn
- Jupyter Notebook
- Matplotlib / Seaborn (for visualization)
- Pickle (`.pkl`) model export

## 🧠 Machine Learning

- Model: Random Forest Regressor
- Input: ship coordinates, speed, course over ground (COG)
- Output: predicted latitude and longitude after 5 minutes
- Trained and saved using `joblib` as `trajectory_rf_model.pkl`

## 📦 Folder Structure

```
source_code/
├── 1a_AIS_data_fetching.py         # Fetch AIS data from source (e.g., MQTT or API)
├── 1b_AIS_preprocessing.ipynb      # Clean and prepare data
├── 2a_train_rf_model.py            # Train and export Random Forest model
├── 2b_Visualize_prediction.py      # Plot predictions vs real data
├── 3a_query_API.py                 # Predict future position given live data
├── trajectory_rf_model.pkl         # Trained machine learning model
```

## ▶️ How to Run

1. Install dependencies (`requirements.txt` recommended)
2. Run data fetching:  
```bash
python source_code/1a_AIS_data_fetching.py
```
3. Preprocess data using Jupyter Notebook:  
```bash
jupyter notebook source_code/1b_AIS_preprocessing.ipynb
```
4. Train model:  
```bash
python source_code/2a_train_rf_model.py
```
5. Visualize predictions:  
```bash
python source_code/2b_Visualize_prediction.py
```
6. Query with new data:  
```bash
python source_code/3a_query_API.py
```

## 📚 Credits

Developed by Jiao Chen and Vo Thao at Turku University of Applied Sciences  
Part of the AI + Real-time Data Engineering course

## 💡 Future Improvements

- Integrate with real-time map dashboard (Dash / Leaflet)
- Deploy via web service API (e.g., FastAPI)
- Extend prediction range (15+ min)
