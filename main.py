from gunicorn.app.wsgiapp import WSGIApplication
from helper import app
from users.routes import users_bp

app.secret_key = 'your_secret_key'
app.register_blueprint(users_bp, url_prefix='/')

if __name__ == '__main__':
    options = {
        'bind': '0.0.0.0:5000',
        'workers': 4
    }

    WSGIApplication(app).run(options)
