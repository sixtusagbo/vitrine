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
        item = brand.to_dict()
        item["detail_points"] = []
        for detail_point in brand.detail_points:
            item["detail_points"].append(detail_point.content)
        result.append(item)

    return jsonify(result)
