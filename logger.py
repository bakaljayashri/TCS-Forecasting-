import sqlite3
import os

DB_PATH = os.path.join("database", "tcs_forecast.db")

def log_forecast(request_text, forecast_output):
    """Save a forecast request and result to the database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO logs (request_text, forecast_output)
            VALUES (?, ?)
        """, (request_text, forecast_output))

        conn.commit()
        conn.close()
        print("✅ Log saved successfully!")

    except Exception as e:
        print("❌ Error saving log:", e)


def fetch_logs():
    """Retrieve all logs from the database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM logs ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()
        return rows

    except Exception as e:
        print("❌ Error fetching logs:", e)
        return []
