#!/usr/bin/python3
"""
Database storage engine
Note: db - database
"""
from os import getenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.brand import Brand
from models.detail_point import DetailPoint
from models.work import Work

classes = {"Brand": Brand, "DetailPoint": DetailPoint, "Work": Work}


class DBStorage:
    """Handle database storage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize `DBStorage`"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("VIT_MYSQL_USER"),
                getenv("VIT_MYSQL_PWD"),
                getenv("VIT_MYSQL_HOST"),
                getenv("VIT_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )

        if getenv("VIT_ENV") == "test":
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
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Force SQLAlchemy to reload session
        """
        self.__session.close()

    def all(self, cls=None):
        """Return all objects"""
        result = {}

        if cls:
            # All objects that belong to class
            if type(cls) is str:
                cls = classes[cls]
            query_rows = self.__session.query(cls)
            for obj in query_rows:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj
            return result
        else:
            # All objects
            for name, value in classes.items():
                query_rows = self.__session.query(value)
                for obj in query_rows:
                    key = "{}.{}".format(name, obj.id)
                    result[key] = obj
            return result

    def get(self, cls, id):
        """Return one object using id or `None` if not found"""
        objects = self.__session.query(cls)
        for obj in objects:
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        """Return the number of objects in storage"""
        if cls:
            if type(cls) is str:
                cls = classes[cls]
            return (
                self.__session.query(func.count("*")).select_from(cls).scalar()
            )
        else:
            result = 0
            for obj in classes.values():
                result += (
                    self.__session.query(func.count("*"))
                    .select_from(obj)
                    .scalar()
                )
            return result

    def get_brand(self, handle):
        """Return one brand using handle or `None` if not found"""
        query = self.__session.query(Brand).filter_by(handle=handle)
        return query.one_or_none()
