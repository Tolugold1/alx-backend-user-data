#!/usr/bin/env python3
""" Session authentication"""
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User
import os


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def user_Login() -> str:
    """auth_session login"""
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    for i in user:
        if i.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(i.id)
            user_json = jsonify(i.to_json())
            user_json.set_cookie(os.getenv('SESSION_NAME'), session_id)
            return user_json
        else:
            return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """ view for route /auth_session/logout, method DELETE """
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if destroy_session is False:
        abort(404)
    else:
        return jsonify({}), 200
