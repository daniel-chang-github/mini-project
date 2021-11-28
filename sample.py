import sqlite3

class bank:
    def __init__(self, bankId, name, location):
        self.bankId = bankId
        self.name = name
        self.location = location


class employee:
    def __init__(self, employeeId, employeeName, employeeStatus):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.employeeStatus = employeeStatus


class customer:
    def __init(self, customerNumber, userId, name, phoneNumber, ssn):
        self.customerNumber = customerNumber
        self.userId = userId
        self.name = name
        self.phoneNumber = phoneNumber
        self.ssn = ssn

class address:
    def __init(self, street, city, state, postalCode):
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        

class account:
    def __init__(self, accountNumber, accountType, activeStatus=False, balance = 0):
        self.accountNumber = accountNumber
        self.activeStatus = activeStatus
        ##Testing private variable but it doesn't work?
        self.balance = balance  
        self.accountType = accountType

    def withdrawl(self, amount):
        print("Current balance:{}".format(self.balance))
        if self.balance >= amount:
            self.balance -= amount
            print("Balance after withdrawl:{}".format(self.balance))
        else:
            print("Insufficient balance!")
    
    def deposit(self, amount):
        print("Current balance: {}".format(self.balance))
        self.balance += amount
        print("Balance after the deposit: {}".format(self.balance))


    @property
    def __balance(self):
        return __balance
    @__balance.setter
    def __balance(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error")
        


