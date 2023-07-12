#!/usr/bin/python3
"""Intialize authentication blueprint"""
from flask import Blueprint, jsonify
from flask_httpauth import HTTPBasicAuth
from models import storage
from models.brand import Brand

auth_bp = Blueprint("authentication", __name__, url_prefix="/api/v1")
auth_bp.config = {}

auth = HTTPBasicAuth()


@auth_bp.record
def record_params(setup_state):
    """
    Logic that depends on app
    """
    app = setup_state.app
    auth_bp.config['SECRET_KEY'] = app.config['SECRET_KEY']


@auth.verify_password
def verify_password(handle_or_token, password):
    """Specify how to verify password"""
    user = Brand.verify_auth_token(handle_or_token,
                                   auth_bp.config['SECRET_KEY'])
    if not user:
        user = storage.get_brand(handle_or_token)
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@auth_bp.route('/api/token')
@auth.login_required
def get_auth_token():
    """Return new token"""
    token = g.user.generate_auth_token(auth_bp.config['SECRET_KEY'])

    return jsonify({'token': token.decode('ascii')})


@auth.error_handler
def unauthorized():
    """When user is not authorized"""
    # use 403 to prevent basic auth login popup
    return jsonify({'error': 'Unauthorized access'}), 403
