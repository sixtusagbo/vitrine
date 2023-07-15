#!/usr/bin/python3
"""Routes for the general blueprint"""
from web.general import general_bp
from flask import render_template
import uuid


@general_bp.route("/<handle>")
def brand(handle):
    """Return a brand's page"""
    return render_template("brand.html", cache_id=uuid.uuid4())
