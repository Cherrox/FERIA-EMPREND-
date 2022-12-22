import string
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, Regexp
from Usuario import Usuario


def alfabetico(form, field):
        if not field.data.isalpha():
            raise ValidationError('El campo debe contener solo caracteres alfabéticos')

def validar_contrasena(form, field):
        if len(field.data) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres')
        if not any(char.isdigit() for char in field.data):
            raise ValidationError('La contraseña debe tener al menos un dígito')
        if not any(char.isupper() for char in field.data):
            raise ValidationError('La contraseña debe tener al menos una letra mayúscula')
        if not any(char.islower() for char in field.data):
            raise ValidationError('La contraseña debe tener al menos una letra minúscula')
        if not any(char in set(string.punctuation) for char in field.data):
            raise ValidationError('La contraseña debe tener al menos un caracter especial')

def validar_email(form, field):
    email = field.data
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario is not None:
        raise ValidationError('El correo electrónico ya está en uso')

def validar_numero_dni(form, field):
    numero_dni = field.data
    usuario = Usuario.query.filter_by(numero_dni=numero_dni).first()
    if usuario is not None:
        raise ValidationError('El número de documento ya está en uso')


def validar_dni(form, field):
        if not len(field.data) == 8:
            raise ValidationError('El DNI debe tener 8 dígitos')
        if not field.data.isdigit():
            raise ValidationError('El DNI debe contener solo dígitos')

            
class Formulario(object):
  

    class RegistroForm(FlaskForm):
        nombre = StringField('Nombre', validators=[DataRequired(), alfabetico])
        apellido = StringField('Apellido', validators=[DataRequired(), alfabetico])
        email = StringField('Email', validators=[DataRequired(), Email(), validar_email])
        contraseña = PasswordField('Contraseña', validators=[DataRequired(), EqualTo('confirmar_contraseña')])
        confirmar_contraseña = PasswordField('Confirmar contraseña')
        telefono = StringField('Teléfono', validators=[DataRequired(), Length(min=7, max=15), Regexp(r'^\+?[1-9]\d{1,14}$', message='El número de teléfono debe tener un formato válido')])
        dni = RadioField('Tipo de documento', choices=[('DNI', 'DNI'), ('LE', 'Libreta de Enrolamiento')], validators=[DataRequired()])
        numero_dni = StringField('Número de documento', validators=[DataRequired(), Regexp(r'^[0-9]{7,8}$', message='El número de documento debe tener entre 7 y 8 dígitos')])
        tipo_usuario = SelectField('Tipo de usuario', choices=[('cliente', 'Cliente'), ('emprendedor', 'Emprendedor')], validators=[DataRequired()])
        submit = SubmitField('Registrarse')

    class LoginForm(FlaskForm):
        email = StringField('Email', validators=[DataRequired(), Email()])
        contraseña = PasswordField('Contraseña', validators=[DataRequired()])
        submit = SubmitField('Iniciar sesión')
