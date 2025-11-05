import os
import sqlite3

def test_connection():
    try:
        db_path = os.path.join("database", "tcs_forecast.db")

        # Ensure folder exists
        os.makedirs("database", exist_ok=True)

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        print("✅ Database connected successfully!")

        # Create table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_text TEXT,
            forecast_output TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        conn.commit()
        print("📋 Table 'logs' is ready!")

        conn.close()

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    test_connection()
