import numpy as np
import player
import copy
import update_player_data as upd
import parameter as prm

player_data = np.empty((prm.TOTAL_PLAYERS,38), dtype=player.Player)

def set_player_data(player, x, y):
    player_data[x, y] = copy.deepcopy(player)

def get_player_data():
    return player_data

def print_player_data():
    for i in range(25):
        player_data[i, 0].print_all()
        
