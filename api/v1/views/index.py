#!/usr/bin/python3
"""index of API"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['Get'])
def status():
    """Returns status of Api in json format"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['Get'])
def stats():
    """retrieves the number of each objects by type"""
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
