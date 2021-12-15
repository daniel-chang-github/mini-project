import config
from sqlalchemy import create_engine, MetaData

#Creating connection to the DB
engine = create_engine('sqlite:///'+config.DB_FILE)
connection = engine.connect()

# Create a metadata instance
#https://docs.sqlalchemy.org/en/14/core/reflection.html
metadata = MetaData(engine)
metadata.reflect(bind=engine)