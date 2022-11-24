#!/usr/bin/python3
"""
Module contains FileStorage class model


"""
import json

from models.base_model import BaseModel

class FileStorage:
    """
    Class FileStorage Serializes\deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns -> the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
         __objects serialize to JSON file and store to dic
        """
        with open(self.__file_path, mode="w") as F:
            dict_storage = {}
            for i, val in self.__objects.items():
                dict_storage[i] = val.to_dict()
            json.dump(dict_storage, F)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        Iff it exists!
        """
        try:
            with open(self.__file_path, 'r') as F:
                jo = json.load(F)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass
