from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://milletsaga_user:PNUr51qtkmMYsFczfxJfU2NexgFHz0sO@dpg-cih4kedgkuvojj96qod0-a/milletsaga'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
