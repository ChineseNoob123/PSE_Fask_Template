# Store the default Routes that will be usable by the server

from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


# Homepage
@views.route('/')
@login_required
def home():
    return render_template("base.html")
