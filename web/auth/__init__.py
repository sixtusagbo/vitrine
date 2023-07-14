from flask import Blueprint

auth_bp = Blueprint("auth", __name__)
api_url = "http://127.0.0.1:5001/api/v1"

from web.auth.routes import *
