#Importamos Flask
from flask import Flask

#Crear una Aplicacion  Flask , Instanciar el Objeto Flask
app=Flask(__name__)

#Crear RUTAS
@app.route('/')
def index():
    return "Bienvenido a Flask"

@app.route('/clientes')
def clientes():
    return "Zona de Clientes"

@app.route('/productos')
def productos():
    return "Zona de Productos"

#Ejecutar la Aplicacion
app.run()

#flask run --host=0.0.0.