#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.city import City
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    def test_City_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)

    def test_hasattr_city(self):
        '''
            Check if attributes exists
        '''
        new_city = City()
        self.assertTrue(hasattr(new_city, "name"))
        self.assertTrue(hasattr(new_city, "state_id"))
        self.assertTrue(hasattr(new_city, "places"))

    def test_check_tablename(self):
        '''
            Checks if the name of table is correct
        '''
        new_city = City()
        self.assertEqual(new_city.__tablename__, "cities")
