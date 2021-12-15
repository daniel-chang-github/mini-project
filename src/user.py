from sqlalchemy import MetaData, create_engine
import config
import db_lib

connection = db_lib.connection
engine = db_lib.engine
user_table = db_lib.metadata.tables['User']

class User:
    def __init__(self, userId, userName, phoneNumber, ssn, customerNumber, userType, activeStatus=True):
        self.userId = userId
        self.userName = userName
        self.phoneNumber = phoneNumber
        self.ssn = ssn
        self.activeStatus = activeStatus
        self.customerNumber = customerNumber
        self.userType = userType

    def viewActiveUsers():
        results = engine.execute(user_table.columns.activeStatus == True).fetchall()
        return results
    def viewInactiveUsers():
        results = engine.execute(user_table.columns.activeStatus == False).fetchall()
        return results
