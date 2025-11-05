import random
from datetime import datetime

def generate_financial_forecast():
    """
    Simulates an AI-generated forecast for TCS.
    Later, this will connect to a real LLM or RAG pipeline.
    """
    growth = random.uniform(5, 15)
    margin = random.uniform(20, 28)
    sentiment = random.choice(["Positive", "Neutral", "Cautious"])

    forecast = {
        "company": "Tata Consultancy Services (TCS)",
        "forecast_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "expected_revenue_growth": f"{growth:.2f}%",
        "expected_operating_margin": f"{margin:.2f}%",
        "management_sentiment": sentiment,
        "key_risks": [
            "Currency fluctuations",
            "Client budget cuts",
            "Talent attrition in digital services"
        ],
        "key_opportunities": [
            "Growing demand for cloud & GenAI services",
            "Strategic partnerships with hyperscalers"
        ],
        "summary": f"TCS is expected to post around {growth:.1f}% revenue growth with stable margins near {margin:.1f}%. Overall management outlook remains {sentiment.lower()} for the next quarter."
    }

    return forecast
