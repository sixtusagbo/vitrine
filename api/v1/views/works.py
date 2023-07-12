#!/usr/bin/python3
"""
This module contains RESTful actions for a brand's work
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.brand import Brand
from models.work import Work
from api.v1.auth import auth


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


@app_views.route("/brands/<handle>/works", methods=["POST"])
@auth.login_required
def create_work(handle):
    """Add a work to a brand"""
    brand = storage.get_brand(handle)
    if not brand:
        abort(404)
    payload = request.get_json()
    if not payload:
        abort(400, "Not a JSON")
    if "title" not in payload:
        abort(400, "Missing title")
    if "image_url" not in payload:
        abort(400, "Missing image_url")

    work = Work(**payload)
    work.brand_id = brand.id
    work.save()

    return jsonify(work.to_dict()), 201
