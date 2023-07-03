# This helper filer is used to remove circular depencency

from flask import Flask
# from flask_mysqldb import MySQL
import psycopg2
# app = Flask(__name__)
app = Flask(__name__, instance_relative_config=False)
app.config['POSTGRES_HOST'] = 'dpg-cih4kedgkuvojj96qod0-a'
app.config['POSTGRES_USER'] = 'milletsaga_user'
app.config['POSTGRES_PASSWORD'] = 'PNUr51qtkmMYsFczfxJfU2NexgFHz0sO'
app.config['POSTGRES_DB'] = 'milletsaga'

# Establish a connection to PostgreSQL
conn = psycopg2.connect(
    host=app.config['POSTGRES_HOST'],
    user=app.config['POSTGRES_USER'],
    password=app.config['POSTGRES_PASSWORD'],
    dbname=app.config['POSTGRES_DB'])