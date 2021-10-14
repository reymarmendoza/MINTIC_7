from flask import Flask, render_template
import os

app = Flask(__name__)
# algunos navegadores agregan un / por defecto al final de la url, lo que hace fallar la ruta en flask, con esta flag se evita ese comportamiento
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/acceso', methods=['GET', 'POST'])
def acceso():
	return render_template('acceso.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
	return render_template('registro.html')

@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
	return render_template('recuperar.html')

@app.route('/usuario')
def usuario():
	return render_template('usuario.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/empleado')
def empleado():
	return render_template('empleado.html')

@app.route('/proveedores', methods=['GET', 'POST', 'DELETE'])
def proveedores():
	return render_template('proveedores.html')

@app.route('/productos', methods=['GET', 'POST', 'DELETE'])
def productos():
	return render_template('productos.html')
	
if __name__ == '__main__':
	app.run()