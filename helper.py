# This helper filer is used to remove circular depencency

from flask import Flask
from flask_mysqldb import MySQL

# app = Flask(__name__)
app = Flask(__name__, instance_relative_config=False)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'flask_meemit'
mysql = MySQL(app)