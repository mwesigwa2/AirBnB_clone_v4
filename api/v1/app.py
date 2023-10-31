#!/usr/bin/python3
"""Flask api application"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

pp.url_map.strict_slashes = False
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
