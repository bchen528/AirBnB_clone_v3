#!/usr/bin/python3
'''
    Define the class City.
'''
import os
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
import models

class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""
