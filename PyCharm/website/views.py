# Store the default Routes that will be usable by

from flask import Blueprint

views = Blueprint('views', __name__)


# Homepage
@views.route('/')
def home():
    return "<h1>Test</h1>"
