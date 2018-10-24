#-------------------------------------------------------------------------------
# Name: BASE CASE TO TEST MEDIUM API APP
# Purpose:Educational
#
# Author:      mmk
#
# Created:     23/10/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------

import unittest

import os
#from flask.ext.testing import TestCase
import app
from databaseapi import DataBase
import requests
#from project import app, db
#from project.models import User, BlogPost
from flask_testing import TestCase
import urllib.request
from datetime import datetime

database_name="mediumdatabase"
test_database=DataBase(database_name)



class BaseTestCase(unittest.TestCase):
    """A base test case."""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app=app.client_test()
        self.client=self.app.test_client()
         # propagate the exceptions to the test client
        self.app.testing = True

      #test home page response...
    def tearDown(self):
        pass


    def test_home_test(self):
        # sends HTTP GET request to the application
        # on the specified path

        response = requests.head(app.home_page_response())

        self.assertEqual(response.status_code,200)

    def test_about_page_test(self):
        # sends HTTP GET request to the application
        # on the specified path

        response = requests.head(app.about_page_response())


        self.assertEqual(response.status_code,200)

    #test for contains in the page
    def test_home_page_data(self):
        #test the contain at the home page..
        #tester = app.home()
        response=app.return_home_page_reguest()
        self.assertTrue(b'Welcome'in response.content)

    #test for contains in about page
    def test_about_page_data(self):
        #test the contain at the home page..

        response=app.return_about_page_reguest()
        self.assertTrue(b'About'in response.content)

    #test for the medium feeder type:
    def test_medium_rss_feeder(self):
        #test if the medium rss function in the app return a list
        #a default name was inserted....
        medium_type=app.medium_test()
        self.assertIs(medium_type,list)

     #test for the database is connected
    def test_database_connected(self):
        #test if there is a connection with the database.
        #tHis test return a true value if connection or false if no connection..


         self.assertTrue(test_database.is_it_connected_to_database())

    #test if  data in the database is greater than or less than
    def test_is_greater_than_cach_time(self):
        #check if data enter is less than caching time
        if(test_database.is_greater_than_cach_time(datetime.now())):

            self.assertTrue(test_database.is_greater_than_cach_time(datetime.now()))
        else:
            self.assertFalse(test_database.is_greater_than_cach_time(datetime.now()))



    #test if the database created for the app is more than 2min by inserting a dummy data type.







def main():
    pass

if __name__ == '__main__':
    unittest.main()
