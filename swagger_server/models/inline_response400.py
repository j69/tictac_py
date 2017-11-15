# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse400(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, reason: str=None):
        """
        InlineResponse400 - a model defined in Swagger

        :param reason: The reason of this InlineResponse400.
        :type reason: str
        """
        self.swagger_types = {
            'reason': str
        }

        self.attribute_map = {
            'reason': 'reason'
        }

        self._reason = reason

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse400':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_400 of this InlineResponse400.
        :rtype: InlineResponse400
        """
        return deserialize_model(dikt, cls)

    @property
    def reason(self) -> str:
        """
        Gets the reason of this InlineResponse400.
        Why the game failed to start

        :return: The reason of this InlineResponse400.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """
        Sets the reason of this InlineResponse400.
        Why the game failed to start

        :param reason: The reason of this InlineResponse400.
        :type reason: str
        """

        self._reason = reason

