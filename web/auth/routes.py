#!/usr/bin/python3
"""Authentication blueprint routes"""
from web.auth import auth_bp as auth
from flask import render_template


@auth.route("/login")
def login():
    """Render some content"""
    return render_template("auth/login.html")


@auth.route("/register")
def register():
    """Render some content"""
    return render_template("auth/register.html")
