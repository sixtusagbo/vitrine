#!/usr/bin/python3
"""
Handles all RESTful API actions for `Brand` objects
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.brand import Brand


@app_views.route('/brands')
def brands():
    """Return in JSON all the brands on vitrine"""
    result = []

    for brand in storage.all(Brand).values():
        result.append(brand.to_dict())

    return jsonify(result)


@app_views.route('/brands/<handle>')
def brand(handle):
    """Return in JSON a brand information based on the brand's handle"""
    brand = storage.get_brand(handle)

    if not brand:
        abort(404)

    return brand.to_dict()
