from flask import Flask

def create_app():
    #Create Flask App
    app = Flask(__name__)
    #Encrypt site/session cookies
    app.config['SECRET_KEY']='super_secret_key'

    return app

