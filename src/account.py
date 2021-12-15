from pandas.core.algorithms import value_counts
from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData, create_engine, engine,insert, select, func
from sqlalchemy.sql.expression import update
from sqlalchemy.orm import sessionmaker
import pandas as pd
import config
import db_lib
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO)


connection = db_lib.connection
engine = db_lib.engine
account_table = db_lib.metadata.tables['Account']
user_table = db_lib.metadata.tables['User']

class Account:
    def __init__(self, customerNumber, accountType, interestRate = .01, accountNumber=None, account_count=None, activeStatus=True, balance = 0):
        #Must check to see if the user exsits first.
        df_result = pd.read_sql("SELECT customerNumber from User WHERE customerNumber != 'NaN'",connection)
        if customerNumber in df_result['customerNumber']:
            self.customerNumber = customerNumber

            account_count_stmt = select([func.count()]).select_from(account_table)
            account_count = engine.execute(account_count_stmt).scalar() + 10
            self.accountNumber = account_count
            self.activeStatus = activeStatus
            ##Testing private variable but it doesn't work?
            self.balance = balance  
            self.accountType = accountType
            # stmt = "account_table.insert(),customerNumber=customerNumber,accountNumber = accountNumber, accountType=accountType, activeStatus = activeStatus,balance = balance"
            engine.execute(account_table.insert(),customerNumber=customerNumber,accountNumber = self.accountNumber, interstRate = interestRate, accountType=accountType, activeStatus = activeStatus,balance = balance)
            


    def withdrawl(customerNumber, accountNumber, amount):
        # I'm not sure how to use sqlalchemy to get the whole table. Fetchall returns a series.
        # account_info = connection.execute(select([account_table]).where(account_table.columns.accountNumber == accountNumber)).fetchall()
    
        account_info=pd.read_sql("SELECT * FROM Account WHERE accountNumber = {} and customerNumber = {}".format(accountNumber,customerNumber),connection)
        account_balance = account_info['balance'].values
        print("Current balance:{}".format(account_balance))
        if account_balance > float(amount):
            account_balance -= float(amount)
            stmt = account_table.update().where(account_table.columns.accountNumber == accountNumber).values(balance = account_balance )
            connection.execute(stmt)
            print("Balance after withdrawl:{}".format(account_balance))
            logging.info("Customer number {} withdrew $ {} from account number {}".format(customerNumber, amount, accountNumber))
        else:
            print("Insufficient balance!")
    
    def deposit(customerNumber, accountNumber, amount):
        account_info=pd.read_sql("SELECT * FROM Account WHERE accountNumber = {} and customerNumber = {}".format(accountNumber,customerNumber),connection)
        account_balance = account_info['balance'].values
        print("Current balance: {}".format(account_balance))
        account_balance += float(amount)

        print("Balance after the deposit: {}".format(account_balance))
        # # stmt=(update(account_table).where(account_table.c.accountNumber == accountNumber).values(balance = account_balance))
        stmt = account_table.update().where(account_table.columns.accountNumber == accountNumber).values(balance = account_balance )
        connection.execute(stmt)
        logging.info("Customer number {} deposited $ {} to account number {}".format(customerNumber, amount, accountNumber))        

    def viewAccounts():
        stmt = select([account_table])
        results = engine.execute(stmt)
        for result in results:
            print(result)

    # @property
    # def __balance(self):
    #     return __balance
    # @__balance.setter
    # def __balance(self,amount):
    #     if amount > 0:
    #         self.__balance += amount
    #     else:
    #         print("Error")




# Testing codes
# df_result = pd.read_sql("SELECT customerNumber from User WHERE customerNumber != 'NaN'",connection)
# if 2 in df_result['customerNumber'].to_list():
#     print("this works")

# Create a test account
# Account(customerNumber=1, accountType="C", account_count=None, activeStatus=True, balance = 0)

# View accounts
# Account.viewAccounts()

# account_info = connection.execute(select([user_table]).where(user_table.columns.customerNumber == 1)).fetchall()

# print(account_info)


# account_info = connection.execute(select([account_table]).where(account_table.columns.accountNumber == '10')).fetchall()
# account_info=pd.read_sql("SELECT * FROM Account WHERE accountNumber = 10",connection)
# print(account_info['balance'].to_string(index=False))

# print(type(account_info))
# account_balance = account_info
# print(account_balance)
# print("Current balance:{}".format(account_balance))



# amount=100
# accountNumber=10
# account_info=pd.read_sql("SELECT * FROM Account WHERE accountNumber = {}".format(accountNumber),connection)
# account_balance = account_info['balance'].values


# print("Current balance: {}".format(account_balance))
# account_balance += amount



# print("Balance after the deposit: {}".format(account_balance))

# # # stmt=(update(account_table).where(account_table.c.accountNumber == accountNumber).values(balance = account_balance))
# stmt = account_table.update().where(account_table.columns.accountNumber == accountNumber).values(balance = account_balance )
# connection.execute(stmt)


# Account(customerNumber=3, accountType = "S")