from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://milletsaga_user:PNUr51qtkmMYsFczfxJfU2NexgFHz0sO@dpg-cih4kedgkuvojj96qod0-a/milletsaga'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# class Regtb(db.Model):
#     __tablename__ = 'regtb'
#     user_id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False)
#     user_password = db.Column(db.String(50), nullable=False)
#     phone_number = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(50), nullable=False)

#     def __repr__(self):
#         return f"User_id: {self.user_id}, Name: {self.username}, Password: {self.user_password}, Phone: {self.phone_number}, Email: {self.email}"
