#!/usr/bin/python3
"""
This module contains RESTful actions for a brand's work
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort
from models.brand import Brand
from models.work import Work


@app_views.route("/brands/<handle>/works")
def works(handle):
    """Retrieve a brand's works"""
    brand = storage.get_brand(handle)
    if not brand:
        abort(404)
    result = []

    for work in brand.works:
        result.append(work.to_dict())

    return jsonify(result)
