#ESTE ARCHIVO SE DEBE INICIAR DESDE JKORP/ (Ex. python server/main.py)
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from sqlalchemy import func
from authlib.integrations.flask_client import OAuth, oauth_registry
import os
import sys

root_path = os.getcwd()
app = Flask(__name__, static_folder=root_path+"\\client\\static", template_folder=root_path+"\\client\\templates")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/jkorp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

app.config['SECRET_KEY'] = 'JKORP2021'

db = SQLAlchemy(app)

oauth = OAuth(app)
google = oauth.register(
    name = 'google',
    client_id="1071814098669-idi49ailgbvnlgsjgavarnoqa4skuaa8.apps.googleusercontent.com",
    client_secret="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",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'}
)

lg_manager = LoginManager(app)
@lg_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) ## siendo relacionada a user se puede acceder a sus variables

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # notes = db.relationship('Note') ## crea una relacion con notes.

db.create_all(app=app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/roadmaps")
def roadmaps():
    return render_template("roadmaps.html")

@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Usuario.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In!', category='success')
                # login_user(user, remember=True)
                session["profile"] = {"fname":user.first_name, "email": user.email}
                session.permanent = True
                return redirect("/")
            else:
                flash('Contraseña Incorrecta.', category='error')
        else:
            flash('El correo ingresado no existe', category='error')
    return render_template("login.html", user=current_user)

@app.route("/logout")
@login_required ## todas las funciones relacionadas a un usuario en especifico necestan login_requiered para relacionarlo a sus propiedades
def logout():
    logout_user()
    return redirect(url_for("/"))

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = Usuario.query.filter_by(email=email).first() ## se inicia un query para encontrar y aliar al usuario con el correo
        if user:
            flash('Este correo ya existe', category='error')
        elif password1 != password2:
            flash('Contraseñas no son iguales', category='error')
        else:
            new_user = Usuario(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            print(new_user)
            try:
                db.session.add(new_user) ## se genera el usuario si se pasan todas las pruebas/protocolos
                db.session.commit()
            except:
                db.session.rollback()
                print(sys.exc_info)
            finally:
                db.session.close()
            # login_user(new_user, remember=True)
            flash('Cuenta creada!', category='success')
            return redirect("/")

    return render_template("signup.html", user=current_user)

@app.route("/gmailauth")
def googleauth():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route("/authorize")
def authorize():
    token = oauth.google.authorize_access_token() 
    resp = oauth.google.get('userinfo')  
    user_info = resp.json()
    obj = Usuario(
        email = user_info["email"],
        password=generate_password_hash(user_info["id"], method='sha256'),
        first_name = user_info["given_name"]
    )
    try:
        db.session.add(obj)
        db.session.commit()
    except:
        db.session.rollback()
        print(sys.exc_info)
    finally:
        db.session.close()

    return redirect("/")

if __name__ =="__main__":
    app.run(debug=True)