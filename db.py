from flask_sqlalchemy import SQLAlchemy

# Configurar la base de datos
DATABASE_URI = 'mysql://username:password@server/db'

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

def init_app(app):
    # Configurar la aplicación Flask para usar la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
