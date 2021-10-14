from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
# algunos navegadores agregan un / por defecto al final de la url, lo que hace fallar la ruta en flask, con esta flag se evita ese comportamiento
app.url_map.strict_slashes = False

data = []
loginToken = "superadmin"

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/acceso', methods=['GET', 'POST'])
def acceso():
	return render_template('acceso.html')

@app.route('/accesoHandler', methods=['GET', 'POST'])
def accesoHandler():
	if request.method == 'POST':
		user = request.form['fieldUsuario']
		pwd = request.form['fieldPassword']

		# if user == os.getenv("USER") and pwd == os.getenv("USER") :
		if user == loginToken and pwd == loginToken :
			print("Login correcto")
			return render_template('registro.html')
		else :
			print("Login fallido")

	return redirect('acceso')

@app.route('/registro')
def registro():
	return render_template('registro.html')

@app.route('/registroHandler', methods=['POST'])
def registroHandler():
	if request.method == 'POST':
		# result = request.form # obtener todo el formulario
		fname = request.form['fname']
		email = request.form['email']
		profile = request.form['profile']
		user = request.form['user']
		password = request.form['password']
		confirmPwd = request.form['confirmPwd']
		
		if password == confirmPwd and len(password) >= 6:
			userForm = [fname, email, profile, user, password]
			
			valid = True
			for field in userForm :
				if field == '' :
					valid = False

			if valid :
				data.append(userForm)

		else :
			print("Contrasena no coincide")

		for i in data :
			print(i)

	return redirect('registro')

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