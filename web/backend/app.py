# ESTE ARCHIVO SE DEBE INICIAR DESDE JKORP/ (Ex. python backend/main.py)
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask.helpers import url_for
from sqlalchemy.orm import backref
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, init
from flask_login import current_user, LoginManager
from authlib.integrations.flask_client import OAuth
import os
import sys

root_path = os.getcwd()
static_path = root_path + "\\frontend\\static"
template_path = root_path + "\\frontend\\templates"
app = Flask(__name__, static_folder=static_path, template_folder=template_path)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/jkorp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'JKORP2021'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id="1071814098669-idi49ailgbvnlgsjgavarnoqa4skuaa8.apps.googleusercontent.com",
    client_secret="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",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'}
)

github = oauth.register(
    name='github',
    client_id="Iv1.06e52ba8e94af6d7",
    client_secret="986dc17d6604647dbacb6563a916c2e81539de2f",
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

lg_manager = LoginManager(app)


@lg_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))


""" class Cursando(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id')) 
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id')) """


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(40), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    creador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    # alumno = db.relationship('Cursando', backref="curso") 


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    curso = db.relationship('Curso', backref="usuario")
    # cursando = db.relationship('Cursando', backref="usuario")  


# db.create_all(app=app)


@app.route("/")
def home():
    hayUsuario = session.get('profile')

    return render_template("index.html", hayUsuario=hayUsuario)


""" @app.route("/desktop")
def desktop():
    return render_template("desktop.html") """


@app.route("/roadmaps", methods=['GET', 'POST'])
def roadmaps():
    hayUsuario = session.get('profile')
    idUsuario = session.get('user_id')
    if request.method == 'POST':
        title = request.form.get("title")
        description = request.form.get("description")
        id_creador = (Usuario.query.filter_by(email=session["profile"]["email"]).first()).id
        crs = Curso(
            titulo=title, descripcion=description, creador_id=id_creador
        )
        try:
            db.session.add(crs)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info)
        finally:
            db.session.close()
        return redirect("/roadmaps")
    courses = Curso.query.all()
    return render_template("roadmaps.html", courses=courses, tamano=len(courses), hayUsuario=hayUsuario,
                           idUsuario=idUsuario)


@app.route("/login", methods=['GET', 'POST'])
def login():
    errorS = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Usuario.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                errorS = 'Logged In!'
                session["profile"] = {"name": user.first_name, "email": user.email}
                session["user_id"] = (Usuario.query.filter_by(email=email).first()).id
                session.permanent = True
                return redirect("/")
            else:
                errorS = 'Contraseña Incorrecta.'
        else:
            errorS = 'El correo ingresado no existe'
    return render_template("login.html", user=current_user, errorS=errorS)


@app.route("/removeCourse", methods=['GET', 'POST'])
def removeCourse():
    if request.method == "POST":
        course_id = request.form.get("cid")
        try:
            Curso.query.filter_by(id=course_id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info)
        finally:
            db.session.close()

    return redirect("/roadmaps")


@app.route("/logout")
def logout():
    for idS in list(session.keys()):
        session.pop(idS)
    return redirect("/")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    errorS = None
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = Usuario.query.filter_by(
            email=email).first()  ## se inicia un query para encontrar y aliar al usuario con el correo
        if user:
            errorS = 'Este correo ya existe'
        elif password1 != password2:
            errorS = 'Contraseñas no son iguales'
        else:
            new_user = Usuario(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            try:
                db.session.add(new_user)  ## se genera el usuario si se pasan todas las pruebas/protocolos
                db.session.commit()
            except:
                db.session.rollback()
                print(sys.exc_info)
            finally:
                db.session.close()
            errorS = 'Cuenta creada!'
            return redirect("/")

    return render_template("signup.html", user=current_user, errorS=errorS)


@app.route("/gmailauth")
def googleauth():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route("/authorize")
def authorize():
    token = oauth.google.authorize_access_token()
    resp = oauth.google.get('userinfo')
    user_info = resp.json()

    user = Usuario.query.filter_by(email=user_info["email"]).first()
    if not user:
        obj = Usuario(
            email=user_info["email"],
            password=generate_password_hash(user_info["id"], method='sha256'),
            first_name=user_info["given_name"]
        )
        try:
            db.session.add(obj)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info)
        finally:
            db.session.close()
    session["profile"] = user_info
    session["user_id"] = (Usuario.query.filter_by(email=user_info["email"]).first()).id

    return redirect("/")

@app.route("/gitlogin")
def gitlogin():
    redirect_url = url_for("gitauth", _external=True)
    return github.authorize_redirect(redirect_url)

@app.route("/gitauth")
def gitauth():
    token = github.authorize_access_token()
    resp = github.get('user', token=token)
    user_info = resp.json()

    user = Usuario.query.filter_by(email=user_info["login"]).first()
    if not user:
        obj = Usuario(
            email=user_info["login"],
            password=generate_password_hash(str(user_info["id"]), method='sha256'),
            first_name=user_info["login"]
        )
        try:
            db.session.add(obj)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info)
        finally:
            db.session.close()
    session["profile"] = user_info
    session["user_id"] = (Usuario.query.filter_by(email=user_info["login"]).first()).id

    return redirect('/')




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=25565)
