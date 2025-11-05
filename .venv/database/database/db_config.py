from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# 🧠 Update these credentials to match your MySQL setup
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"   # change if you used a different password
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "tcs_forecast_db"

# 🔗 SQLAlchemy connection URL
DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# 🚀 Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# 🧱 Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ⚙️ Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
