#!/usr/bin/python3
"""Flask api application"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, make_response
from flask import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def shutdown_everything(exception):
    """Closes and clears everything"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    ''' handles 404 error'''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    port = int(os.getenv("HBNB_API_PORT", 5000))
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    app.run(host=host, port=port, threaded=True)
