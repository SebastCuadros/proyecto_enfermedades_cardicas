import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# Leer el archivo CSV
import os
csv_path = os.path.join(os.path.dirname(__file__), 'heart_data.csv')
df = pd.read_csv(csv_path)


# Eliminar columna innecesaria si existe
if "Unnamed: 0" in df.columns:
    df = df.drop("Unnamed: 0", axis=1)

# Separar variables independientes y dependiente
X = df[['biking', 'smoking']]
y = df['heart.disease']

# Dividir el dataset en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluación rápida
r2 = model.score(X_train, y_train)
print(f"R² del modelo: {r2:.4f}")

# Guardar modelo
os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Modelo entrenado y guardado en 'models/model.pkl'")

# Prueba de predicción opcional
ejemplo = model.predict([[20.1, 56.3]])
print(f"Ejemplo de predicción [20.1%, 56.3%]: {ejemplo[0]:.2f}%")
