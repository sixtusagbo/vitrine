from flask import Blueprint
from os import getenv

auth_bp = Blueprint("auth", __name__)
api_url = getenv("VIT_API_URL", "http://127.0.0.1:5001/api/v1")

from web.auth.routes import *
