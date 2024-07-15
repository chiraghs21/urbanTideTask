from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from app.constants import DATABASE_URL

# Create a SQLAlchemy engine using the database URL from the constants file
engine = create_engine(DATABASE_URL)

# Initialize MetaData object for reflecting the database schema
metadata = MetaData()

# Create a configured "Session" class and instantiate a session
Session = sessionmaker(bind=engine)
session = Session()
