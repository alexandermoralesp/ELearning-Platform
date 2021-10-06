from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db


auth = Blueprint('auth', __name__)

@auth.route('/logout')
@login_required ## todas las funciones relacionadas a un usuario en especifico necestan login_requiered para relacionarlo a sus propiedades
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Contraseña Incorrecta.', category='error')
        else:
            flash('El correo ingresado no existe', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first() ## se inicia un query para encontrar y aliar al usuario con el correo
        if user:
            flash('Este correo ya existe', category='error')
        elif len(email) < 4:
            flash('Correo amerita ser mas largo que 3 caracteres. Invalido', category='error')
        elif len(first_name) < 2:
            flash('Nombre Invalido', category='error')
        elif password1 != password2:
            flash('Contraseñas no son iguales', category='error')
        elif len(password1) < 7:
            flash('Clave ingresada es invalida, debe ser mayor a 7 caracteres', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user) ## se genera el usuario si se pasan todas las pruebas/protocolos
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Cuenta creada!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)




