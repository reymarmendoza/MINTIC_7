from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap
# libreria para usar formularios
from flask_wtf import FlaskForm
# Los formularios tienen campos , asi los importo directamente desde la libreria
from wtforms.fields import StringField, SubmitField, FormField
# desde wtf, lo que hace es validar que la informacion requerida esta completa
from wtforms.validators import DataRequired
# asi me permite invocar os para acceder a .env
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# para wtf
class LoginForm(FlaskForm):
	# uso los tipos de campo que importe de wtf
	proveedor = StringField('Proveedor', validators=[DataRequired()])
	nit = StringField('Nit', validators=[DataRequired()])
	nombre = StringField('Nombre', validators=[DataRequired()])
	telefono = StringField('Telefono', validators=[DataRequired()])
	direccion = StringField('Direccion', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	web = StringField('Web', validators=[DataRequired()])
	nuevo = SubmitField('Nuevo')
	modificar = SubmitField('Modificar')
	eliminar = SubmitField('Eliminar')
	grabar = SubmitField('Grabar')
	listar = SubmitField('Listar')
	salir = SubmitField('Salir')

class TelephoneForm(FormField):
	country_code = StringField('Country Code', validators=[DataRequired()])
	area_code = StringField('Area Code/Exchange', validators=[DataRequired()])
	number = StringField('Number')

@app.errorhandler(404)
def notFound(error):
	return render_template('404.html', error=error)

@app.route('/')
def index():
	response = make_response(redirect('/proveedor'))
	return response

@app.route('/proveedor')
def proveedor():
	# crear una instancia de la clase que cree mas arriba
	loginForm = LoginForm()
	telephoneForm = TelephoneForm()

	context = {
		'loginForm': loginForm,
		'telephoneForm': telephoneForm
	}

	return render_template('proveedor.html', **context)
	
if __name__ == '__main__':
	app.run()