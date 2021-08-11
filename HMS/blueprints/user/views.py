# from flask import request, flash, redirect, url_for
# from flask.templating import render_template
# from hms.blueprints.user import user
# from hms.blueprints.user.forms import (LoginForm, RegisterForm, UpdateEmailForm, 
#                                                             UpdatePasswordForm,PasswordResetForm, ChangePasswordForm)
# from flask_login import login_user, logout_user, login_required, current_user
# from lib.safe_url import safe_next_url
# from hms.blueprints.user.model import User
# from hms.extensions import db
# from hms.email import send_confirmation_mail


# @user.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.find_by_identity(email = form.email.data)
#         if user and user.verify_password(form.password.data):
#             flash(f"You are now logged in as {form.email.data}", 'success')
#             if login_user(user, form.remember_me.data) and user.is_active():
#                 next_page = request.args.get('next')
#                 if next_page: 
#                     return redirect(safe_next_url(next_page) or url_for('page.home'))
#             else:
#                 flash("Your account has been disable, please contact customer support for assistance", "info")
#         elif user is None:
#             flash("There is no account with this email, please register to access this page.", 'info')
#         else:
#             flash("Incorrect password or email", "error")
#     return render_template("user/login.html", form = form )


# @user.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash("You are logged out", "success")
#     return redirect(url_for('user.login'))

# @user.route('/register', methods=['GET', 'POST'])
# def register():
#         form = RegisterForm()

#         if form.validate_on_submit():
#             user = User(email=form.email.data, firstname=form.first_name.data, 
#                         lastname = form.last_name.data, password = form.password.data )
#             db.session.add(user)
#             db.session.commit()
#             token = user.serialize_confirmation_token()
#             send_confirmation_mail(email, 'auth/email/index', user=user, token=token )
#             flash("Registration successful", 'success')
#             return redirect(url_for('user.login'))
#         return render_template('page/register.html', form=form)
            

# @user.route('/confirm/<token>')
# @login_required
# def confirm_token(token):
#     if user.confirmed:
#         return redirect(url_for('page.home'))
#     if current_user.disserialize_confirmation_token(token):
#         flash('Your account has successfully being confirmed', 'success')
#     else:
#         flash("The confirmation link is invalid or expired", 'error')
#     return redirect(url_for('page.home')) 


# @user.before_app_request 
# def before_request():
#     if current_user.is_authenticated() and not current_user.confirmed and request.endpoint[:5] != 'user.':
#         return redirect(url_for('user.unconfirmed'))

# @user.route('/unconfirmed')
# def unconfimed():
#     if current_user.is_anonymous() or current_user.confirmed:
#         return redirect(url_for('page.home'))
#     return render_template('page/unconfirmed.html')


# @user.route('/resend_confirmation')
# @login_required
# def resend_confirmation():
#     token = current_user.serialize_confirmation_token()
#     send_confirmation_mail(current_user.email, 'auth/email/index', user=user, token=token )
#     flash("A new confirmation link has been sent to your account by email", 'success')
#     return redirect(url_for('page.home'))


# @user.route('/update_password', methods=['GET', 'POST'])
# @login_required
# def update_password():
#     form = ChangePasswordForm()
#     if form.validate_on_submit():
#         previous_password = form.old_password.data
#         new_password = form.new_password.data

#         if current_user.verify_password(previous_password):
#             current_user.password = current_user.passsword(new_password)
#             db.session.commit()
#             flash("You have successfully updated your password")
#         else:
#             flash("Incorrect password", 'error')
#         return redirect(url_for('user.settings'))
#     return redirect(url_for("user.update_credentials.html"), form=form )

# @user.route('/settings')
# @login_required
# def settings():
#     '''Showing the user settings page'''
#     return render_template("page/settings.html")


# @user.route('/password_reset', methods=['GET', 'POST'])
# def password_reset():
#     form = PasswordResetForm()
#     if form.validate_on_submit():
#         email = User.query.filter_by(email = form.email.data).first()
#         if email:
#             token = current_user.generate_reset_password()
#             send_confirmation_mail(current_user.email, 'auth/email/password_reset', token=token)
#             flash('Check your email for a new password reset link.', 'success')
#             return redirect(url_for('user.login'))
#     return render_template('page/password_reset.html', form=form)

# @user.route('/change_password/<token>', methods=['GET', 'POST'])
# def change_password(token):
#     form = ChangePasswordForm()
#     if form.validate_on_submit():
#         user = User.reset_pasword(token)
#         new_password = form.new_password
#         if user is not None:
#             user.password = new_password
#             db.session.commit()
#             flash('Your password has been change successfully.', 'success')
#             return redirect(url_for('user.login'))
#         else:
#             return redirect(url_for('user.register'))
#     return render_template('page/changepassword.html', form=form)


# @user.route('/request_update_email', methods=['GET', 'POST'])
# @login_required
# def request_update_email():
#     form = UpdateEmailForm()
#     if form.validate_on_submit():
#         new_email = form.email.data
#         if current_user.verify_password(form.password.data):
#             token = current_user.generate_email_token()
#             send_confirmation_mail(new_email, 'confirmation email', 'auth/email/index', token=token)
#             flash("A confirmation link has been sent to your email", "success")
#             return redirect(url_for('user.settings'))
#         else:
#             flash("Invalid password, please input a correct password.", 'danger')
#     return render_template('page/update_email.html', form = form )


# @user.route('/confirm_email_update/<token>')
# @login_required
# def confirm_email_update(token):
#     if current_user.confirm_email_update(token):
#         db.session.commit()
#         flash("Your email has been updated", 'success')
#     else:
#         flash('Invalid request...')

#     return redirect(url_for('user.settings'))