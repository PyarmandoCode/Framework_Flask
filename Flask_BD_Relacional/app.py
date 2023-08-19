from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rioazulq12@localhost/bdcommerce'
db = SQLAlchemy(app)


# todo Crear un Objeto que permita hacer el Mapping de mi tabla ORM
class productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.String(80), nullable=False)
    proveedor = db.Column(db.String(80), nullable=False)
    stock = db.Column(db.Integer)
    estado = db.Column(db.String(1), nullable=False)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
