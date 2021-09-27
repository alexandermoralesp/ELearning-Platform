from flask import Flask, render_template, request
import glob, os.path
from flask.helpers import url_for

from werkzeug.utils import redirect

jkorp = Flask(__name__)

#Conseguir cache de paginas estaticas
def getCache():
    paths = glob.glob("server/templates/*.html")
    cacheDict = dict()
    #Para que el render_template funcione 
    with jkorp.app_context():
        for p in paths:
            base =  os.path.basename(p)
            cacheDict[base] = render_template(base)
            render_template(base)
    return cacheDict
Cache = getCache()

#Definir login handler
@jkorp.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return Cache["login.html"]
    else:
        print(request.form.get("test"))
        return redirect(url_for("login"))

#Registrarse
@jkorp.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        return Cache["register.html"]
    else:
        print(request.form.get("test"))
        return redirect(url_for("register"))

if __name__ == "__main__":
    jkorp.run(debug=True)
