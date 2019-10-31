from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI
from strings import html_producto, html_producto_input, html_borrar

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
        if request.form.get('id_producto'):
            id_editado = request.form.get('id_producto')
            producto_editado = Producto.query.filter_by(id_producto=id_editado).first()
            producto_editado.nombre = request.form.get('nombre'),
            producto_editado.descripcion = request.form.get('descripcion'),
            producto_editado.precio = request.form.get('precio'),
            producto_editado.stock = request.form.get('stock')
        else:
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
            p.stock,
            p.id_producto,
            p.id_producto
        )
        tarjetas += tarjeta
    #aquí vamos a mandar variables para cargar la tarjeta de edición de producto,
    #como el titulo de la tarjeta, los valores de los campos si hay info y si el
    #botón cancelar debe estar oculto o no:
    tarjeta_input = html_producto_input.format(
        'Crear un nuevo producto',
        '','','','','',''
        'hidden'
        )
    return render_template('menu.html', tarjeta_input=tarjeta_input, tarjetas=tarjetas)

@app.route('/editar', methods=['GET','POST'])
def editar():
    id_seleccionado = request.form.get('id_producto')
    p = Producto.query.filter_by(id_producto=id_seleccionado).first()
    tarjeta_editar = html_producto_input.format(
        'Editar Producto:',
        p.nombre,
        p.descripcion,
        p.precio,
        p.stock,
        p.id_producto,
        'button'
    )

    return render_template('editar.html', tarjeta_input=tarjeta_editar)

@app.route('/confirmar', methods=['POST'])
def confirmar_borrado():
    id_seleccionado = request.form.get('id_producto')
    p = Producto.query.filter_by(id_producto=id_seleccionado).first()
    tarjeta = html_borrar.format(
        p.nombre,
        p.descripcion,
        p.precio,
        p.stock,
        p.id_producto,
        p.id_producto
    )
    return render_template('confirmar.html', tarjeta=tarjeta)

@app.route('/borrar', methods=['POST'])
def borrar():
    #TODO, en realidad esto tiene que redirigir a una página donde se le pregunta si quiere 
    #eliminar de verdad, y esa página recién lleva aquí
    id_seleccionado = request.form.get('id_producto')
    p = Producto.query.filter_by(id_producto=id_seleccionado).first()
    db.session.delete(p)
    db.session.commit()
    return redirect('/')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    busqueda = '%{}%'.format(request.form.get('busqueda'))
    #ilike en vez de like, evita los problemas con mayusculas y minusculas en la búsqueda.
    encontrados = Producto.query.filter(Producto.nombre.ilike(busqueda)).all()
    tarjetas = ''
    for e in encontrados:
        tarjeta = html_producto.format(
            e.nombre,
            e.descripcion,
            e.precio,
            e.stock,
            e.id_producto,
            e.id_producto
        )
        tarjetas += tarjeta
    print(tarjetas)
    return render_template('buscar.html', resultados=tarjetas)


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(debug=True)
    


