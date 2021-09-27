from flask import Flask 
from flask import render_template
import glob, os.path

jkorp = Flask(__name__)

#Conseguir cache de paginas estaticas
def getCache():
    paths = glob.glob("server/templates/*.html")
    cacheDict = dict()
    with jkorp.app_context():
        for p in paths:
            base =  os.path.basename(p)
            cacheDict[base] = render_template(base)
            render_template(base)
    return cacheDict
Cache = getCache()

#Definir login handler
@jkorp.route("/login")
def login():
    return Cache["login.html"]


if __name__ == "__main__":
    jkorp.run(debug=True)
