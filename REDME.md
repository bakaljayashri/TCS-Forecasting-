# 🧠 TCS Financial Forecast Agent

A FastAPI-based AI agent that analyzes recent TCS financial data and generates a structured business forecast.

---

## ⚙️ 1. Project Overview

The system simulates an AI agent that:
- Extracts quantitative data from quarterly reports
- Performs qualitative analysis of management commentary
- Synthesizes both into a **JSON forecast**
- Logs all requests and responses to a local database

### Components
| Module | Purpose |
|---------|----------|
| `ai_agent.py` | Generates forecast (dummy AI simulation) |
| `logger.py` | Saves request + result to SQLite DB |
| `main.py` | FastAPI API layer |
| `test_ai.py` | Unit test for the forecast logic |

---

## 🧩 2. Setup Instructions

### 1️⃣ Clone or Download
```bash
cd Desktop
git clone <your-repo-link>
cd "TCS Forecast AGent"
