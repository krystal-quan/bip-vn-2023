import numpy as np
import player
import copy

players = np.empty((683,38), dtype=player.Player)

def set_players(player, x, y):
    players[x, y] = copy.deepcopy(player)

def get_players():
    return players

def print_players():
    for i in range(25):
        players[i, 0].print_all()