#!/usr/bin/python3
"""Views index: Show some statistics"""
from api.v1.views import app_views
from flask import jsonify
from models.brand import Brand
from models.detail_point import DetailPoint
from models.work import Work
from models import storage


classes = {
    "brands": Brand,
    "detail_points": DetailPoint,
    "works": Work
}


@app_views.route("/metrics")
def statistics():
    """Retrieve the number of each object in storage by type"""
    result = {}

    for key, value in classes.items():
        result[key] = storage.count(value)

    return jsonify(result)


@app_views.route("/mi_mi_show_dummy")
def dummy():
    """Display the dummy data generated with AI"""
    from os import path
    import json
    with open("/home/vagrant/vitrine/dummy_data.json", "r") as file:
        list_json = json.load(file)

    return jsonify(list_json)
