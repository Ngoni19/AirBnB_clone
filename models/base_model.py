#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
BaseModel Module
All classes will inherit from this parent
"""


class BaseModel():
    """AirBnB base class
    Methods:
        __init__(self, *var, **vars)
        __str__(self)
        __repr__(self)
        __save(self)
        to_dict(self)
    """

    def __int__(self, *var, **vars):
        """
        Initialize attr: dates created/updated and uuid

        """
        if vars:
            for k, i in vars.items():
                if "created_at" == k:
                    self.created_at = datetime.strptime(vars["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == k:
                    self.updated_at = datetime.strptime(vars["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == k:
                    pass
                else:
                    setattr(self, k, i)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns-> info about model as strings
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        returns-> representation as strings
        """
        return (self.__str__())

    def save(self):
        """
        Save to serialized file after instance update time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return-> dictionary with str formats of times;add class info to dic1
        """
        dic1 = {}
        dic1["__class__"] = self.__class__.__name__
        for j, i in self.__dict__.items():
            if isinstance(i, (datetime, )):
                dic1[j] = i.isoformat()
            else:
                dic1[j] = i
        return dic1
