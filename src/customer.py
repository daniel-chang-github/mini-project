from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData, create_engine,insert, select
from sqlalchemy.sql.expression import true, update
import config
from user import *

import db_lib

connection = db_lib.connection
engine = db_lib.engine
user_table = db_lib.metadata.tables['User']

class Customer(User):
    def __init(self, customerNumber, userId, userName, phoneNumber, ssn, activeStatus = True):
        super().__init__(self, userId, phoneNumber, ssn, customerNumber, activeStatus=True)
        self.customerNumber = customerNumber
        engine.execute(user_table.insert(),userName = userName,phoneNumber = phoneNumber,ssn = ssn,customerNumber = customerNumber, activeStatus=activeStatus)
    
