
# 🧠 Predicción de Enfermedades Cardíacas - Proyecto Final

Este proyecto es una aplicación web desarrollada con Flask que permite predecir el riesgo de enfermedades cardíacas a partir del porcentaje de personas que montan bicicleta y del porcentaje de fumadores en una población. Forma parte del proyecto final del curso **Programación Avanzada** de la Universidad Distrital Francisco José de Caldas.

## 🚀 Funcionalidades principales

- Predicción del riesgo de enfermedad cardíaca usando un modelo de regresión lineal.
- Almacenamiento de cada predicción en una base de datos SQLite.
- Visualización del historial completo de predicciones realizadas desde la web.

---

## 🧰 Tecnologías utilizadas

- Python 3.12
- Flask
- Scikit-learn
- Pandas
- SQLAlchemy (ORM)
- SQLite
- HTML + Jinja2

---

## 📂 Estructura del proyecto

```
proyecto_flask_prediccion/
├── app.py
├── entrenar_modelo.py
├── heart_data.csv
├── requirements.txt
├── predicciones.db
├── models/
│   └── model.pkl
├── services/
│   ├── predictor.py
│   └── database.py
├── templates/
│   ├── index.html
│   └── historial.html
```

---

## ⚙️ Cómo ejecutar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/proyecto-final-prediccion.git
cd proyecto-final-prediccion
```

### 2. Crea y activa un entorno virtual (opcional pero recomendado)

```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
source .venv/bin/activate  # En Linux/macOS
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Entrena el modelo (si no existe)

```bash
python entrenar_modelo.py
```

Esto creará el archivo `models/model.pkl`.

### 5. Ejecuta la aplicación web

```bash
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

---

## 📝 Funcionalidad de historial

Accede al historial de predicciones realizadas visitando:

```
http://127.0.0.1:5000/historial
```

---

## 📊 Datos de entrenamiento

El modelo fue entrenado con datos sintéticos basados en correlaciones estadísticas entre actividad física, tabaquismo y enfermedades cardíacas, contenidos en el archivo `heart_data.csv`.

---

## 📚 Créditos

Desarrollado por **Juan Sebastián Gutiérrez Cuadros**  
Curso: Programación Avanzada  
Universidad Distrital Francisco José de Caldas  
Docente: Ing. Jonathan Torres, PhD.

---

## 📎 Licencia

Este proyecto es exclusivamente educativo y no está destinado para uso clínico o comercial.
