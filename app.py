from flask import Flask, request, render_template
from services.predictor import Predictor
from services.database import Prediccion, Session

app = Flask(__name__)
predictor = Predictor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        ciclismo = float(request.form['ciclismo'])
        fumadores = float(request.form['fumadores'])
        resultado = predictor.predecir(ciclismo, fumadores)

        # Guardar en base de datos
        session = Session()
        nueva_pred = Prediccion(ciclismo=ciclismo, fumadores=fumadores, resultado=resultado)
        session.add(nueva_pred)
        session.commit()
        session.close()

        mensaje = f"Probabilidad estimada de enfermedad cardíaca: {resultado:.2f}%"
    except Exception as e:
        mensaje = f"⚠️ Error al procesar la predicción: {str(e)}"

    return render_template('index.html', prediction_text=mensaje)


@app.route('/historial')
def historial():
    session = Session()
    predicciones = session.query(Prediccion).order_by(Prediccion.timestamp.desc()).all()
    session.close()
    return render_template('historial.html', predicciones=predicciones)



if __name__ == '__main__':
    app.run(debug=True)
