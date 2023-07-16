#!/usr/bin/python3
"""Authentication blueprint routes"""
from models.work import Work
from web.auth import auth_bp as auth, api_url
from flask import flash, redirect, render_template, request, url_for
import requests
from flask_login import login_required, login_user, current_user, logout_user
from models.brand import Brand


@auth.route("/login")
def login():
    """Render login view"""
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.home"))
    return render_template("auth/login.html")


@auth.route("/register")
def register():
    """Render registration view"""
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.home"))
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
    data = response.json()
    user = Brand(**data)
    user.works = [Work(**work) for work in data["works"]]

    # login the user
    login_user(user, remember=remember)

    # redirect appropriately
    next = request.args.get("next")
    if next:
        return redirect(next)
    return redirect(url_for("dashboard.home"))


@auth.route("/register", methods=["POST"])
def register_post():
    """Register a new user"""
    brand_data = {
        "handle": request.form["handle"],
        "name": request.form["name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "is_solopreneur": True
        if request.form.get("is_solopreneur")
        else False,
    }

    # call api to store the new user
    response = requests.post("{}/brands".format(api_url), json=brand_data)
    data = response.json()
    if response.status_code != 201:
        flash(data["error"], "error")
        return redirect(url_for("auth.register"))

    # Automatically log the user in
    user = Brand(**data)
    login_user(user, remember=True)
    return redirect(url_for("dashboard.home"))


@auth.route("/logout")
@login_required
def logout():
    """Log user out of the application"""
    # Call api to logout
    requests.get("{}/logout".format(api_url), auth=(current_user.token, ""))

    # log user out from flask_login
    logout_user()

    # redirect to login page
    return redirect(url_for("auth.login"))
