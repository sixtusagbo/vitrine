#!/usr/bin/python3
"""
Handles all RESTful API actions for `Brand` objects
"""
import os
from api.v1.views import app_views
from flask import jsonify, abort, request, g, current_app
from models import storage
from models.brand import Brand
from api.v1.auth import auth
from models.detail_point import DetailPoint
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@app_views.route("/brands")
@auth.login_required
def brands():
    """Return in JSON all the brands on vitrine"""
    result = []

    for brand in storage.all(Brand).values():
        result.append(brand.to_dict())

    return jsonify(result)


@app_views.route("/brands/<handle>")
@app_views.route("/reload_brand/<magic>")
@auth.login_required
def brand(handle=None, magic=None):
    """Return in JSON a brand information based on the brand's handle"""
    if magic == "current":
        # user is authenticated user, prevent another read request to database
        brand = g.user
    else:
        brand = storage.get_brand(handle)
        if not brand:
            abort(404)
    result = brand.to_dict(with_works=True)

    return jsonify(result)


@app_views.route("/brands/<handle>/<sentinel>")
def public_brand(handle=None, sentinel=None):
    """Return in JSON a brand information based on the brand's handle"""
    brand = storage.get_brand(handle)
    if not brand or not sentinel:
        abort(404)
    result = brand.to_dict()
    if sentinel == "public":
        # From JS or any where
        del result["password"]
        del result["token"]
        del result["id"]
    else:
        abort(403)

    return jsonify(result)


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
    brand.hash_password(payload["password"])
    brand.token = brand.generate_auth_token(current_app.config["SECRET_KEY"])
    brand.save()

    return jsonify(brand.to_dict()), 201


@app_views.route("/brands/<handle>", methods=["PUT"])
@auth.login_required
def update_brand(handle):
    """Update a brand"""
    payload = request.get_json()
    if not payload:
        abort(400, "Not a JSON")
    if "handle" in payload and " " in payload["handle"]:
        abort(400, "Handle contains space")
    if "handle" in payload and len(payload["handle"]) > 15:
        abort(400, "Handle is too long")
    if "name" in payload and len(payload["name"]) > 49:
        abort(400, "Name is too long")
    if "handle" in payload and storage.get_brand(payload["handle"]):
        abort(400, "Handle is already taken")

    brand = storage.get_brand(handle)
    if not brand:
        abort(404)
    ignore = ["id", "created_at", "updated_at", "detail_points"]

    for key, value in payload.items():
        if key not in ignore:
            setattr(brand, key, value)
    if payload.get("detail_points"):
        for value in payload["detail_points"]:
            if len(brand.detail_points) == 4:
                break
            point = DetailPoint()
            point.content = value
            brand.detail_points.append(point)
    brand.save()

    return jsonify(brand.to_dict())


@app_views.route("/brands/<handle>/email", methods=["POST"])
def send_email(handle):
    """Send contact email to a brand"""
    brand = storage.get_brand(handle)
    if not brand:
        abort(404)
    payload = request.get_json()
    if not payload:
        abort(400, "Not a JSON")
    if "name" not in payload:
        abort(400, "Missing name")
    if "email" not in payload:
        abort(400, "Missing email")
    if "message" not in payload:
        abort(400, "Missing message")
    if "site_url" not in payload:
        abort(400, "Missing site_url")

    sender = os.getenv("VIT_MAIL_SENDER", "admin@example.com")
    password = os.getenv("VIT_MAIL_PASSWORD")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Vitrine: Contact Message from {}".format(
        payload["name"]
    )
    message["From"] = sender
    message["To"] = brand.email

    text = """
    Hi {},

    Message from {}:
    {},
    {}
    """.format(
        brand.handle, payload["name"], payload["message"], payload["email"]
    )
    with open("web/templates/contact_mail.html", "r") as file:
        html_only = file.read()
    with open("web/templates/contact_styles.html", "r") as file:
        styles = file.read()
    html_only = html_only.format(
        site_url=payload["site_url"],
        message=payload["message"],
        sender_name=payload["name"],
        reply_email=payload["email"],
    )
    # Solve string format conflict with css tags issue
    html = html_only.replace("<style></style>", styles)

    # get mime objects
    text_part = MIMEText(text, "plain")
    html_part = MIMEText(html, "html")

    # Add the parts to the `message`
    # The email client will try to render the last part first
    message.attach(text_part)
    message.attach(html_part)

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, brand.email, message.as_string())

    return jsonify({"ok": True})
