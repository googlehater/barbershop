# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# DATABASE_URL = (
#     "postgresql+psycopg2://postgres:postgres@db:5432/barbershop"
# )

# engine = create_engine(
#     DATABASE_URL,
#     echo=True
# )

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models.base_model import Base

# ВНИМАНИЕ: для локальной разработки пока используем localhost
# Позже в Docker заменим на переменные окружения
DATABASE_URL = "postgresql://postgres:postgres@db:5432/barbershop"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        