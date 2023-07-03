from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://milletsaga_user:PNUr51qtkmMYsFczfxJfU2NexgFHz0sO@dpg-cih4kedgkuvojj96qod0-a/milletsaga'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Regtb(db.Model):
    __tablename__ = 'regtb'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __init__(self, user_id,username,password,phone_number,email):
        self.user_id=user_id
        self.username=username
        self.password=password
        self.phone_number=phone_number
        self.email=email



