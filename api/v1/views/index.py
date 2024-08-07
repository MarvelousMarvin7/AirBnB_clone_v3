#!/usr/bin/python3
"""index of API"""

from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['Get'])
def status():
    """Returns status of Api in json format"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['Get'])
def stats():
    """retrieves the number of each objects by type"""
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
