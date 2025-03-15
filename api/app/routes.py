from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)


@api_bp.route("/example", methods=["GET"])
def example():
    return jsonify({"message": "Hello from Flask API"})
