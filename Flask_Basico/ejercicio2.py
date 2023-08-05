from flask import Flask
import json

app= Flask(__name__)


@app.route('/')
def index():
    return json.dumps({'Nombre':'Armando',
                      'Email':'armando.eu.ruiz@gmail.com',
                      'Profesion':'developer',
                      'Edad':40
    })


app.run()