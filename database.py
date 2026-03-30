from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base

# SQLite database file
DATABASE_URL = "sqlite:///sewer_database2.db"

# Create the engine (connection to the DB)
engine = create_engine(
    DATABASE_URL,
    echo=True,
)

# Session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

# Create all tables in the database
def create_tables():
    Base.metadata.create_all(bind=engine)
