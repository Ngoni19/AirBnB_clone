#!/usr/bin/python3
"""Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implementation of the Review model"""
    place_id = ""
    user_id = ""
    text = ""

