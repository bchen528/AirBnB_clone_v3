#!/usr/bin/python3
'''
    Testing the file_storage module.
'''
import time
import unittest
import sys
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models import storage
from console import HBNBCommand
from os import getenv
from io import StringIO

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
        cls.dbstorage = DBStorage()
        cls.output = StringIO()
        sys.stdout = cls.output
    @classmethod
    def tearDownClass(cls):
        '''
            delete variables
        '''
        del cls.dbstorage

    def create(self):
        '''
            Create HBNBCommand()
        '''
        return HBNBCommand()

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

    def test_dbstorage_check_method(self):
        '''
            Check methods exists
        '''
        self.assertTrue(hasattr(self.dbstorage, "all"))
        self.assertTrue(hasattr(self.dbstorage, "__init__"))
        self.assertTrue(hasattr(self.dbstorage, "new"))
        self.assertTrue(hasattr(self.dbstorage, "save"))
        self.assertTrue(hasattr(self.dbstorage, "delete"))
        self.assertTrue(hasattr(self.dbstorage, "reload"))

    def test_dbstorage_all(self):
        '''
            Testing all function
        '''
        storage.reload()
        result = storage.all("")
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)
        new = User(email="adriel@hbtn.com", password="abc")
        console = self.create()
        console.onecmd("create State name=California")
        result = storage.all("State")
        self.assertTrue(len(result) > 0)

"""
        x = (self.output.getvalue())
        print(x)

        console.onecmd("create User email=adriel@hbnb.com password=abc")
        self.storage.save()
        result = self.storage.all("User")
        print(result)5A
"""
