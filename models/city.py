#!/usr/bin/python3
'''
    Define the class City.
'''
import os
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
#from models.state import State

class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""
