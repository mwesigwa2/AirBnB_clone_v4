#!/usr/bin/python3
"""route status for api"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def return_status():
    """ Response for a successful fetch """
    return jsonify({"status": "OK"})
