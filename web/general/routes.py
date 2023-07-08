from web.general import general_bp
from flask import render_template

@general_bp.route("/<handle>")
def brand(handle):
    """Return a brand's page"""
    return render_template("brand.html")
