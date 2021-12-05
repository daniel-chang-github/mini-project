from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData, create_engine,insert, select, func
from sqlalchemy.engine import result
from sqlalchemy.sql.expression import true, update
import config
import pandas as pd
from user import *

#Creating connection to the DB
engine = create_engine('sqlite:///'+config.DB_FILE)
connection = engine.connect()

# Create a metadata instance
#https://docs.sqlalchemy.org/en/14/core/reflection.html
metadata = MetaData(engine)
metadata.reflect(bind=engine)
users_table = metadata.tables['User']
account_table = metadata.tables['Account']

class Employee(User):  
    def __init__(self, userName, phoneNumber, ssn, userType ,employeeNumber=None, customerNumber = None , activeStatus=True):
        # super().__init__(self, userName, phoneNumber, ssn, customerNumber, userType, activeStatus=True)
        # self.employeeNumber = employeeNumber  
        try:
            #A unique customer number or employee number is automatically assigned based on how many employees or customers exist in the user table. Increment of 1.
            if userType.upper() == "E":
                #This is to assgin unique customer# based on the exsiting customers
                stmt = select([func.count()]).select_from(users_table).where(users_table.columns.userType == "E")
                result = engine.execute(stmt).scalar() + 1
                engine.execute(users_table.insert(),userName = userName,phoneNumber = phoneNumber,ssn = ssn, userType = userType.upper(), employeeNumber  = result, activeStatus=activeStatus)
                print("New employee {} was added \nThe employee id is {}".format(userName,result))
            if userType.upper() =="C":
                #This is to assgin unique exmployees# based on the exsiting exmployees
                stmt = select([func.count()]).select_from(users_table).where(users_table.columns.userType == "C")
                result = engine.execute(stmt).scalar() + 1
                engine.execute(users_table.insert(),userName = userName,phoneNumber = phoneNumber,ssn = ssn, userType = userType.upper(), customerNumber= result, activeStatus=activeStatus)
                print("""New customer {} was added \nThe user id is {}""".format(userName, result))
        except:
            print("Invalid input was entered!")

    def viewActiveEmpoyees():
        stmt = select([users_table])
        stmt = stmt.where(users_table.columns.activeStatus == True)
        for result in engine.execute(stmt):
            print(result)
    
    def viewInactiveEmpoyees():
        stmt = select([users_table])
        stmt = stmt.where(users_table.columns.activeStatus == False)
        for result in engine.execute(stmt):
            print(result)
    
    #List all accounts
    def viewAllAccount():
        # stmt = select([account_table])
        # results = engine.execute(stmt).fetchall()
        # print(results)
        results = pd.read_sql("SELECT * FROM Account",connection)
        print(results)

    #Deactivate a user
    def deactivate(user_name):
        Update_statement= users_table.update().\
        values(activeStatus=False).\
        where(users_table.columns.userName == user_name)
        engine.execute(Update_statement)
    #re-activate a user.
    def activate(user_name):
        Update_statement= users_table.update().\
        values(activeStatus=True).\
        where(users_table.columns.userName == user_name)
        engine.execute(Update_statement)
