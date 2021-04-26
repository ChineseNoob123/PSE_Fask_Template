from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Create Flask App
app = Flask(__name__)
DBLoc = 'loc'

DB_NAME = "database.db"

if DBLoc == 'remote':
    # Path to Postgresql database path is postgresql://postgres:Password@host/Databasename
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/flask'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

# Disable stupid Warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def create_app():
    # Encrypt site/session cookies
    app.config['SECRET_KEY'] = 'super_secret_key'

    # Init Database

    db.init_app(app)

    # Register the Blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    # Initialize Database
    create_database(app)

    login_manager = LoginManager()
    # Where to redirect when to login
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # How to load/identify Users
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    db.create_all(app=app)
    # if not path.exists('website/' + DB_NAME):
    #     db.create_all(app=app)
    #     print('Created Database!')