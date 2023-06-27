import numpy as np
import player
import copy
import update_player_data as upd
import parameter as prm

# A numpy object, which contain all old data of player in old week 
# (When program is processing data of week 20, player_data stored data from week 1 to week 19)
player_data = np.empty((prm.TOTAL_PLAYERS,38), dtype=player.Player)

'''
Input:
    player is an object stored data of a Player
    x is id of this player
    y is week - 1 (Because order of table is from 0 and order of week is from 1)
Output: None
To do: Store old data to player_data for reuse.
'''
def set_player_data(player, x, y):
    player_data[x, y] = copy.deepcopy(player)

'''
Input: None
Output: None
To do: Get player_data.
'''
def get_player_data():
    return player_data
        
