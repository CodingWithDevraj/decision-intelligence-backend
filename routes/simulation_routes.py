from flask import Blueprint, request, jsonify
from services.simulation_service import simulate

simulation_bp = Blueprint("simulation", __name__)

@simulation_bp.route("/simulate", methods=["GET"])
def run_simulation():
    price_change = float(request.args.get("price_change", 0))
    demand_change = float(request.args.get("demand_change", 0))

    result = simulate(price_change, demand_change)

    return jsonify(result)