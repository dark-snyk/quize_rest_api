from flask import Flask
from api import leaders, registration, test_process
# library that allows to interact flask with db
from flask_sqlalchemy import SQLAlchemy
from database.models import db



# create main object for future interactions
app = Flask(__name__)

# set up config and path for db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"

# connect db to certain application
db.init_app(app)

# registration of components
app.register_blueprint(leaders.leaders_bp)
app.register_blueprint(registration.registration_bp)
app.register_blueprint(test_process.test_bp)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)
