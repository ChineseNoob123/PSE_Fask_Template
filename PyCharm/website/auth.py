from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


# Allow Post requests
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Get Data from POST request
    data = request.form
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Some sanity Checks
        if len(email) < 4:
            flash('Email must be longer than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('Firstname must be longer than 1 characters', category='error')
        elif password2 != password1:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be longer than 6 characters', category='error')
        else:
            # Add User to Database
            flash('Account created', category='success')


    return render_template("sign_up.html")
