from sqlalchemy import MetaData, create_engine
import config

#Creating connection to the DB
engine = create_engine('sqlite:///'+config.DB_FILE)
connection = engine.connect()

# Create a metadata instance
#https://docs.sqlalchemy.org/en/14/core/reflection.html
metadata = MetaData(engine)
metadata.reflect(bind=engine)
users_table = metadata.tables['User']

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
        results = engine.execute(users_table.columns.activeStatus == True).fetchall()
        return results
    def viewInactiveUsers():
        results = engine.execute(users_table.columns.activeStatus == False).fetchall()
        return results
