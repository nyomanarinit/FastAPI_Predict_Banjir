from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# Inisialisasi FastAPI
app = FastAPI(title="API Prediksi Banjir Jakarta")

# Cek apakah model dan scaler sudah ada
if not os.path.exists("model_knn.pkl") or not os.path.exists("scaler.pkl"):
    # Kalau belum ada, training dulu
    # Path relatif
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "Final_Data.csv")

    df = pd.read_csv(file_path)
    X = df[['RH_avg', 'RR', 'ss', 'TempRangeCategory', 'month']]
    y = df['flood']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    scaler = MinMaxScaler()
    X_train_norm = scaler.fit_transform(X_train)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train_norm, y_train)

    with open("model_knn.pkl", "wb") as f:
        pickle.dump(knn, f)

    with open("scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    print("Training selesai dan model disimpan!")

# Load model dan scaler
with open("model_knn.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Schema input
class FloodPredictionInput(BaseModel):
    RH_avg: float
    RR: float
    ss: float
    TempRangeCategory: int
    month: int

# Endpoint root
@app.get("/")
def read_root():
    return {"message": "API Prediksi Banjir Jakarta aktif!"}

# Endpoint prediksi
@app.post("/predict")
def predict_flood(data: FloodPredictionInput):
    input_data = np.array([[data.RH_avg, data.RR, data.ss, data.TempRangeCategory, data.month]])
    input_data_norm = scaler.transform(input_data)
    prediction = model.predict(input_data_norm)
    hasil = "Potensi Banjir" if prediction[0] == 1 else "Aman Banjir"
    return {"input": data, "prediksi": hasil}
