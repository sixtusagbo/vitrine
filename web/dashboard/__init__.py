#!/usr/bin/python3
"""Initialize dashboard blueprint"""
from flask import Blueprint

dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")

from web.dashboard.index import *
