from helper import app
from users.routes import users_bp
from waitress import serve

app.secret_key = 'your_secret_key'

app.register_blueprint(users_bp, url_prefix='/')

mode=''
if __name__=='__main__':
    if mode=='dev':
        app.run(debug=True)
    else:
        serve(app,host='0.0.0.0',port=50000,threads=4, url_prefix='/')
