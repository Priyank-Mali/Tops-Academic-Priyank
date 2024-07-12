from databaseconnector import *


def createTable():
    sql = '''CREATE TABLE Product_Manager (Name VARCHAR(255) NOT NULL,
                        Contact VARCHAR(20) NOT NULL UNIQUE ,Email VARCHAR(50) NOT NULL UNIQUE,
                        Gender VARCHAR(10) NOT NULL,City VARCHAR(30)   
            NOT NULL)'''
    mycursor.execute(sql)

    sql1 = '''CREATE TABLE Customer (Name VARCHAR(255) NOT NULL,
                        Contact VARCHAR(20) NOT NULL UNIQUE ,Email VARCHAR(50) NOT NULL UNIQUE,
                        Gender VARCHAR(10) NOT NULL,City VARCHAR(30)   
            NOT NULL)'''
    mycursor.execute(sql1)
