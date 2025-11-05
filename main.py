from fastapi import FastAPI
from pydantic import BaseModel
from ai_agent import generate_financial_forecast
from logger import log_forecast
import json

# ✅ Define request structure using Pydantic
class ForecastRequest(BaseModel):
    query: str

# ✅ Create FastAPI app
app = FastAPI(title="TCS Financial Forecast Agent")

@app.get("/")
def home():
    return {"message": "Welcome to TCS Financial Forecast Agent 🚀"}

@app.post("/forecast")
def forecast_endpoint(request: ForecastRequest):
    """Generate a forecast based on user query"""
    # You can access the input like: request.query
    forecast = generate_financial_forecast()

    # Log request and response
    log_forecast(request_text=request.query, forecast_output=json.dumps(forecast))

    return forecast
