# ai_agent.py
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_financial_forecast():
    """
    Uses Gemini 1.5 to generate a realistic financial forecast for TCS.
    Produces a structured JSON output with all key forecast details.
    """

    prompt = """
    You are an expert financial analyst.
    Based on Tata Consultancy Services' recent quarterly results and IT services industry trends,
    generate a realistic forecast for the next quarter.

    Include these fields only (in valid JSON format):
    {
      "company": "Tata Consultancy Services (TCS)",
      "forecast_date": "<current date>",
      "expected_revenue_growth": "<percentage like 10.5%>",
      "expected_operating_margin": "<percentage like 24.8%>",
      "management_sentiment": "<Positive/Neutral/Negative>",
      "key_risks": ["...","..."],
      "key_opportunities": ["...","..."],
      "summary": "<3-4 line summary>"
    }

    Return ONLY JSON — no explanations.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content(prompt)
        raw_output = response.text.strip()

        # Attempt to parse JSON
        try:
            forecast = json.loads(raw_output)
        except json.JSONDecodeError:
            # Fallback if Gemini adds extra text
            forecast = {
                "company": "Tata Consultancy Services (TCS)",
                "forecast_date": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                "summary": raw_output
            }

        # Ensure metadata exists
        forecast.setdefault("company", "Tata Consultancy Services (TCS)")
        forecast.setdefault("forecast_date", str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        return forecast

    except Exception as e:
        return {
            "error": str(e),
            "message": "Failed to generate forecast with Gemini."
        }
