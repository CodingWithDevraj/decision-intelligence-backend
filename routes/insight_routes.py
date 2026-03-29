from flask import Blueprint, jsonify
from services.insight_service import get_insights

insight_bp = Blueprint("insight", __name__)

@insight_bp.route("/insights", methods=["GET"])
def insights():
    result = get_insights()
    return jsonify(result)