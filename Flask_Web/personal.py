from flask import Flask,render_template

app= Flask(__name__)

#Fuente de Datos
empleados = [
    {"nombre":"Alicia","apellido":"Guerrero" ,"picture":"https://www.baarty.com/articulos/wp-content/uploads/2013/04/motivando-empleado-bares.jpg"},
    {"nombre":"Carlos","apellido":"Aguilar","picture":"https://www.bbva.com/wp-content/uploads/2013/03/carlos-torres-vila-ceo-bbva-1024x885.jpg"},
    {"nombre":"Ingrid","apellido":"Guerrero","picture":"https://www.clasibo.com/aviso_images/190626_041735.jpg"},
    {"nombre":"Javier","apellido":"Catalan","picture":"https://factorialhr.es/wp-content/uploads/2019/12/20130507/empleados-felices-portada.jpg"},
    {"nombre":"Lhordes","apellido":"Catln","picture":"https://static9.depositphotos.com/1594308/1163/i/950/depositphotos_11632583-stock-photo-successful-accountant.jpg"},

]

@app.route('/Listado')
def listado():
    return render_template("listado.html",emp=empleados)


if __name__ == '__main__':
    app.run(debug=True,port=8000)