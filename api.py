# app.py
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado con TensorFlow
model = tf.keras.models.load_model("model_tensorflow.h5")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos de entrada del cliente en formato JSON
        data = request.json['data']

        # Convertir los datos a un array de numpy
        input_data = np.array(data)

        # Realizar la inferencia utilizando el modelo cargado
        prediction = model.predict(np.expand_dims(input_data, axis=0))
        predicted_class = np.argmax(prediction)

        # Obtener el nombre de la clase basado en el índice
        class_names = ["setosa", "versicolor", "virginica"]
        predicted_class_name = class_names[predicted_class]

        # Devolver la predicción como respuesta en formato JSON
        result = {"prediction": predicted_class_name}
        return jsonify(result)
    except:
        return jsonify({"error": "Error en la solicitud. Asegúrate de que los datos de entrada sean válidos."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
