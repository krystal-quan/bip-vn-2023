import pandas as pd
import player as plr
import parameter as prm

'''
Input:
    playerList<list> is a list of Player or None
Output:
    playerList<list> is a list of Player, each Player data is up-to-date for the file 'cleaned_player.csv'
To do: Make or set data for playerList
'''
def set_player_list (playerList = None):
    cleaned_player = pd.read_csv('cleaned_player.csv')
    if (playerList is None):
        playerList = [None] * cleaned_player.shape[0]

    for index, row in cleaned_player.iterrows():
        playerList[index] = plr.Player(index + 1, row[0], row[1], row[2], row[3], 
                                           row[4], row[5], row[6], row[7], 
                                           row[8], row[9], row[10], row[11], 
                                           row[12], row[13], row[14], row[15], 
                                           row[16], row[17], row[18])
    prm.TOTAL_PLAYERS = len(playerList)
    return playerList
    
