# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse201(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, location: str=None):
        """
        InlineResponse201 - a model defined in Swagger

        :param location: The location of this InlineResponse201.
        :type location: str
        """
        self.swagger_types = {
            'location': str
        }

        self.attribute_map = {
            'location': 'location'
        }

        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse201':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201 of this InlineResponse201.
        :rtype: InlineResponse201
        """
        return deserialize_model(dikt, cls)

    @property
    def location(self) -> str:
        """
        Gets the location of this InlineResponse201.
        URL of the started game

        :return: The location of this InlineResponse201.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """
        Sets the location of this InlineResponse201.
        URL of the started game

        :param location: The location of this InlineResponse201.
        :type location: str
        """

        self._location = location
