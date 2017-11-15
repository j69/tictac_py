import connexion
import random
import re
from swagger_server.models.game import Game
from swagger_server.models.inline_response201 import InlineResponse201
from swagger_server.models.inline_response400 import InlineResponse400
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

games = {}
game_count = 0
ai = 'O'
client = 'X'


def api_v1_games_game_id_delete(game_id):
    """
    api_v1_games_game_id_delete
    Delete a game.
    :param game_id: Game id
    :type game_id: str

    :rtype: None
    """
    game_id = int(game_id)
    if game_id in games:
        del games[game_id]

    return games


def api_v1_games_game_id_get(game_id):
    """
    api_v1_games_game_id_get
    Get a game.
    :param game_id: Game id
    :type game_id: str

    :rtype: Game
    """
    game_id = int(game_id)
    if game_id in games:
        return games[game_id]


def api_v1_games_game_id_put(game_id, game):
    """
    api_v1_games_game_id_put
    Post a new move to a game.
    :param game_id: Game id
    :type game_id: str
    :param game: 
    :type game: dict | bytes

    :rtype: Game
    """
    if connexion.request.is_json:
        game = Game.from_dict(connexion.request.get_json())

    game_id = int(game_id)

    # player move always comes as new_board from PUT
    new_board = game.board

    # check length
    if len(new_board) != 9:
        return 'Wrong length'

    # check symbols
    if any(c not in ('X', 'O', '-') for c in new_board):
        return 'Wrong symbols'

    # ----------------------------------------
    # Make a move if there is free space left
    # ----------------------------------------

    if new_board.count('-') > 0:

        # save game
        games[game_id].board = make_a_move(new_board)

    # ----------------------------
    #   update the game state
    #
    #   symbols are numbers:
    #   'O' =   1
    #   'X' =   -1
    #   '-' =   0
    #   ----------------------------

    field = [
        int(s) for s in [
            w.replace('O', '1')
                .replace('-', '0')
                .replace('X', '-1') for w in list(games[game_id].board)
        ]
    ]

    # calculate winner
    sums = [
        sum(field[0:3]),  # rows
        sum(field[3:6]),
        sum(field[6:9]),
        sum(field[0::3]),  # columns
        sum(field[1::3]),
        sum(field[2::3]),
        sum(field[::4]),  # diagonals
        sum(field[2:-2:2])
    ]

    if 3 in sums:
        games[game_id].status = 'O_WON'
    elif -3 in sums:
        games[game_id].status = 'X_WON'
    elif 0 not in field:
        games[game_id].status = 'DRAW'

    return games[game_id].status


def api_v1_games_get():
    """
    api_v1_games_get
    Get all games.

    :rtype: List[Game]
    """
    return games


def api_v1_games_post(game):
    """
    api_v1_games_post
    Start a new game.
    :param game: 
    :type game: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        game = Game.from_dict(connexion.request.get_json())

    new_board = game.board

    # check length
    if len(new_board) != 9:
        return 'Wrong length'

    # # check symbols
    if any(c not in ('X', 'O', '-') for c in new_board):
        return 'Wrong symbols'

    # simple check
    if game.status is None:
        game.status = "RUNNING"

    # make first ai move
    game.board = make_a_move(new_board)

    # increase current games
    global game_count, games
    game_count += 1
    games[game_count] = game

    return '/api/v1/games/' + str(game_count)


def make_a_move(field):

    # find all posiible moves
    possible_moves = [m.start() for m in re.finditer('-', field)]

    # convert to list
    new = list(field)

    # change symbol
    new[random.choice(possible_moves)] = ai

    # convert back to string
    return ''.join(new)
