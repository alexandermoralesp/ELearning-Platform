from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
NOMBRE_DB = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{NOMBRE_DB}'
    app.config['SECRET_KEY'] = 'hdaskdjnasdk.nasdk.jasnd.kjasndkdasdasdsa'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') ## esto es para que se dirigan correctamente a 'home' por decirlo asi
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + NOMBRE_DB):
        db.create_all(app=app)
        print('Base de datos creada')