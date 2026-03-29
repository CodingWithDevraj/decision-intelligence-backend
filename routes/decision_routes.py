from flask import Blueprint, jsonify
from services.decision_service import get_decisions

decision_bp = Blueprint("decision", __name__)

@decision_bp.route("/decisions", methods=["GET"])
def decisions():
    result = get_decisions()
    return jsonify(result)