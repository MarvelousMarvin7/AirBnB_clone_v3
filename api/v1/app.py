#!/usr/bin/python3
"""Implemenation of rest api"""


from api.v1.views import app_views
from flask import Flask, make_response
from flask_cors import CORS
from models import storage
import os


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(exception):
    """close storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler for 404 errors"""
    return make_response({"error": "Not found"}, 404)


if __name__ == "__main__":
    """run flask server: app"""
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
