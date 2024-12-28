# predict/utils.py
import joblib
import os

# Chemin vers le fichier du modèle
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'D:\django\data\car_price_prediction_model.pkl')

# Charger le modèle
model = joblib.load(MODEL_PATH)
