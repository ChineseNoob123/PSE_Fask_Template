from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Database
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    # Create Flask App
    app = Flask(__name__)
    # Encrypt site/session cookies
    app.config['SECRET_KEY'] = 'super_secret_key'
    # Where is the Database stored
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    # Init Database
    db.init_app(app)

    # Register the Blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
