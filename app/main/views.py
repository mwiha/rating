from flask import render_template, Blueprint
from app.users.forms import RegistrationForm



main= Blueprint("main",__name__)


@main.route("/")
def home():
  form= RegistrationForm()
  return render_template("index.html", form=form)