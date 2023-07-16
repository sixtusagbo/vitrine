#!/usr/bin/python3
"""Dashboard routes"""
from flask import flash, redirect, render_template, request, url_for
import requests
from web.dashboard import dashboard
from flask_login import login_required, current_user
from web.auth import api_url


@dashboard.route("/")
@login_required
def home():
    """Dashboard home"""
    return render_template("dashboard/home.html", user=current_user)


@dashboard.route("/vixpert")
@login_required
def vixpert():
    """Stepwise form wizard"""
    return render_template("dashboard/vixpert.html", user=current_user)


@dashboard.route("/vixpert", methods=["POST"])
@login_required
def vixpert_post():
    """Update brand"""
    form_data = request.form
    data = {
        "statement": form_data.get("statement"),
        "description": form_data.get("description"),
        "address": form_data.get("address"),
        "cover_image": form_data.get("cover_image"),
        "detail_image": form_data.get("detail_image"),
        "detail_lead": form_data.get("detail_lead"),
        "detail_points": form_data.getlist("detail_point"),
        "twitter_url": form_data.get("twitter_url"),
        "whatsapp_no": form_data.get("whatsapp_no"),
        "instagram_url": form_data.get("instagram_url"),
        "telegram_url": form_data.get("telegram_url"),
        "youtube_url": form_data.get("youtube_url"),
    }
    # Remove items with empty strings
    data = {k: v for k, v in data.items() if v}

    # Call api to update the brand
    response = requests.put(
        "{}/brands/{}".format(api_url, current_user.handle),
        auth=(current_user.token, ""),
        json=data,
    )
    if response.status_code != 200:
        flash(response.json().get("error"), "error")
        return redirect(url_for("dashboard.home"))

    flash("Brand information updated successfully")
    return redirect(url_for("dashboard.home"))


@dashboard.route("/works", methods=["POST"])
@login_required
def create_work():
    """Create work"""
    form_data = request.form
    data = {
        "title": form_data["title"],
        "description": form_data["description"],
        "image_url": form_data["image_url"],
    }

    # Call api to create new work
    response = requests.post(
        "{}/brands/{}/works".format(api_url, current_user.handle),
        auth=(current_user.token, ""),
        json=data,
    )
    if response.status_code != 201:
        flash(response.json().get("error"), "error")
        return redirect(url_for("dashboard.home"))

    flash("Work created successfully")
    return redirect(url_for("dashboard.home"))


@dashboard.route("/works/<work_id>/update", methods=["POST"])
@login_required
def update_work(work_id):
    """Update work with given id"""
    form_data = request.form
    data = {
        "title": form_data["title"],
        "description": form_data["description"],
        "image_url": form_data["image_url"],
    }
    # Remove items with empty strings
    data = {k: v for k, v in data.items() if v}

    # Call api to update work
    response = requests.put(
        "{}/works/{}".format(api_url, work_id),
        auth=(current_user.token, ""),
        json=data,
    )
    if response.status_code != 200:
        flash(response.json().get("error"), "error")
        return redirect(url_for("dashboard.home"))

    flash("Work updated successfully")
    return redirect(url_for("dashboard.home"))
