#!/usr/bin/python3
"""Authentication blueprint routes"""
from web.auth import auth_bp as auth
from flask import redirect, render_template, url_for


@auth.route("/login")
def login():
    """Render login view"""
    return render_template("auth/login.html")


@auth.route("/register")
def register():
    """Render registration view"""
    return render_template("auth/register.html")


@auth.route("/login", methods=["POST"])
def login_post():
    """Log user into the application"""
    return redirect(url_for("dashboard.home"))
