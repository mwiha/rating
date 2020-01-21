from flask import render_template, Blueprint


users = Blueprint("users",__name__)


@users.route("/register")
def register():
  return render_template("register.html")