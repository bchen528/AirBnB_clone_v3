#!/usr/bin/python3
'''
    Package initializer
'''
from os import getenv

if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity}
#           "Review": Review}

int_types = ["number_rooms", "max_guest", "price_by_night", "number_bathrooms"]
float_types = ["latitude", "longitude"]
"""
"state_id": str, "name": str, "state_id": str,
               "place_id": str, "user_id": str, "text": str, "email": str,
               "password": str, "first_name": str, "last_name": str,
               "city_id": str, "user_id": str, "description": str,
               "number_rooms": int, "max_guest": int, "price_by_night": int,
               "latitude": float, "longitude": float, "amenity_ids": list,
               "number_bathrooms": int}
"""
storage.reload()
