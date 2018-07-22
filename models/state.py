#!/usr/bin/python3
'''
    Implementation of the State class
'''
import os
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
    else:
        name = ""
