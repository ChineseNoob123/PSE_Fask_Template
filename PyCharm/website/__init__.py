from flask import Flask


def create_app():
    # Create Flask App
    app = Flask(__name__)
    # Encrypt site/session cookies
    app.config['SECRET_KEY'] = 'super_secret_key'

    # Register the Blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
