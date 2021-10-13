from flask import Flask, request, make_response, redirect, render_template
# asi me permite invocar os para acceder a .env
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/usuario')
def usuario():
	return render_template('usuario.html')

@app.route('/proveedores')
def proveedores():
	return render_template('proveedores.html')

@app.route('/productos')
def productos():
	return render_template('productos.html')
	
if __name__ == '__main__':
	app.run()