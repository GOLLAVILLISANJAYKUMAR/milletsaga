# from helper import app
# from users.routes import users_bp
# from waitress import serve

# app.secret_key = 'your_secret_key'

# app.register_blueprint(users_bp, url_prefix='/')

# mode=''
# if __name__=='__main__':
#     if mode=='dev':
#         app.run(debug=True)
#     else:
#         serve(app,host='0.0.0.0',port=50000,threads=4, url_prefix='/')



# from helper import app
# from users.routes import users_bp
# from gunicorn.app.base import BaseApplication

# app.secret_key = 'your_secret_key'
# app.register_blueprint(users_bp, url_prefix='/')

# class FlaskApplication(BaseApplication):
#     def __init__(self, app, options=None):
#         self.options = options or {}
#         self.application = app
#         super().__init__()

#     def load_config(self):
#         for key, value in self.options.items():
#             self.cfg.set(key, value)

#     def load(self):
#         return self.application

# if __name__ == '__main__':
#     options = {
#         'bind': '0.0.0.0:5000',
#         'workers': 4
#     }

#     FlaskApplication(app, options).run()

from gunicorn.app.base import FlaskApplication

from helper import app
from users.routes import users_bp

app.secret_key = 'your_secret_key'

app.register_blueprint(users_bp, url_prefix='/')

if __name__ == '__main__':
    options = {
        'bind': '0.0.0.0:5000',
        'workers': 4
    }

    FlaskApplication(app, options).run()
