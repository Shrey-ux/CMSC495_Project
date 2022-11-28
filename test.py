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
    # You can replace the server name with outward TCP IP address to deploy globally
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-62CDVC6\SQLEXPRESS01;'
                          'Database=MDFootballCamp;'
                          'UID=tyler;'
                          'PWD=password;')


def insertToDB():

    valueLS = str(" ('Dhaval', 'Patel', 'dpatel', 'dpatel@gmail.com', '2676165627', '2010-01-01', '5111 Westland', '', 'Arbutus', 'Maryland', '21226', 'qb_event', 'Tyler', 'Smith', '1234567890', 'Friend','No', 'password') ")

    insert_db = str(" INSERT INTO [dbo].[MDFOOTBALLCAMP] " +
                    " ([firstname] ,[lastname] ,[username] ,[email] ,[phone_number] ,[birthdate] ,[address] ,[address2] " +
                    " ,[city] ,[state] ,[zip] ,[event] ,[ec_firstname] ,[ec_lastname] ,[ec_phone_number] ,[relationship_to_athlete] " +
                    " ,[staff_user] ,[password]) VALUES " + valueLS)


def main():
    databaseConnect()
    temp = "select * from Users"

    df = pd.read_sql_query(temp, conn)

    conn.execute(insert_db)

    print(df)
    connectionClose()


if __name__ == '__main__':
    main()
