# Decision Intelligence Backend

This repository implements a backend system for a Decision Intelligence Platform that enables data-driven business decision-making through analytics, simulation, and optimization.

The system is designed to process structured datasets and expose a set of RESTful APIs that support descriptive, diagnostic, predictive, and prescriptive analytics.

---

## Live Service

Base URL:
https://decision-intelligence-backend-h6lw.onrender.com

---

## System Objective

The backend transforms raw tabular data into meaningful business outputs by:

- Computing key performance metrics
- Identifying patterns and anomalies
- Simulating business scenarios
- Optimizing decision variables
- Generating actionable recommendations

---

## Core Capabilities

### Data Ingestion
- Accepts CSV input via API
- Parses and validates data using Pandas
- Stores records in MongoDB for persistent access

### Analytical Processing
- Computes revenue and profit metrics
- Performs aggregation across product and regional dimensions
- Enables dynamic recalculation on demand

### Decision Intelligence
- Converts analytical outputs into prescriptive recommendations
- Identifies high-impact business actions

### Scenario Simulation
- Models price and demand changes
- Applies transformation logic to evaluate outcomes under varying conditions

### Optimization Engine
- Iterates over multiple parameter combinations
- Selects optimal strategy based on profit maximization

### Root Cause Analysis
- Detects underperforming segments
- Surfaces key drivers behind performance variations

### Forecasting
- Estimates future performance using trend-based projection

### Comparative Evaluation
- Supports multi-scenario comparison for decision validation

---

## API Endpoints

| Endpoint | Method | Description |
|--------|--------|-------------|
| /api/upload | POST | Upload dataset |
| /api/insights | GET | Retrieve key metrics |
| /api/decisions | GET | Get recommendations |
| /api/simulate | GET | Run scenario simulation |
| /api/strategy | GET | Get optimized strategy |
| /api/root-cause | GET | Diagnose performance issues |
| /api/forecast | GET | Predict future revenue |
| /api/compare | GET | Compare multiple scenarios |

---

## Data Model Assumptions

The system operates on structured tabular data with the following conceptual fields:

- Product identifier
- Unit price
- Quantity or demand
- Geographic segment (region)
- Unit cost

These fields enable computation of core business metrics such as revenue and profit.

---

## Processing Pipeline

1. Data ingestion via API
2. Storage in MongoDB
3. Retrieval and conversion to DataFrame
4. Metric computation and transformation
5. Execution of analytical or simulation logic
6. Response generation in JSON format

---

## Technology Stack

Backend Framework:
- Flask

Data Processing:
- Pandas
- NumPy

Database:
- MongoDB Atlas

Deployment:
- Render

Development Tools:
- Postman
- Git

---

## Code Structure

backend/
- config/
  - db.py
- routes/
  - upload_routes.py
  - insight_routes.py
  - decision_routes.py
  - simulation_routes.py
  - strategy_routes.py
  - root_cause_routes.py
  - forecast_routes.py
  - compare_routes.py
- services/
  - insight_service.py
  - decision_service.py
  - simulation_service.py
  - strategy_service.py
  - root_cause_service.py
  - forecast_service.py
  - compare_service.py
- app.py

---

## Design Considerations

- Separation of concerns between routing and business logic
- Stateless API design for scalability
- Modular service architecture for extensibility
- Data-driven computation for dynamic outputs

---

## Setup

Clone repository:

git clone <repo-url>
cd backend

Install dependencies:

pip install -r requirements.txt

Set environment variables:

MONGO_URI=your_connection_string

Run server:

python app.py

---

## Deployment Notes

The application is deployed using a production WSGI server:

- gunicorn app:app

Hosted on Render with environment-based configuration.

---

## Future Work

- Integration of advanced machine learning models
- Automated schema detection and validation
- Real-time analytics support
- Role-based access control
- Scalable microservices architecture

---

## Author

Devraj Choudhary
