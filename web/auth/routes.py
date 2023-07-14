#!/usr/bin/python3
"""Authentication blueprint routes"""
from web.auth import auth_bp as auth, api_url
from flask import flash, redirect, render_template, request, url_for
import requests
from flask_login import login_user
from models.brand import Brand


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
    # Implement login
    handle = request.form["handle"]
    password = request.form["password"]
    remember = True if request.form.get("remember") else False

    # get token with credentials from form
    response = requests.get(
        "{}/token".format(api_url), auth=(handle, password)
    )
    token = response.json().get("token")

    if response.status_code != 200 or not token:
        flash("Invalid login credentials", "error")
        return redirect(url_for("auth.login"))

    # get the user
    brand_url = "{}/brands/{}".format(api_url, handle)
    response = requests.get(brand_url, auth=(token, ""))
    user = Brand(**response.json())

    login_user(user, remember=remember)
    return redirect(url_for("dashboard.home"))
