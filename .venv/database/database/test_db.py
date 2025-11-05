from database.db_config import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT DATABASE();"))
        print("✅ Connected to database:", result.fetchone())
except Exception as e:
    print("❌ Connection failed:", e)

