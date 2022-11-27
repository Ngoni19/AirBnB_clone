#!/usr/bin/python3
"""
A module with test suite for the BaseModel class
"""
import unittest
from datetime import datetime
from uuid import uuid4
import os
from time import sleep

import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test -> for models.base_model.BaseModel
    """

    def test_if_BaseModel_inst_has_id(self):
        """
        Checks: if instance has an id assigned on initialization stage
        """
        base01 = BaseModel()
        self.assertTrue(hasattr(base01, "id"))

    def test_str_repr(self):
        """
        Checks: if the string representation is correct
        """
        b = BaseModel()
        self.assertEqual(str(b),
                         "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_type_of_id_is_str(self):
        """
        Checks: that id generated is a str obj
        """
        b02 = BaseModel()
        self.assertTrue(type(b02.id) is str)

    def test_ids_in_unique(self):
        """
        Checks: if id is  randomly generated & is unique
        """
        b01 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b01.id, b2.id)

    def test_created_at_is_datetime(self):
        """
        Checks: attribute 'created_at' is a datetime object
        """
        b03 = BaseModel()
        self.assertTrue(type(b03.created_at) is datetime)


if __name__ == "__main__":
    unittest.main()
