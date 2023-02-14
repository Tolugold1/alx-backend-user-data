#!/usr/bin/env python3
"""flask app"""
from flask import Flask, jsonify, request
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth, _hash_password
app = Flask(__name__)


AUTH = Auth()
@app.route("/", methods=["GET"], strict_slashes=False)
def welcome_message():
    """return a json message"""
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"], strict_slashes=False)
def users(email, password):
    """register a user"""
    email = request.form.get("email")
    pwd = request.form.get("password")
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email,
        "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
