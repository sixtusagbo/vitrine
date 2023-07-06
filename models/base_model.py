#!/usr/bin/python3
"""
Base model for all models
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid
import models

Base = declarative_base()


class BaseModel:
    """Base class for all vitrine models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    format = '%Y-%m-%dT%H:%M%S.%f'
                    value = datetime.strptime(value, format)
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return informal string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.to_dict())

    def save(self):
        """Store object"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return modified version of __dict__"""
        result = {}

        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                result[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                result[key] = value
        result['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in result.keys():
            del result['_sa_instance_state']

        return result

    def delete(self):
        """Remove the current instance from storage"""
        models.storage.delete(self)
