#!/usr/bin/python3
'''
    Define class DatabaseStorage
'''
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from models.state import State
from models.city import City


class DBStorage:
    '''
        Create SQLalchemy database
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            Create engine and link to MySQL databse (hbnb_dev, hbnb_dev_db)
        '''
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        engine = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db),self.__ pool_pre_ping=True)
        self.__session = Base.metadata.create_all(self.__engine)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(bind=engine)
        self.__session = Session()

    def all(self, cls=None):
        '''
            Query current database session
        '''
        db_dict = {}
        classes = Bases.metatable.tables.keys():
        if cls is None:
            for c in classes:
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    db_dict[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
        return (db_dict)

    def new(self, obj):
        '''
            Add object to current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Commit all changes of current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            Delete from current database session
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
            Commit all changes of current database session
        '''
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
