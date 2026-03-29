from flask import Blueprint, request, jsonify
from services.compare_service import compare

compare_bp = Blueprint("compare", __name__)

@compare_bp.route("/compare", methods=["GET"])
def compare_api():
    price = list(map(int, request.args.get("price").split(",")))
    demand = list(map(int, request.args.get("demand").split(",")))

    return jsonify(compare(price, demand))