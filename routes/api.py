from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__)


@api.route("/generate_plot")
def generate_plot():
    return "<p>Sample content</p>"
