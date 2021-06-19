from flask import request, flash, redirect, url_for
from flask.templating import render_template
from hms.blueprints.user import user
from hms.blueprints.user.forms import LoginForm
from flask_login import login_user, logout_user, login_required
from lib.safe_url import safe_next_url
from hms.blueprints.user.model import User

@user.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('page/register.html')


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_by_identity(email = form.email.data)
        if user and user.verify_password(form.password.data):
            flash(f"You are now logged in as {form.email.data}", 'success')
            if login_user(user, form.remember_me.data) and user.is_active():
                next_page = request.args.get('next')
                if next_page: 
                    return redirect(safe_next_url(next_page) or url_for('page.home'))
            else:
                flash("Your account has been disable, please contact customer support for assistance", "info")
        elif user is None:
            flash("There is no account with this email, please register to access this page.", 'info')
        else:
            flash("Incorrect password or email", "error")
    return render_template("user/login.html", form = form )


@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are logged out", "success")
    return redirect(url_for('user.login'))









    

