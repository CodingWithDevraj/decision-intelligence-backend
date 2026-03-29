from flask import Blueprint, jsonify
from services.forecast_service import forecast

forecast_bp = Blueprint("forecast", __name__)

@forecast_bp.route("/forecast", methods=["GET"])
def get_forecast():
    return jsonify(forecast())