#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
import os
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = "users"
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
