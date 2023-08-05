from flask import Flask

app= Flask(__name__)

#Pasar Parametros a las Paginas
@app.route('/suma/<int:s1>/<int:s2>',methods=['GET'])
def suma(s1,s2):
    return 'La suma de los son valores es_'+str(s1+s2)

@app.errorhandler(404)
def page_not_found(error):
    return "Ha ocurrido un problema por favor vuelva a intentarlo en 24 horas" , 404

if __name__ == '__main__':
    app.run(debug=True,port=8000)
