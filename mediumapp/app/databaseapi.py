#-------------------------------------------------------------------------------
# Name: medium demo app database
# Purpose: database
#
# Author:      mmk
#
# Created:     17/10/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#------------------------------------------------------------------------------
import pymongo
from datetime import datetime
#from envparse  import env
#from environs import Env


mongo_url="mongodb://mmk:mediumdatabase1@ds115592.mlab.com:15592/mediumdatabase"

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")

myclient =pymongo.MongoClient(mongo_url,connectTimeoutMs=30000)


class DataBase(object):
    ''' A Class That Stores all the database methods'''

    def __init__(self,database_name):
        #intialise the object and set properties
        self.database_name = myclient[database_name]
        self.database_collection = self.database_name["userdetails"]
        self.data_value={}
        #Properties that help in actual storing it to mongo
        self.data_storage=None
        #Properties to store the database_name as string.. to be use for unit test..
        self.database_name_string=database_name


    def insert_data(self,name_of_account,user_details,publication_details,time):
         '''Function to insert database'''

        #check if user data already in the database
        #then just update

         #check if it have the user id
         if(self.database_collection.count()>=1):
              #first get rid of all datas
               #update base on the user details
               #if(name_of_account==self.data_value['userdetails'])
               self.data_storage=self.database_collection.delete_many({})
               #insert the data
               self.data_value['userdetails']=user_details
               self.data_value['publications']=publication_details
               self.data_value['time']=time
               self.data_storage=self.database_collection.insert_one(self.data_value)

               pass
        #else insert the data
         else:
             #insert  datas
             self.data_value['userdetails']=user_details
             self.data_value['publications']=publication_details
             self.data_value['time']=time
             self.data_storage=self.database_collection.insert_one(self.data_value)




    #function to retrive the data this will be modified to insert password to prevent anyone having acess to the database.

    def retrive_data(self):
        ''' function to return the user and publication details'''

        user_datas =list(self.database_collection.find())
        return user_datas


    #function to fetch out time and return a boolean value
    def is_greater_than_cach_time(self,new_time):
        '''method that return a boolean value determining if the time is less or greater than 5min'''
        user_data=self.retrive_data()
        #get the old time the data was inserted
        old_time=user_data[0]['time']

        time_delta = new_time - old_time
        #convert it to min
        time_checker= int((time_delta.days + time_delta.seconds)/60)
        #check if it is greater than 5 min or not
        if(time_checker<5):
            return True
        else:
            return False
    #fuction to delete the database...
    def delete_data(self):
        '''Delete entire database'''
        self.data_storage=self.database_collection.delete_many({})

    #method to check if there is a connection with the database..
    def is_it_connected_to_database(self):
        '''This method will be used mainly for unit testing database'''
        db_list=myclient.list_database_names()

        if self.database_name_string in db_list:
             return True
        else:
            return False


def main():

  pass
if __name__ == '__main__':
    main()
