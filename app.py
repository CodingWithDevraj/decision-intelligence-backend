from flask import Flask
from flask_cors import CORS
from routes.upload_routes import upload_bp
from routes.insight_routes import insight_bp
from routes.decision_routes import decision_bp
from routes.simulation_routes import simulation_bp
from routes.strategy_routes import strategy_bp
from routes.root_cause_routes import root_bp
from routes.forecast_routes import forecast_bp
from routes.compare_routes import compare_bp

app = Flask(__name__)
CORS(app)

# Register route
app.register_blueprint(upload_bp, url_prefix="/api")
app.register_blueprint(insight_bp, url_prefix="/api")
app.register_blueprint(decision_bp, url_prefix="/api")
app.register_blueprint(simulation_bp, url_prefix="/api")
app.register_blueprint(strategy_bp, url_prefix="/api")
app.register_blueprint(root_bp, url_prefix="/api")
app.register_blueprint(forecast_bp, url_prefix="/api")
app.register_blueprint(compare_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "Decision Intelligence API Running 🚀"}

if __name__ == "__main__":
    app.run(debug=True)