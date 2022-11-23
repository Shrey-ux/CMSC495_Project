import datetime
import pyodbc
import pandas as pd


def connectionClose():
    '''Close the connection to the database'''
    conn.commit()
    conn.close()


def databaseConnect():
    '''Creates a connection to the database
    can be accessed globally'''
    global conn
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-62CDVC6\SQLEXPRESS01;'
                          'Database=MDFootballCamp;'
                          'UID=tyler;'
                          'PWD=password;')


def main():
    databaseConnect()
    temp = "select * from Tyler"

    df = pd.read_sql_query(temp, conn)

    print(df)
    connectionClose()


if __name__ == '__main__':
    main()
