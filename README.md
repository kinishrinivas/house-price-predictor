# 🏠 House Price Prediction Web App

This is a Machine Learning based web application that predicts house prices based on user inputs such as area, quality, garage size, etc.

---

## 🚀 Live Demo
(Add your Render link here after deployment)

---

## 📌 Features

- Predict house price using ML model
- User-friendly web interface
- Input validation (prevents wrong inputs)
- Shows price in ₹ (Indian format)
- Displays price category (Low / Medium / High)
- Keeps user input even after errors

---

## 🧠 Machine Learning

### Algorithms Used:
- Linear Regression
- Decision Tree
- Random Forest ✅ (Best Model)

### Evaluation Metrics:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

### Best Model:
Random Forest performed best with:
- R² Score ≈ 0.87
- Cross-validation score ≈ 0.81

---

## 📊 Dataset

- Kaggle House Prices Dataset
- Features used:
  - GrLivArea
  - OverallQual
  - GarageCars
  - GarageArea
  - TotalBsmtSF
  - 1stFlrSF
  - FullBath

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas / NumPy
- HTML + CSS

---

## 📁 Project Structure
house-price-predictor/
│
├── app.py
├── model.pkl
├── requirements.txt
├── templates/
│ └── index.html
└── README.md


---

## ⚙️ How to Run Locally

```bash
# Clone repo
git clone https://github.com/kinishrinivas/house-price-predictor.git

# Go to folder
cd house-price-predictor

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py

Open browser:

http://127.0.0.1:5000/
