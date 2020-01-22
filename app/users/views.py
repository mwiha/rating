from flask import render_template, Blueprint
from app.users.forms import RegistrationForm


users = Blueprint("users",__name__)


@users.route("/register")
def register():
  return render_template()