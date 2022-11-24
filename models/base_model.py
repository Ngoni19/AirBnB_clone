#!/usr/bin/python3
"""
Module implements the BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class to be inherited with common attr/methods for other classes
    """

    def __init__(self, *var, **vars):
        """
        Initialize BaseModel class
        """

        from models import storage
        if not vars:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, val in vars.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)

    def __str__(self):
        """
        Returns -> string representation of BaseModel object.
        In this format-> [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        'self.updated_at' updated with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns -> a dict containing all keys & values of __dict__
        of the instance:

        > instance attributes set will be returned exclusively
        > a key __class__ is added with the class name of the obj
        > created_at & updated_at converted to string obj in ISO obj
        """
        dict01 = self.__dict__.copy()
        dict01["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict01[k] = v
        return dict01
