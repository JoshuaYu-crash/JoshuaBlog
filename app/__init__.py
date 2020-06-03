from flask import Flask
from app.Admin import admin_bp
from app.User import user_bp

app = Flask(__name__)

app.config.from_pyfile('settings.py')

app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(user_bp)


@app.route("/", methods=["GET"])
def X():
    return "Hello"
