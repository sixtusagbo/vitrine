#!/usr/bin/python3
"""Dashboard routes"""
from flask import render_template
from web.dashboard import dashboard
from flask_login import login_required, current_user


@dashboard.route("/")
@login_required
def home():
    """Dashboard home"""
    return render_template("dashboard/home.html", user=current_user)


@dashboard.route("/vixpert")
@login_required
def vixpert():
    """Stepwise form wizard"""
    return render_template("dashboard/vixpert.html", user=current_user)
