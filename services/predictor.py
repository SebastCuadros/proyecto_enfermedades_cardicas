import numpy as np
import pickle
import os

class Predictor:
    def __init__(self, model_path='models/model.pkl'):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Modelo no encontrado en: {model_path}")
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predecir(self, ciclismo: float, fumadores: float) -> float:
        entrada = np.array([[ciclismo, fumadores]])
        prediccion = self.model.predict(entrada)
        return float(np.clip(prediccion[0], 0, 100))  # % de riesgo
