#!/usr/bin/python3
"""Dashboard home routes"""
from flask import render_template
from web.dashboard import dashboard


@dashboard.route("/")
def home():
    """Dashboard home"""
    return render_template("dashboard/home.html")
