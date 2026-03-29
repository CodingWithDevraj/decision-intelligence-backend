from flask import Blueprint, request, jsonify
import pandas as pd
from config.db import db

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload_data():
    try:
        # 🔍 Debug logs (VERY IMPORTANT)
        print("FILES RECEIVED:", request.files)
        print("FORM DATA:", request.form)

        # ✅ Check if file exists
        if "file" not in request.files:
            return jsonify({"error": "No file part in request"}), 400

        file = request.files["file"]

        # ✅ Check if file selected
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        # ✅ Read CSV safely
        try:
            df = pd.read_csv(file)
        except Exception as e:
            return jsonify({"error": f"CSV read error: {str(e)}"}), 400

        # ✅ Check empty data
        if df.empty:
            return jsonify({"error": "CSV file is empty"}), 400

        # ✅ Convert to JSON
        data = df.to_dict(orient="records")

        # ✅ Insert into MongoDB
        db.sales.insert_many(data)

        return jsonify({
            "message": "Data uploaded successfully",
            "records": len(data)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500