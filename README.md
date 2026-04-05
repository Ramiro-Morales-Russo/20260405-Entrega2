# Ramiro Morales Russo 018976/1
20260405-Entrega2
Se corresponde a la entrega 2 del taller de lenguaje - Python

Como instalar las dependencias (windows):

Lo primeroque debemos hacer es definir un entorno virtual en un directorio donde se realizará el proyecto:

Para esto:

1- Abrir la terminal y ubicarse en la carpeta donde se alojará el proyecto

2- Crear el entorno virtual usando el comando:

    python -m venv mi_entorno

(Si no funciona este comando usar python3 en lugar de python)

3- Activar el entorno:

    mi_entorno\Scripts\activate


Para que esta entrega pueda ejecutarse correctamente se deben instalar las librerías indicadas en el archivo requierements.txt. 

Para esto:
Posicionarse en la carpeta donde se dispone del archivo requirements.txt y ejecutar en la terminal:


    pip install -r requirements.txt


Como ejecutar el programa:

Para ejecutar correctamente el programa se requiere instalar jupyter usando el comando:

    pip install jupyterlab

(Esto debemos realizarlo en el directorio donde alojemos el proyecto)

Podemos utilizar esta herramienta desde el IDE, por ejemplo en Visual Studio Code que posee integración:

Si el archivo posee extensión ipynb será formato notebook.

o sino ejecutando en la terminal el siguiente comando:

    jupyter notebook

(Considerar que es necesario estar posicionado en el entorno virtual que creamos previamente y con las librerías necesarias)
