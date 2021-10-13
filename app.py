from flask import Flask, request, render_template
from markupsafe import escape 

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
@app.route('/home/')
#def inicio():
#    return '<ul><li><a href="/login">Login</a></li><li><a href="/recuperar">Recuperar datos</a></li><li><a href="/registro">registrarse</a></li></ul>'

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        # Proceso de login
        # 1. Recuperar los datos del formulario
        usr = escape(request.form['usrtxt'])
        cla = escape(request.form['pwdtxt'])
        return f"Suministraste los datos {usr} y {cla}"

@app.route('/recuperar/',methods=['GET','POST'])
def recuperar():
    if request.method=='GET':
        return render_template('recuperar.html')
    else:
        # Recuperar datos del formulario
        # Se añade el escape para evitar inyección de código
        ema = escape(request.form['ematxt']) 
        # Se realiza validación estática
        if ema=='katacastroc3@gmail.com':
            sal= f"Se han enviado las instrucciones de recuperación al correo {ema}"
        else:
            sal = "El correo suministrado no coincide con el registrado en la base de datos"
        return sal

@app.route('/registro/',methods=['GET','POST'])
def registro():
    if request.method=='GET':
        return render_template('registro.html')
    
        #return sal

if __name__=='__main__':
    app.run(debug=True)
