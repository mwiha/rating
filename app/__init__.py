from flask import Flask

app = Flask(__name__)



# import blueprints
from app.main.views import main
from app.users.views import users




#register bluepprints

app.register_blueprint(main)
app.register_blueprint(users)
