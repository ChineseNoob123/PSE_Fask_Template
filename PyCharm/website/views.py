# Store the default Routes that will be usable by

from flask import Blueprint, render_template

views = Blueprint('views', __name__)


# Homepage
@views.route('/')
def home():
    return render_template("base.html")
