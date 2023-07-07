#!/usr/bin/python3
"""
Handles all RESTful API actions for `Brand` objects
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.brand import Brand


@app_views.route("/brands")
def brands():
    """Return in JSON all the brands on vitrine"""
    result = []

    for brand in storage.all(Brand).values():
        result.append(brand.to_dict())

    return jsonify(result)


@app_views.route("/brands/<handle>")
def brand(handle):
    """Return in JSON a brand information based on the brand's handle"""
    brand = storage.get_brand(handle)

    if not brand:
        abort(404)

    return brand.to_dict()


@app_views.route("/brands", methods=["POST"])
def create_brand():
    """Create a brand object"""
    payload = request.get_json()
    if not payload:
        abort(400, "Not a JSON")
    if "name" not in payload:
        abort(400, "Missing name")
    if "handle" not in payload:
        abort(400, "Missing handle")
    if "email" not in payload:
        abort(400, "Missing email")
    if "password" not in payload:
        abort(400, "Missing password")
    if " " in payload["handle"]:
        abort(400, "Handle contains space")
    if len(payload["handle"]) > 15:
        abort(400, "Handle is too long")
    if len(payload["name"]) > 49:
        abort(400, "Name is too long")
    if storage.get_brand(payload["handle"]):
        abort(400, "Handle is already taken")

    brand = Brand(**payload)
    brand.save()

    return jsonify(brand.to_dict()), 201
