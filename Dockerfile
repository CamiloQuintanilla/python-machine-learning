# Utiliza la imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios a la imagen de contenedor
COPY api.py model_tensorflow.h5 /app/

# Instala las dependencias necesarias
RUN pip install Flask==2.3.2 tensorflow==2.13.0

# Expone el puerto 5000, el mismo que usa la aplicación Flask
EXPOSE 5000

# Ejecuta la aplicación Flask cuando se inicie el contenedor
CMD ["python", "api.py"]
