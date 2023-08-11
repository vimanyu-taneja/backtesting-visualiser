from flask import Blueprint, jsonify, request

api = Blueprint("api", "api")


@api.route("update_plot")
def update_plot():
    return "This is API"
