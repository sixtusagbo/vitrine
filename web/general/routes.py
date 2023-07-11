from web.general import general_bp
from flask import render_template, abort
import uuid
from models import storage

@general_bp.route("/<handle>")
def brand(handle):
    """Return a brand's page"""
    brand = storage.get_brand(handle)
    if not brand:
        abort(404)
    meta = {}

    meta["name"] = brand.name
    meta["handle"] = brand.handle
    meta["description"] = brand.description
    meta["cover_image"] = brand.cover_image
    meta["address"] = brand.address

    return render_template("brand.html", meta=meta, cache_id=uuid.uuid4(),
                           is_solopreneur=brand.is_solopreneur)
