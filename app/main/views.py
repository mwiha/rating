from flask import render_template, Blueprint
from app.users.forms import RegistrationForm, LoginForm



main= Blueprint("main",__name__)


@main.route("/")
def home():
  form= RegistrationForm()
  login_form = LoginForm()
  return render_template("index.html", form=form, login_form=login_form)