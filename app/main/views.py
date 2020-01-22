from flask import render_template, Blueprint
from app import db, bcrypt
from app.users.forms import RegistrationForm, LoginForm
from app.models import User



main= Blueprint("main",__name__)


@main.route("/")
def home():
  form= RegistrationForm()
  if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(
          form.password.data).decode('utf-8')
      user = User(username=form.username.data,
                  email=form.email.data, password=hashed_password)
      db.session.add(user)
      db.session.commit()
      flash('Your account has been created! You are now able to log in','success')
      return redirect(url_for('user.login'))
  login_form = LoginForm()
  if login_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
        form.password.data).decode('utf-8')
    user = User(username=form.username.data,
                email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in''success')
    return redirect(url_for('user.login'))
  return render_template("index.html", form=form, login_form=login_form)