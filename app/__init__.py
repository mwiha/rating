from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "efec7e52ccb4a3e86ec302b43fce90fa1c167ba1"



# import blueprints
from app.main.views import main
from app.users.views import users




#register bluepprints

app.register_blueprint(main)
app.register_blueprint(users)
