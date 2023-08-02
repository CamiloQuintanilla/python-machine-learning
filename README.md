# python-machine-learning

Este proyecto contiene un modelo de machine learning y este se ejecute mediante un api POST

para el correcto funcionamiento de la aplicacion se utiliza docker y kubernetes, a continuacion se dejan todos los comandos que se necesiten para disponibilizar la aplicacion

# Creacion de la imagen de docker
solo es ejecutar el siguiente comando bajo el path del proyecto:

- docker build -t nombre_imagen . (nombre_imagen se puede reemplazar segun como quieras llamar la imagen de docker)

en caso de que desees probar el funcionamiento de la api lo puedes hacer con este comando:

- docker run -p 5000:5000 nombre_imagen

# Despliegue con Kubernetes
En el proyecto hay dos archivos ("deployment.yaml","service.yaml") estos ficheros permiten el despliegue en hacia el cluster de kubernetes con los siguientes comandos:

- kubectl apply -f deployment.yaml
- kubectl apply -f service.yaml

ya para obtener la direccion IP y el PUERTO en el que se esta ejecutando la aplicacion se ejecuta el siguiente comando:

- kubectl get services

Ya con esto se tendria esta aplicacion basica de machine-learning funcionando con Docker y Kubernetes :)