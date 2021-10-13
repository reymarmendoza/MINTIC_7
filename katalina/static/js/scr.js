// Se encarga de revelar el contrenido de un campo tipo password
function revelar() {
    // Acceder a los campos
    var pwd = document.getElementById('pwdtxt') // Recupera el elemento cuyo ID es pwdtxt
        // Revelo el campo
    pwd.type = 'text'
}

// Se encarga de ocultar el contrenido de un campo tipo password
function ocultar() {
    // Acceder a los campos
    var pwd = document.getElementById('pwdtxt') // Recupera el elemento cuyo ID es pwdtxt
        // Revelo el campo
    pwd.type = 'password'
}

// Se encarga de validar el formulario
function validar() {
    // Acceder a los campos
    var usr = document.getElementById('usrtxt') // Recupera el elemento cuyo ID es usrtxt
    var pwd = document.getElementById('pwdtxt') // Recupera el elemento cuyo ID es pwdtxt
    var msg = '';
    // aplico la svalidaciones
    if (!usr.checkValidity())
        msg += 'Usuario requerido y debe tener minimo 8 caracteres'
    if (!pwd.checkValidity())
        msg += 'Clave requerida, mínimo 8 letras'
        // Despliego el mensaje
    if (msg == '')
        msg = 'Todo esta correcto'
    alert(msg)
}
// Se encarga de registrar 
function registrar() {
    // Acceder a los campos
    var nom = document.getElementById('nomtxt') // Recupera el elemento cuyo ID es usrtxt
    var mail = document.getElementById('mailtxt') // Recupera el elemento cuyo ID es usrtxt
    var perfil = document.getElementById('perfiltxt') // Recupera el elemento cuyo ID es usrtxt
    var usr = document.getElementById('usrtxt') // Recupera el elemento cuyo ID es usrtxt
    var pwd = document.getElementById('pwdtxt') // Recupera el elemento cuyo ID es pwdtxt
    var msg = '';
    // aplico la svalidaciones
    if (!nom.checkValidity())
        msg += 'Usuario requerido'
    if (!mail.checkValidity())
        msg += 'correo requerido'
    if (!perfil.checkValidity())
        msg += 'perfil requerido'
    if (!usr.checkValidity())
        msg += 'Usuario requerido y debe tener minimo 8 caracteres'
    if (!pwd.checkValidity())
        msg += 'Clave requerida, mínimo 8 letras'
        // Despliego el mensaje
    if (msg == '')
        msg = 'Todo esta correcto'
    alert(msg)
}