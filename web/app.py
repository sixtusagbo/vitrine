#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from web.general import general_bp

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(general_bp)

@app.teardown_appcontext
def dispose(exception):
    """Release database connections"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return render_template("errors/404.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
