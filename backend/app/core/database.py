
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models.base_model import Base
import os

os.load_dotenv()


engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        