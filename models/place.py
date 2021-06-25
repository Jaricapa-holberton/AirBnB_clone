#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""place module.
- Class Place - A place class to save data of the users
- Instance Attributes (public):
      - city_id: string - empty string: it will be the City.id
      - user_id: string - empty string: it will be the User.id
      - name: string - empty string
      - description: string - empty string
      - number_rooms: integer - 0
      - number_bathrooms: integer - 0
      - max_guest: integer - 0
      - price_by_night: integer - 0
      - latitude: float - 0.0
      - longitude: float - 0.0
      - amenity_ids: list of string - empty list: it will be the list of Amenity.id later
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
class Place(BaseModel):
      """A place class for storing user data, which inherits from BaseModel."""
      def __init__(self, *args, **kwargs):
        """The class constructor.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
      super().__init__(id)
      self.city_id = str("")
      self.user_id = str("")
      self.name = str("")
      self.description = str("")
      self.number_rooms = 0
      self.number_bathrooms = 0
      self.max_guest = 0
      self.price_by_night = 0
      self.latitude = 0.0
      self.longitude = 0.0
      self.amenity_ids = []