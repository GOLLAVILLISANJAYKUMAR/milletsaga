import re
from helper import db

class User:
    def __init__(self, user_id, username, user_password, phone_number, email):
        self.user_id = user_id
        self.username = username
        self.user_password = user_password
        self.phone_number = phone_number
        self.email = email

    def save(self):
        try:
            cur = db.connection.cursor()

            cur.execute("INSERT INTO regdb (user_id, username, user_password, phone_number, email) VALUES (%s, %s, %s, %s, %s)",
                        (self.user_id, self.username, self.user_password, self.phone_number, self.email))

            db.connection.commit()

            cur.close()

        except Exception as e:
            print(f"Error: {e}")

    def check_password(self, user_password):
        return self.user_password == user_password

    @staticmethod
    def get_user_by_id(user_id):
        try:
            cur = db.connection.cursor()

            cur.execute("SELECT * FROM regdb WHERE user_id = %s", (user_id,))

            result = cur.fetchone()
            cur.close()

            if result:
                return User(*result)

        except Exception as e:
            print(f"Error: {e}")

        return None

    @staticmethod
    def get_user_by_identifier(identifier):
        try:
            cur = db.connection.cursor()

            cur.execute("SELECT * FROM regdb WHERE user_id = %s OR phone_number = %s OR email = %s",
                        (identifier, identifier, identifier))

            result = cur.fetchone()
            cur.close()

            if result:
                return User(*result)

        except Exception as e:
            print(f"Error: {e}")

        return None

    @staticmethod
    def save_users():
        try:
            cur = db.connection.cursor()

            # Delete existing data from the regdb table
            # cur.execute("DELETE FROM regdb")

            # Insert each user into the regdb table
            for user in User.users:
                cur.execute("INSERT INTO regdb (user_id, username, user_password, phone_number, email) VALUES (%s, %s, %s, %s, %s)",
                            (user.user_id, user.username, user.user_password, user.phone_number, user.email))

            db.connection.commit()

            cur.close()

        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def load_users():
        try:
            cur = db.connection.cursor()

            cur.execute("SELECT * FROM regdb")

            fetchdata = cur.fetchall()
            cur.close()

            User.users = []  # Clear the existing users list

            for user in fetchdata:
                user_id = user['user_id']
                username = user['username']
                user_password = user['user_password']
                phone_number = user['phone_number']
                email = user['email']

                User.users.append(User(user_id, username, user_password, phone_number, email))

        except Exception as e:
            print(f"Error: {e}")
            User.users = []

    @staticmethod
    def is_valid_user_id(user_id):
        pattern = r'^[a-z_][a-z0-9_.]{2,28}[a-z0-9_]$'
        return re.match(pattern, user_id) is not None

    @staticmethod
    def is_unique_user_id(user_id):
        try:
            cur = db.connection.cursor()

            cur.execute("SELECT * FROM regdb WHERE user_id = %s", (user_id,))

            result = cur.fetchone()
            cur.close()

            return result is None

        except Exception as e:
            print(f"Error: {e}")

        return False

    @staticmethod
    def validate_password(user_password):
        pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=\[{\]};:<>|./?,-])[a-zA-Z0-9!@#$%^&*()_+=\[{\]};:<>|./?,-]{8,}$'
        return re.match(pattern, user_password) is not None

    @staticmethod
    def is_valid_username(username):
        return 3 <= len(username) <= 30

User.load_users()
