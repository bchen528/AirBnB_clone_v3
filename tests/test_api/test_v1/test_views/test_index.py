#!/usr/bin/python3
import unittest
import pep8
from os import getenv
import requests

storage = getenv("HBNB_TYPE_STORAGE")


class TestIndex(unittest.TestCase):
    '''test index'''
    def test_status(self):
        '''test status function'''
        response = requests.get('http://0.0.0.0:5000/api/v1/status')
        self.assertEqual(response.json(), {'status': 'OK'})
        
    """
    def test_count(self):
        response = requests.get('http://0.0.0.0:5000/api/v1/stats')
        
        self.assertEqual(response.json(), { "amenities": 13, "cities": 32, 
                                            "places": 0, "reviews": 0, 
                                            "states": 13, "users": 0})
    """
if __name__ == '__main__':
      unittest.main()

