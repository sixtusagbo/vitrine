#!/usr/bin/python3
"""
Entry point for the RESTful api that aids data access in vitrine
"""
from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from api.v1.auth import auth_bp


app = Flask(__name__)
app.url_map.strict_slashes = False
# Replace with strong secret key in production
app.config['SECRET_KEY'] = 'dev'
app.register_blueprint(app_views)
app.register_blueprint(auth_bp)

CORS(app, origins=["*"])
host = getenv("VIT_API_HOST", "0.0.0.0")
port = getenv("VIT_API_PORT", "5000")


@app.teardown_appcontext
def teardown(exception):
    """Cleanup opearations"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(400)
def invalid_request(error):
    return jsonify({"error": error.description}), 400


if __name__ == "__main__":
    app.run(host, port, threaded=True, debug=True)
