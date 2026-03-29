from flask import Blueprint, jsonify
from services.root_cause_service import root_cause_analysis

root_bp = Blueprint("root", __name__)

@root_bp.route("/root-cause", methods=["GET"])
def root_cause():
    return jsonify(root_cause_analysis())