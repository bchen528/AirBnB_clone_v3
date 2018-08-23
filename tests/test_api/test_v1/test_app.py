"""import os
from api.v1.app import app
from api.v1.views import *
import unittest
import tempfile


class AppTestCase(unittest.TestCase):

    def setUp(self, ** kwargs):
        a = app.test_client(host='0.0.0.0', port=5000, threaded=True)
        app.testing = True
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


    def test_errorhandler(self):
        '''check error message from invalid input'''
        pass

if __name__ == '__main__':
    unittest.main()

"""
