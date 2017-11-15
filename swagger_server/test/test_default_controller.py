# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.game import Game
from swagger_server.models.inline_response201 import InlineResponse201
from swagger_server.models.inline_response400 import InlineResponse400
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_api_v1_games_game_id_delete(self):
        """
        Test case for api_v1_games_game_id_delete

        
        """
        response = self.client.open('/api/v1/games/{game_id}'.format(game_id='game_id_example'),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_api_v1_games_game_id_get(self):
        """
        Test case for api_v1_games_game_id_get

        
        """
        response = self.client.open('/api/v1/games/{game_id}'.format(game_id='game_id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_api_v1_games_game_id_put(self):
        """
        Test case for api_v1_games_game_id_put

        
        """
        game = Game()
        response = self.client.open('/api/v1/games/{game_id}'.format(game_id='game_id_example'),
                                    method='PUT',
                                    data=json.dumps(game),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_api_v1_games_get(self):
        """
        Test case for api_v1_games_get

        
        """
        response = self.client.open('/api/v1/games',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_api_v1_games_post(self):
        """
        Test case for api_v1_games_post

        
        """
        game = Game()
        response = self.client.open('/api/v1/games',
                                    method='POST',
                                    data=json.dumps(game),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
