from flask import Blueprint, render_template, request, session, redirect
from users.models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@users_bp.route('/signup', methods=['POST'])
def signup():
    user_id = request.form['user_id'].lower()
    username = request.form['username']
    user_password = request.form['password']
    confirm_password = request.form['confirm_password']
    phone_number = request.form['phone_number']
    email = request.form['email']

    if not User.is_valid_user_id(user_id):
        return render_template('signup_failed.html',
                               message='Invalid user ID. User ID must start with a lowercase character or underscore, '
                                       'can end with a lowercase character, underscore, or number, and can contain '
                                       'lowercase alphanumeric characters, underscores, and periods in the middle. '
                                       'Length: 4-30')

    if not User.is_unique_user_id(user_id):
        return render_template('signup_failed.html', message='User ID already exists. Please choose a different user ID.')

    if not User.validate_password(user_password):
        return render_template('signup_failed.html', message='Invalid password. Password must be at least 8 characters '
                                                             'long and contain at least one digit, one uppercase '
                                                             'letter, one lowercase letter, and one special character.')

    if user_password != confirm_password:
        return render_template('signup_failed.html', message='Password and confirm password do not match. Please re-enter the password.')

    if not User.is_valid_username(username):
        return render_template('signup_failed.html', message='Invalid username. Username must be a minimum of 3 characters and a maximum of 30 characters.')

    new_user = User(user_id, username, user_password, phone_number, email)
    new_user.save()

    session['user_id'] = new_user.user_id
    return redirect('/home')

@users_bp.route('/login', methods=['POST'])
def login():
    login_identifier = request.form['login_id']
    user_password = request.form['password']

    user = User.get_user_by_identifier(login_identifier)

    if user is None or not user.check_password(user_password):
        return render_template('login_failed.html', message='Invalid credentials. Please try again.')

    session['user_id'] = user.user_id
    return redirect('/home')

@users_bp.route('/home')
def home():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.get_user_by_id(user_id)

        if user:
            return render_template('home.html', user=user)

    return redirect('/')

@users_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')
