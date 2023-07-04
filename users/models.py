import re
from helper import db

class User(db.Model):
    __tablename__ = 'regtb'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"User_id: {self.user_id}, Name: {self.username}, Password: {self.user_password}, Phone: {self.phone_number}, Email: {self.email}"
    
    def __init__(self,user_id, username, user_password, phone_number, email):
        self.user_id=user_id
        self.username = username
        self.user_password = user_password
        self.phone_number = phone_number
        self.email = email
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(f"Error: {e}")

    def check_password(self, user_password):
        return self.user_password == user_password

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_identifier(identifier):
        return User.query.filter(
            (User.user_id == identifier) | (User.phone_number == identifier) | (User.email == identifier)
        ).first()

    @staticmethod
    def is_valid_user_id(user_id):
        pattern = r'^[a-z_][a-z0-9_.]{2,28}[a-z0-9_]$'
        return re.match(pattern, user_id) is not None

    @staticmethod
    def is_unique_user_id(user_id):
        return User.query.filter_by(user_id=user_id).count() == 0

    @staticmethod
    def validate_password(user_password):
        pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=\[{\]};:<>|./?,-])[a-zA-Z0-9!@#$%^&*()_+=\[{\]};:<>|./?,-]{8,}$'
        return re.match(pattern, user_password) is not None

    @staticmethod
    def is_valid_username(username):
        return 3 <= len(username) <= 30
