from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(100), nullable=False)
    numero_dni = db.Column(db.String(100), unique=True, nullable=False)
    foto = db.Column(db.String(100))


    
class Cliente(usuario):
    pass

class Emprendedor(usuario):
    logo = db.Column(db.String(100))