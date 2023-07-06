#!/usr/bin/python3
"""
Database storage engine
Note: db - database
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """Handle database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize `DBStorage`"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('VIT_MYSQL_USER'),
            getenv('VIT_MYSQL_PWD'),
            getenv('VIT_MYSQL_HOST'),
            getenv('VIT_MYSQL_DB')
        ),
                                      pool_pre_ping=True
                                      )

        if getenv('VIT_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """Add new object to current db session"""
        self.__session.add(obj)

    def save(self):
        """Save all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current db session"""
        self.__session.delete(obj)

    def reload(self):
        """
        Create the database session and all tables in the database.
        """
        # create all the tables
        Base.metadata.create_all(self.__engine)

        # create database session
        session_factory = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Force SQLAlchemy to reload session
        """
        self.__session.close()
