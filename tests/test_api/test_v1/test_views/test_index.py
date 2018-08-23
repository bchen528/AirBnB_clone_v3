#!/usr/bin/python3
'''testing the index route'''
import unittest
import pep8
from os import getenv
import requests
import json

storage = getenv("HBNB_TYPE_STORAGE")


class TestIndex(unittest.TestCase):
    '''test index'''
    def test_status(self):
        '''test status function'''
        '''
        response = requests.get('http://0.0.0.0:5000/api/v1/status')
        self.assertEqual(response.json(), {'status': 'OK'})
        '''
        pass

    def test_count(self):
        '''test count'''
        '''
        response = requests.get('http://0.0.0.0:5000/api/v1/stats')
        r = response.json()
        for k, v in r.items():
            self.assertIsInstance(v, int)
            self.assertTrue(v >= 0)
        '''
        pass


if __name__ == '__main__':
    unittest.main()
