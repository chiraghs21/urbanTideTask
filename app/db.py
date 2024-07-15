from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from app.constants import DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()
