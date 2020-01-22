from flask import render_template, Blueprint
from app import db, bcrypt
from app.users.forms import RegistrationForm, LoginForm
from app.models import User



main= Blueprint("main",__name__)


@main.route("/", methods=["GET", "POST"])
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
      return redirect(url_for('main.home'))
  login_form = LoginForm()
  if login_form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
          login_user(user, remember=form.remember.data)
          flash('Login successfull.', 'success')
          return redirect(url_for("main.home"))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
  return render_template("index.html", form=form, login_form=login_form)