from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy(app)
login_manager = LoginManager(app)