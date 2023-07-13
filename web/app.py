#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from web.dashboard import dashboard
from web.general import general_bp
from web.auth import auth_bp

app = Flask(__name__)
app.url_map.strict_slashes = False
# Replace with strong secret key in production
app.config["SECRET_KEY"] = "dev"
app.register_blueprint(general_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard)


@app.teardown_appcontext
def dispose(_):
    """Release database connections"""
    storage.close()


@app.errorhandler(404)
def not_found(_):
    return render_template("errors/404.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
