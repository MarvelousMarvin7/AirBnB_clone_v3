#!/usr/bin/python3
"""index of API"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['Get'])
def status():
    """Returns status of Api in json format"""
    return jsonify({"status": "OK"})
