#!/usr/bin/env python3
""" Session authentication"""
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
import os


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def user_Login() -> str:
    """auth_session login"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not len(email) or email is None:
        return jsonify({"error": "email missing"}), 400
    if not len(password) or password is None:
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
