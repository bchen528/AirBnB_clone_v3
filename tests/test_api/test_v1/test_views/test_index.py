#!/usr/bin/python3
'''Tests for index'''
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import unittest
import sys
from os import getenv, remove
import pep8
import requests
from socket import *


classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


class TestIndex(unittest.TestCase):
    '''Test index'''
    """
    def setUp(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(('0.0.0.0',5000))

    def tearDown(self):
        client_socket.close()

    def test_status(self):
        '''test status function'''
        response = requests.get('http://0.0.0.0:5000/api/v1/status')
        self.assertEqual(response.json(), {'status': 'OK'})

    
    def test_count(self):
        response = requests.get('http://0.0.0.0:5000/api/v1/stats')
        self.assertEqual(response.json(), { "amenities": 13, "cities": 32, 
                                            "places": 0, "reviews": 0, 
                                           "states": 13, "users": 0})
    """

if __name__ == '__main__':
      unittest.main()
