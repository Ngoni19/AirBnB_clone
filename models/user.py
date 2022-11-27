#!/usr/bin/python3
"""User's model implementation"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from the BaseModel class
    & add user's functionalities

    Args:
        email (str): user email
        password (str): user password
        first_name (str): user first name 
        last_name (str): user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
