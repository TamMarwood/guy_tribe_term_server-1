from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings

# SQLAlchemy Database URL
DATABASE_URL = settings.database_url

# Create a SQLAlchemy engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base class for SQLAlchemy models
Base = declarative_base()

# # Metadata for database
# metadata = MetaData()

# # Bind the engine to the metadata
# Base.metadata.bind = engine