from sqlalchemy.sql.expression import false, true
from account import *
from employee import *
from user import *
import pandas as pd
import config
from print_and_log import *

#logging
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO)



##Start of the code
while True:
    print("""
Welcome to the bank system.

Plase select one option
1) Employee login
2) Customer login
3) Exit

    """)
    userchoice = int(input())
    #Employee login
    if userchoice == 1:
        while True:
            print("""
What would you like to do?

Please select one option
1)Create a new user
2)Deactivate a user
3)Activate a user
4)Create a bank account
5)Exit

            """)
            empchoice = int(input())
            if empchoice == 1:
                Input_userName = input("What is the new user's name?\n")
                Input_phoneNumber = input("What is the new user's phone number?\n")
                Input_ssn = input("What is the new user's ssn number?\n")
                Input_user_type = input("What is the user type? E for employee, C for customer.\n")
                Employee(userName=Input_userName,phoneNumber = Input_phoneNumber,ssn = Input_ssn, userType = Input_user_type)
                    
            if empchoice == 2:
                Employee.viewActiveEmpoyees()
                name = input("What is the user's name you want to deactivate?\n")
                Employee.deactivate(name)
          
            if empchoice == 3:
                Employee.viewInactiveEmpoyees()
                Employee.activate(input("What is the user's name you want to activate?\n"))     

            if empchoice == 4:
                Input_customerNumber= input("What is the customer number?\n")
                Input_accountType = input("What is the account type? C for Checking, S for Savings.\n")
                Account(customerNumber=Input_customerNumber, accountType = Input_accountType)
                print("Account was created")

            if empchoice == 5:
                exit()
    
    #Customer login
    if userchoice == 2: 
        while true:
            print("""
What would you like to do?

Please select one option.
1)Login
2)Exit
            """)
            custchoice=int(input())
            if custchoice == 1:
                print('Please enter the user number\n')
                Input_customerNumber = int(input())
                print('Please enter the account number\n')
                Input_accoutNumber = int(input())

                #incorporate try and exept here
                df_result = pd.read_sql("SELECT * from Account where accountNumber = {} and customerNumber = {}".format(Input_accoutNumber,Input_customerNumber),connection)
                # print(df_result['customerNumber'].to_list())
                if Input_accoutNumber in df_result['accountNumber'].values and Input_customerNumber in df_result['customerNumber'].values :
                    print('''
Selected customer
Customer number: {}
Account number: {}
Current balance: {}

What would you like to do?
1)Withdrawal
2)Deposit

                    '''.format(Input_customerNumber,Input_accoutNumber, df_result['balance'].values))
                    action_input=int(input())
                    
                    while true:

                        if action_input == 1:
                            withdrawal_amount = input("How much do you want to withdraw? Please enter a whole number.\n")
                            Account.withdrawl(accountNumber=Input_accoutNumber, customerNumber= Input_customerNumber, amount=withdrawal_amount)
                            break
                            
                        if action_input == 2:
                            deposit_amount = input("How much do you want to deposit? Please enter a whole number.\n")
                            Account.deposit(accountNumber=Input_accoutNumber, customerNumber= Input_customerNumber, amount = deposit_amount)
                            
                else:
                    print('The matching user and account numbers does not exist!')
                    logging.warning('Invalid bank account access by customer account: {}'.format(Input_customerNumber))
                    
    #Exit program
    if userchoice == 3:
        Account(customerNumber=3, accountType = "S")
        exit()