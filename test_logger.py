from logger import log_forecast, fetch_logs

# Test inserting a record
log_forecast("Predict sales for Q1", "Expected growth: 12%")

# Test fetching logs
logs = fetch_logs()
print("📋 Logs:", logs)
