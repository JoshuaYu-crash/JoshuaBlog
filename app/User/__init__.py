from flask import Blueprint

user_bp = Blueprint('user', __name__)

import app.User.views
