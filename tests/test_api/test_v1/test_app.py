import os
from api.v1 import app
from api.v1.views import *
import unittest
import tempfile

class Config():
    DEBUG = False
    TESTING = True
    CACHE_NO_NULL_WARNING = True

class TestCase(unittest.TestCase):

    def setUp(self, ** kwargs):
        pass
        """
        config = Config()
        config.__dict__.update(kwargs)
        a = app.create_app(config)
        self.a = app.test_client()
        """
        #self.db_fd, app.config['hbnb_dev_db'] = tempfile.mkstemp()
        #app.testing = True
        #self.app = app.test_client()
        #with app.app_context():
            #app.init_db()

    def tearDown(self):
        #os.close(self.db_fd)
        #os.unlink(app.config['hbnb_dev_db'])
        pass
        

    def test_create_app(self):
        '''check app instance with blueprint is created'''
        pass 

    def test_errorhandler(self):
        '''check error message from invalid input'''
        pass
    

if __name__ == '__main__':
    unittest.main()
