from flask import Blueprint

general_bp = Blueprint('general', __name__)

from web.general.routes import *
