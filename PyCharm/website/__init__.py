from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    # Create Flask App
    app = Flask(__name__)
    # Encrypt site/session cookies
    app.config['SECRET_KEY'] = 'super_secret_key'
    # Where is the Database stored
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    # Disable stupid Warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # Init Database
    db.init_app(app)

    # Register the Blueprints
    from .views import views
    from .auth import auth

    # Check that Database is initialized

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import User, Note

    return app


def create_database(app):
    # Check if Database already exists
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')