#!/usr/bin/python3
"""Unittest for the User class in models.user"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """User class test cases"""

        def test_user_if_subclass_of_basemodel(self):
        u_name01 = User()
        self.assertTrue(issubclass(type(u_name01), BaseModel))
        
        def test_attr_are_class_attr(self):
        u_name01 = User()
        # test if it is a class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_class_attrs(self):
        u_name01 = User()
        # test if it is a class attribute
        self.assertIs(type(u_name01.first_name), str)
        self.assertIs(type(u_name01.last_name), str)
        self.assertTrue(u_name01.first_name == "")
        self.assertTrue(u_name01.last_name == "")

