# 🌧️🌊Banjir Jakarta Flood Prediction API

Sebuah project berbasis FastAPI yang dapat memprediksi kemungkinan terjadinya banjir di Jakarta, berdasarkan input data lingkungan seperti kelembapan, curah hujan, sinar matahari, kategori tanah, dan bulan.

## 📂 Struktur File FastAPI

```
fastapi_flood/
├── Final_Data.csv       # Dataset hasil olahan untuk training/testing model
├── main.py              # Endpoint API utama berbasis FastAPI
├── model_knn.pkl        # File model Machine Learning (KNN) yang telah dilatih
├── scaler.pkl           # File scaler untuk normalisasi data input
├── requirements.txt     # Daftar dependency/library yang dibutuhkan
└── __pycache__/         # Folder cache Python hasil kompilasi file .py
```

## 🚀 Fitur API

- Prediksi potensi banjir di Jakarta berdasarkan data lingkungan  
- Menerima input melalui metode **POST**  
- Hasil prediksi berupa: `Aman Banjir` atau `Potensi Banjir`  
- Ringan, cepat, dan siap diintegrasikan ke aplikasi atau dashboard analisis  

## ▶️ Cara Menjalankan

### 1. Clone Repositori

```bash
git clone https://github.com/username/banjir-fastapi.git
cd banjir-fastapi
```

### 2. Buat Virtual Environment

```bash
python -m venv .env
source .env/bin/activate  # Command Prompt: .env\Scripts\activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan API

```bash
uvicorn main:app --reload
```

### 5. Akses Swagger UI

Buka browser ke:  
➡️ [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📨 Contoh 1 JSON Input

```json
{
  "RH_avg": 95,
  "RR": 180,
  "ss": 1,
  "TempRangeCategory": 2,
  "month": 1
}
```

## 📩 Contoh Output 1

```json
{
  "input": {
    "RH_avg": 95,
    "RR": 180,
    "ss": 1,
    "TempRangeCategory": 2,
    "month": 1
  },
  "prediksi": "Potensi Banjir"
}
```
## 📨 Contoh 2 JSON Input

```json
{
  "RH_avg": 85,
  "RR": 100,
  "ss": 2,
  "TempRangeCategory": 2,
  "month": 6
}
```

## 📩 Contoh Output 2

```json
{
  "input": {
    "RH_avg": 85,
    "RR": 100,
    "ss": 2,
    "TempRangeCategory": 2,
    "month": 6
  },
  "prediksi": "Aman Banjir"
}
```


> Dibuat sebagai bagian dari praktik tahap **Deployment** dalam metode **CRISP-DM**.  
> Proyek ini dapat dijadikan dasar pengembangan API prediksi sederhana lainnya.
