from flask import Flask, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Formulario import Formulario
from Usuario import Cliente, Emprendedor
from config import Config

app = Flask(__name__)
app.config.from_object*(Config)
db = SQLAlchemy(app)



@app.route('/')
def Bienvenido():
    return render_template('index.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = Formulario.RegistroForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        contraseña = form.contraseña.data
        telefono = form.telefono.data
        dni = form.dni.data
        numero_dni = form.numero_dni.data
        tipo_usuario = form.tipo_usuario.data

        usuario = usuario(nombre=nombre, apellido=apellido, email=email, contraseña=contraseña, telefono=telefono, dni=dni, numero_dni=numero_dni)
        if tipo_usuario == 'cliente':
            cliente = Cliente(id=usuario.id, nombre=usuario.nombre, apellido=usuario.apellido, email=usuario.email, contraseña=usuario.contraseña, telefono=usuario.telefono, dni=usuario.dni, numero_dni=usuario.numero_dni)
            db.session.add(cliente)
        elif tipo_usuario == 'emprendedor':
            emprendedor = Emprendedor(id=usuario.id, nombre=usuario.nombre, apellido=usuario.apellido, email=usuario.email, contraseña=usuario.contraseña, telefono=usuario.telefono, dni=usuario.dni, numero_dni=usuario.numero_dni)
            db.session.add(emprendedor)
        db.session.add(usuario)
        db.session.commit()
        flash('Te has registrado con éxito')
        return redirect(url_for('login'))
    return render_template('registro.html', form=form)



if __name__ == '__main__':
    app.run()