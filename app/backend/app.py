from flask import Flask, app
import sqlite3
import json
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2

jkorp = Flask(__name__)
jkorp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(jkorp)
app_path = os.path.dirname(os.path.realpath(__file__))

@jkorp.route('/')
def index():
    return "Hello World"

@jkorp.route('/api')
def api():
    credentials_path = app_path + '/credentials.json'
    f = open(credentials_path)
    jsonFile = json.load(f)
    return jsonFile

if __name__ == '__main__':
    jkorp.run()