#!/usr/bin/python3
"""Intialize authentication blueprint"""
from flask import Blueprint, jsonify, g, current_app
from flask_httpauth import HTTPBasicAuth
from models import storage
from models.brand import Brand

auth_bp = Blueprint("authentication", __name__, url_prefix="/api/v1")

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(handle_or_token, password):
    """Specify how to verify password"""
    user = Brand.verify_auth_token(
        handle_or_token, current_app.config["SECRET_KEY"]
    )
    if not user:
        user = storage.get_brand(handle_or_token)
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@auth_bp.route("/token")
@auth.login_required
def get_token():
    """Return new token"""
    token = None
    if g.user.token:
        # Prevent double generation of token if token is still valid
        user = Brand.verify_auth_token(
            g.user.token, current_app.config["SECRET_KEY"]
        )
        if user:
            token = user.token

    if not token:
        token = g.user.generate_auth_token(current_app.config["SECRET_KEY"])
        g.user.token = token
        g.user.save()

    return jsonify({"token": token})


@auth_bp.route("/logout")
@auth.login_required
def logout():
    """Remove user token"""
    # unset the user's token
    g.user.token = None
    g.user.save()

    # remove current user
    g.user = None

    return jsonify({})


@auth.error_handler
def unauthorized():
    """When user is not authorized"""
    # use 403 to prevent basic auth login popup
    return jsonify({"error": "Unauthorized access"}), 403
