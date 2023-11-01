#!/usr/bin/python3
"""users  file """
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.user import User
from datetime import datetime
import uuid


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_users():
    """Retrieves a list of all User objects"""
    list_users = []
    users = storage.all(User).values()
    for user in users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    '''Retrieves a User object'''
    all_users = storage.get(User, user_id)
    if all_users:
        return jsonify(all_users.to_dict())
    abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    '''Deletes a User object'''
    all_users = storage.get(User, user_id)
    if all_users:
        storage.delete(all_users)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    '''Creates a User'''
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def updates_user(user_id):
    """Updates a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user. key, vallue)
    user.save()
    return jsonify(user.to_dict()), 200
