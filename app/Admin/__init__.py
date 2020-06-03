from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

import app.Admin.views
