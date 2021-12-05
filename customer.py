from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData, create_engine,insert, select
from sqlalchemy.sql.expression import true, update
import config
from user import *

#Creating connection to the DB
engine = create_engine('sqlite:///'+config.DB_FILE)
connection = engine.connect()

# Create a metadata instance
#https://docs.sqlalchemy.org/en/14/core/reflection.html
metadata = MetaData(engine)
metadata.reflect(bind=engine)
users_table = metadata.tables['User']

class Customer(User):
    def __init(self, customerNumber, userId, userName, phoneNumber, ssn, activeStatus = True):
        super().__init__(self, userId, phoneNumber, ssn, customerNumber, activeStatus=True)
        self.customerNumber = customerNumber
        engine.execute(users_table.insert(),userName = userName,phoneNumber = phoneNumber,ssn = ssn,customerNumber = customerNumber, activeStatus=activeStatus)
    
