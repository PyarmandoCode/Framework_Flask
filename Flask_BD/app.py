from flask import Flask,render_template,request,redirect,url_for,jsonify
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
    
#Ruta para eliminar Books
@app.route('/books/<int:book_id>/delete',methods=['GET','POST'])   
def deleteBook(book_id):
    bookToDelete=session.query(Book).filter_by(id=book_id).one()
    if request.method=="POST":
        session.delete(bookToDelete)
        session.commit()
        return redirect(url_for('showBooks',book_id=book_id))
    else:
        return render_template('deleteBook.html',book=bookToDelete)

#Ruta para Editar Books 
@app.route('/books/<int:book_id>/edit',methods=['GET','POST'])   
def editBook(book_id):
    bookToEdit=session.query(Book).filter_by(id=book_id).one()
    if request.method=="POST":
        if request.form['nombre']:
            #Poniendo solo el campo Nombre
            bookToEdit.title=request.form['nombre']
            return redirect(url_for('showBooks'))
    else:
        return render_template('editBook.html',book=bookToEdit)


#Api Rest
# Funciones para las Apis
def get_books():
    books = session.query(Book).all()
    return jsonify(books=[b.serialize for b in books])

def book_new(titulo,autor,genero,precio):
    newBook=Book(title=titulo,
                     author=autor,
                     genre=genero,
                     price=precio)
    session.add(newBook)
    session.commit()
    return jsonify(Book=newBook.serialize)

def get_book(book_id):
    book=session.query(Book).filter_by(id=book_id).one()
    return jsonify(books=book.serialize)

def deleteBook(id):
     bookToDelete=session.query(Book).filter_by(id=id).one()
     session.delete(bookToDelete)
     session.commit()
     return 'Book removido con exito %s' % id

def updateBook(id,title):
    bookupdate=session.query(Book).filter_by(id=id).one()
    if not title:
        bookupdate.title=title
    session.add(bookupdate)    
    session.commit()
    return 'Book Actualizado con exito %s' % id
     


#Crear los Endpoints
@app.route('/booksApi',methods=['GET','POST'])
def booksFunction():
    if request.method == 'GET':
        return get_books()
    elif request.method =='POST':
        title=request.args.get('title','')
        author=request.args.get('author','')
        genre=request.args.get('genre','')
        price=request.args.get('price','')
        return book_new(title,author,genre,price)
    
@app.route('/booksApi/<int:id>',methods=['GET','PUT','DELETE'])    
def bookfunctionid(id):
    if request.method=='GET':
        return get_book(id)
    elif request.method =='DELETE':
        return deleteBook(id)
    elif request.method=='PUT':
         title=request.args.get('title','')
         return updateBook(id,title)
    

        
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=4996)