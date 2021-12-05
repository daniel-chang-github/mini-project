import sqlite3
import config
connection = sqlite3.connect(config.DB_FILE)
    
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Bank (
        bankId INTEGER PRIMARY KEY, 
        name TEXT NOT NULL, 
        location TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
        userId INTEGER PRIMARY KEY, 
        userName TEXT NOT NULL,
        phoneNumber TEXT ,
        activeStatus BOOLEAN ,
        ssn TEXT,  
        userType TEXT NOT NULL,
        employeeNumber INTEGER,
        customerNumber INTERGER
        
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Account (
        accountNumber INTEGER NOT NULL,
        customerNumber INTEER NOT NULL,
        activeStatus BOOLEAN NOT NULL,
        balance FLOAT NOT NULL,
        interstRate FLOAT NOT NULL

    )
""")





connection.commit()






