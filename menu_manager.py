from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI
from strings import html_producto, html_producto_input

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    descripcion = db.Column(db.String)
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)

    def __repr__(self):
        return "<Producto(nombre='{}', descripción='{}', precio={}, stock={})>".format(
                self.nombre, self.descripcion, self.precio, self.stock
                )

@app.route('/', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        producto = Producto(
            nombre = request.form.get('nombre'),
            descripcion = request.form.get('descripcion'),
            precio = request.form.get('precio'),
            stock = request.form.get('stock')
        )
        db.session.add(producto)
        db.session.commit()

    productos = Producto.query.all()
    tarjetas = ''
    for p in productos:
        tarjeta = html_producto.format(
            p.nombre,
            p.descripcion,
            p.precio,
            p.stock
        )
        tarjetas += tarjeta
    #aquí vamos a mandar variables para cargar la tarjeta de edición de producto,
    #como el titulo de la tarjeta, los valores de los campos si hay info y si el
    #botón cancelar debe estar oculto o no:
    tarjeta_input = html_producto_input.format(
        'Crear un nuevo producto',
        '','','','',
        'hidden'
        )
    return render_template('menu.html', tarjeta_input=tarjeta_input, tarjetas=tarjetas)


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(debug=True)
    


