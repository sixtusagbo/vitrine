#!/usr/bin/python3
"""Routes for the general blueprint"""
from web.general import general_bp
from flask import flash, render_template
import uuid


@general_bp.route("/<handle>")
def brand(handle):
    """Return a brand's page"""
    return render_template("brand.html", cache_id=uuid.uuid4())


@general_bp.route("/")
def home():
    """Return the homepage"""
    return render_template("index.html", cache_id=uuid.uuid4())
