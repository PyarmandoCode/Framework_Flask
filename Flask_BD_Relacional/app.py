from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rioazulq12@localhost/bdcommerce'
db = SQLAlchemy(app)


# todo Crear un Objeto que permita hacer el Mapping de mi tabla ORM
class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.String(80), nullable=False)
    proveedor = db.Column(db.String(80), nullable=False)
    stock = db.Column(db.Integer)
    estado = db.Column(db.String(1), nullable=False)


@app.route("/", methods=['GET', 'POST'])
@app.route("/<int:producto_id>", methods=['GET'])
def index(producto_id=None):
    if request.method == 'POST':
        pid = request.form.get('id')
        nombre = request.form.get('nombre')
        proveedor = request.form.get('proveedor')
        precio = request.form.get('precio')
        stock = request.form.get('stock')
        estado = request.form.get('estado')
        # todo Para actualizar
        if pid:
            producto = Productos.query.filter_by(id=pid).first()
            producto.name = nombre
            producto.precio = precio
            producto.proveedor = proveedor
            producto.stock = stock
            producto.estado = estado
            db.session.commit()
        else:
            # todo Para insertar
            entrada = Productos(name=nombre, precio=precio, proveedor=proveedor, stock=stock, estado=estado)
            db.session.add(entrada)
            db.session.commit()
    producto = None
    if producto_id:
        producto = Productos.query.filter_by(id=producto_id).first()
    productos = Productos.query.all()

    return render_template("index.html", productos=productos, producto=producto)


if __name__ == "__main__":
    app.run(debug=True)
