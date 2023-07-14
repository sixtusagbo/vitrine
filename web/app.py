#!/usr/bin/python3
from flask import Flask, render_template, session, app
import requests
from models import storage
from models.brand import Brand
from web.dashboard import dashboard
from web.general import general_bp
from web.auth import auth_bp
from flask_login import LoginManager
from web.auth import api_url
from datetime import timedelta

app = Flask(__name__)
app.url_map.strict_slashes = False
# Replace with strong secret key in production
app.config["SECRET_KEY"] = "dev"
app.register_blueprint(general_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard)
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@app.teardown_appcontext
def dispose(_):
    """Release database connections"""
    storage.close()


@app.errorhandler(404)
def not_found(_):
    return render_template("errors/404.html")


@login_manager.user_loader
def load_user(token):
    """Reload user from token stored in session"""
    response = requests.get(
        "{}/reload_brand/current".format(api_url), auth=(token, "")
    )
    return Brand(**response.json())


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=8)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
