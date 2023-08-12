from flask import Flask,render_template,request,redirect,url_for
app= Flask(__name__)

from sqlalchemy import create_engine
#Object Relational Mapping
from sqlalchemy.orm  import sessionmaker
from Crear_bd import Base,Book


#Conectarme a la base de datos #Bind = Enlace a una BD existente
engine = create_engine('sqlite:///Flask_BD/books-collection.db')
Base.metadata.bind=engine

#Manejo de Sessiones
DBSession = sessionmaker(bind=engine)
#Instanciando el Objeto Session
session= DBSession()


#Landing Page Mostrar Todos Los Libros
@app.route('/')
@app.route('/books')
def showBooks():
    #Select * from Book
    books = session.query(Book).all()
    return render_template('books.html',books=books)

#Ruta Insertar Nuevos Books
@app.route('/books/new',methods=['GET','POST'])
def newBook():
    if request.method == 'POST':
        #Objeto que tratara de insertase en la tabla
        newBook=Book(title=request.form['nombre'],
                     author=request.form['autor'],
                     genre=request.form['genero'],
                     price=request.form['precio'])
        session.add(newBook)
        session.commit()
        return redirect(url_for('showBooks'))
    else:
        return render_template('newbooks.html')
        
                     
                     
                     




if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=4996)