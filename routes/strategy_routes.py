from flask import Blueprint, jsonify
from services.strategy_service import find_best_strategy

strategy_bp = Blueprint("strategy", __name__)

@strategy_bp.route("/strategy", methods=["GET"])
def strategy():
    result = find_best_strategy()
    return jsonify(result)