#!/usr/bin/python3
'''
    Testing the file_storage module.
'''
import time
import unittest
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from os import getenv

db = getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(db != 'db', "Testing DBstorage only")
class test_DBStorage(unittest.TestCase):
    '''
        Testing the DB_Storage class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            Initializing classes
        '''
        cls.storage = DBStorage()

    @classmethod
    def tearDownClass(cls):
        '''
            delete variables
        '''
        del cls.storage

    def test_new(self):
        '''
            Test DB new
        '''
        new_obj = State(name="California")
        self.assertEqual(new_obj.name, "California")

    def test_dbstorage_user_attr(self):
        '''
            Testing User attributes
        '''
        new = User(email="melissa@hbtn.com", password="hello")
        self.assertTrue(new.email, "melissa@hbtn.com")
