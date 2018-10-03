#-------------------------------------------------------------------------------
# Name:   A temporary database design using mariadb
# Purpose:     Educational
#
# Author:      mmk
#
# Created:     03/10/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriasoftconcepto>
#-------------------------------------------------------------------------------
import mysql.connector as mariadb
import dbconfiq
#established a connection the database




#create a connection method

def create_connection():
    '''This method is to create a database or connection to existing database'''
    mariadb_connection = mariadb.connect(user=dbconfiq.root_name(), password=dbconfiq.data_password())

    try:
            cursor= mariadb_connection.cursor()
            #create the database ....
            sql = "CREATE DATABASE IF NOT EXISTS meduimblogdata"
            cursor.execute(sql)
            #create the database table..........
            sql = """CREATE TABLE IF NOT EXISTS  meduimblogdata.usersdetails (
                 id INT NOT NULL AUTO_INCREMENT,
                 username VARCHAR(100) NOT NULL,
                 url VARCHAR(100) NOT NULL,
                 imageurl VARCHAR(100) NOT NULL,
                 postnumber INT ,
                 time TIMESTAMP,
                 PRIMARY KEY (id)
                                   )"""
            cursor.execute(sql);


            mariadb_connection.commit()
    finally:
        mariadb_connection.close()


#function to insert data
def retrieve_all_datas():
    ''' function that return a list of all the datas in the table'''
    mariadb_connection = mariadb.connect(user=dbconfiq.root_name(), password=dbconfiq.data_password(),db="meduimblogdata")

    try:
        query="SELECT DISTINCT HIGH_PRIORITY id,username,url,postnumber,time FROM usersdetails;"

        #prepare a cursor object using cursor() method

        cursor = mariadb_connection.cursor()
        # execute the SQL query using execute() method.
        cursor.execute (query)

        return cursor.fetchall()
    finally:
        mariadb_connection.close()



#function to update data  paramaters to be inserted...
def input_data(username,url=None,imageurl=None,postnumber=None,time=None):
    '''function that insert data to usersdetails table'''
    mariadb_connection = mariadb.connect(user=dbconfiq.root_name(), password=dbconfiq.data_password(),db="meduimblogdata")
    try:
        query="INSERT INTO usersdetails (username,url,imageurl,postnumber,time) VALUES (%s, %s) "
        # datas to be inserted
        datas=(username,url,imageurl,postnumber,time)
        #prepare a cursor object using cursor() method

        cursor = mariadb_connection.cursor()
        # execute the SQL query using execute() method.
        cursor.execute (query,datas)

        mariadb_connection.commit()

    finally:
        mariadb_connection.close()


#function to delete all data in the tables
def delete_all_data(data):
    ''''function to delete all data in the usersdetails table'''
    mariadb_connection = mariadb.connect(user=dbconfiq.root_name(), password=dbconfiq.data_password(),db="meduimblogdata")

    try:
        query = "DELETE FROM usersdetails;"

        #prepare a cursor object using cursor() method

        cursor = mariadb_connection.cursor()
         # execute the SQL query using execute() method.
        cursor.execute (query)

        mariadb_connection.commit()

    finally:
        mariadb_connection.close()


#function to query if a data is already in the database table
def query_row(field_name,value):
     ''''function to search for a particular data in the usersdetails table'''
     mariadb_connection = mariadb.connect(user=dbconfiq.root_name(), password=dbconfiq.data_password(),db="meduimblogdata")

     try:
        if field_name=="username":
            is_item_present=False
           #check if the value is in that field..
            query = "SELECT * FROM usersdetails WHERE username ='{}'".format(value)
            cursor = mariadb_connection.cursor()
         # execute the SQL query using execute() method.
            cursor.execute (query)

            data_result=cursor.fetchall()

            mariadb_connection.commit()
            #loop through the data:
            for val in data_result:
                if val==value:
                 is_item_present=True

            return is_item_present


        elif field_name=="url ":
             is_item_present=False
           #check if the value is in that field..
             query = "SELECT * FROM usersdetails WHERE url ='{}'".format(value)
             cursor = mariadb_connection.cursor()
         # execute the SQL query using execute() method.
             cursor.execute (query)

             data_result=cursor.fetchall()

             mariadb_connection.commit()
            #loop through the data:
             for val in data_result:
                if val==value:
                 is_item_present=True

             return is_item_present

        elif field_name=="imageurl":
             is_item_present=False
           #check if the value is in that field..
             query = "SELECT * FROM usersdetails WHERE imageurl ='{}'".format(value)
             cursor = mariadb_connection.cursor()
         # execute the SQL query using execute() method.
             cursor.execute (query)

             data_result=cursor.fetchall()

             mariadb_connection.commit()
            #loop through the data:
             for val in data_result:
                if val==value:
                 is_item_present=True

             return is_item_present

        elif field_name=="postnumber":
            is_item_present=False
           #check if the value is in that field..
            query = "SELECT * FROM usersdetails WHERE postnumber ='{}'".format(value)
            cursor = mariadb_connection.cursor()
         # execute the SQL query using execute() method.
            cursor.execute (query)

            data_result=cursor.fetchall()

            mariadb_connection.commit()
            #loop through the data:
            for val in data_result:
                if val==value:
                 is_item_present=True

            return is_item_present


        elif field_name=="time":
            is_item_present=False
           #check if the value is in that field..
            query = "SELECT * FROM usersdetails WHERE time ='{}'".format(value)
            cursor = mariadb_connection.cursor()
         # execute the SQL query using execute() method.
            cursor.execute (query)

            data_result=cursor.fetchall()

            mariadb_connection.commit()
            #loop through the data:
            for val in data_result:
                if val==value:
                 is_item_present=True

            return is_item_present


        else:
            return False


#function to determined the time






def main():
    pass

    create_connection()

    data=retrieve_all_datas()



    # print the rows
    for row in data :

       print (row[0], row[1], row[2],row[3],row[4],row[5])

if __name__ == '__main__':
    main()
